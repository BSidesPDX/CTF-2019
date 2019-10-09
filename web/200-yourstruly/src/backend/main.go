package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"time"

	minio "github.com/minio/minio-go/v6"
)

type Character struct {
	FirstName string   `json:"firstName"`
	LastName  string   `json:"lastName"`
	Aliases   []string `json:"aliases"`
	Photo     string   `json:"photo"`
	PhotoURL  string   `json:"photoUrl"`
}

func getRemoteCharacters(client *http.Client, serviceURL string) ([]Character, error) {
	resp, err := client.Get(serviceURL)
	if err != nil {
		return nil, fmt.Errorf("unable to make get characters request to service %q: %w", serviceURL, err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("expected a 200 OK but got %s", resp.Status)
	}

	chars := make([]Character, 0)
	if err := json.NewDecoder(io.LimitReader(resp.Body, 16384)).Decode(&chars); err != nil {
		return nil, fmt.Errorf("unable to JSON decode response: %w", err)
	}

	return chars, nil
}

func mustLoadEnv(key string) string {
	v, ok := os.LookupEnv(key)
	if !ok {
		log.Fatalf("environment variable %q was unset\n", key)
	}

	return v
}

func main() {
	minioEndpoint := mustLoadEnv("MINIO_ENDPOINT")
	accessKeyID := mustLoadEnv("MINIO_ACCESS_KEY_ID")
	secretAccessKey := mustLoadEnv("MINIO_SECRET_ACCESS_KEY")

	minioClient, err := minio.New(minioEndpoint, accessKeyID, secretAccessKey, false)
	if err != nil {
		log.Fatalln("unable to setup minio client", err)
	}

	characterService := mustLoadEnv("CHARACTER_SERVICE_URL")

	client := &http.Client{Timeout: time.Second * 5}

	http.HandleFunc("/characters", func(res http.ResponseWriter, req *http.Request) {
		serviceURL := characterService
		if debug := req.Header.Get("X-Debug-Characters"); debug != "" {
			serviceURL = debug
		}

		chars, err := getRemoteCharacters(client, serviceURL)
		if err != nil {
			http.Error(res, err.Error(), http.StatusInternalServerError)
			return
		}

		for i, v := range chars {
			u, err := minioClient.Presign(http.MethodGet, "suspects", v.Photo, time.Minute*5, nil)
			if err != nil {
				log.Println("unable to presign URL", err)
				continue
			}

			chars[i].PhotoURL = u.String()
		}

		json.NewEncoder(res).Encode(chars)
	})

	http.ListenAndServe(":8081", nil)
}
