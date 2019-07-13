package db

import (
	"os"

	"github.com/pkg/errors"

	"github.com/boltdb/bolt"
)

// DB uses bolt db to store and retrieve users.
type DB struct {
	bolt *bolt.DB
}

// Open opens a boltdb database at the given path with the given file mode
// and initializes it with the needed buckets.
func Open(path string, mode os.FileMode) (*DB, error) {
	bdb, err := bolt.Open(path, mode, nil)
	if err != nil {
		return nil, errors.Wrap(err, "unable to open bolt db")
	}

	db := &DB{bolt: bdb}

	err = db.init()
	return db, errors.Wrap(err, "unable to initialize db")
}

// Close closes the bolt db database connection.
func (db *DB) Close() error {
	return db.bolt.Close()
}

const (
	usersBucket = "users"
)

type existsErr struct {
	error
	exists bool
}

func (e existsErr) Exists() bool {
	return e.exists
}

// Exister returns a value that indicates whether the desired
// resource existed or not. This can mean different things in
// different contexts, for example in a create a true Exists()
// might mean a conflict, but in a get a false Exists() means
// the resource didn't exist.
type Exister interface {
	Exists() bool
}

// GetUser returns the hashed password for a user given their
// username. Returns an Exister if the user wasn't found.
func (db *DB) GetUser(username string) (string, error) {
	var hashedPassword string
	err := db.bolt.View(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(usersBucket))
		if bucket == nil {
			return errors.New("users bucket doesn't exist")
		}

		val := bucket.Get([]byte(username))
		if val == nil {
			return existsErr{error: errors.New("username key does not exist"), exists: false}
		}

		hashedPassword = string(val)

		return nil
	})
	return hashedPassword, err
}

// CreateUser creates a user in the database given a username and
// hashed password. Returns an Exister if the user already exists.
func (db *DB) CreateUser(username, hashedPassword string) error {
	return db.bolt.Update(func(tx *bolt.Tx) error {
		bucket := tx.Bucket([]byte(usersBucket))
		if bucket == nil {
			return errors.New("users bucket doesn't exist")
		}

		if val := bucket.Get([]byte(username)); val != nil {
			return existsErr{error: errors.New("username key already exists"), exists: true}
		}

		err := bucket.Put([]byte(username), []byte(hashedPassword))
		return errors.Wrap(err, "can't put user")
	})
}

func (db *DB) init() error {
	return db.bolt.Update(func(tx *bolt.Tx) error {
		_, err := tx.CreateBucketIfNotExists([]byte(usersBucket))
		return err
	})
}
