package main

import (
	"io"
	"net/http"
)

const usersBlob = `[
	{
		"firstName": "Kate",
		"lastName": "Libby",
		"aliases": ["Acid Burn"],
		"photo": "hackers/photos/42842/74b7f996-8b1c-4f16-ab35-4b5e99225347.jpg"
	},
	{
		"firstName": "Ramόn",
		"lastName": "Sánchez",
		"aliases": ["The Phantom Phreak"],
		"photo": "hackers/photos/38492/388c2903-4931-41ef-9900-bf6af83f3843.jpg"
	},
	{
		"firstName": "Dade",
		"lastName": "Murphy",
		"aliases": ["Zero Cool", "Crash Override", "0xdade"],
		"photo": "hackers/photos/029313/5c209e50-6304-438a-b071-e61241a724ec.jpg"
	},
	{
		"firstName": "Emmanuel",
		"lastName": "Goldstein",
		"aliases": ["Cereal Killer"],
		"photo": "hackers/photos/102932/72f2c744-ce40-45f3-92a0-af5ad142362d.jpg"
	},
	{
		"firstName": "Paul",
		"lastName": "Cook",
		"aliases": ["Lord Nikon"],
		"photo": "hackers/photos/939482/583200a8-704f-476e-b489-8f6aba2dba4b.jpg"
	},
	{
		"firstName": "Eugene",
		"lastName": "Belford",
		"aliases": ["The Plague"],
		"photo": "losers/photos/94021/OWVhMjBhMzEtZjhmYi00ODlmLWIyYTUtNDA2MGVmY2U5ODBjCg==.jpg"
	}
]`

func main() {
	http.ListenAndServe(":8080", http.HandlerFunc(func(res http.ResponseWriter, req *http.Request) {
		io.WriteString(res, usersBlob)
	}))
}
