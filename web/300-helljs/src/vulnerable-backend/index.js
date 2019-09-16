const express = require("express");
const cors = require("cors");
const { MongoClient } = require("mongodb");
const assert = require("assert");
const customers = require("./customers.json");
const jwt = require("jsonwebtoken");

const MONGODB_URL = process.env.MONGODB_URL;
const MONGODB_DB_NAME = process.env.MONGODB_DB_NAME;
const JWT_SECRET = process.env.JWT_SECRET;
const PORT = process.env.PORT;

assert.notStrictEqual(MONGODB_URL, undefined);
assert.notStrictEqual(JWT_SECRET, undefined);
assert.notStrictEqual(PORT, undefined);

const app = express();

const client = new MongoClient(MONGODB_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

app.use(express.json());
app.use(cors());

client.connect(async err => {
  assert.strictEqual(null, err);
  const db = client.db(MONGODB_DB_NAME);

  const usersCollection = db.collection("users");
  usersCollection.updateOne(
    {
      _id: "123"
    },
    {
      $set: {
        username: "franklin",
        password: "password"
      }
    },
    {
      upsert: true
    }
  );

  app.post("/login", async (req, res) => {
    const usersCollection = db.collection("users");

    const user = await usersCollection.findOne({
      username: req.body.username,
      password: req.body.password
    });

    if (user == null) {
      res.sendStatus(401).end();
      return;
    }

    const token = jwt.sign(
      { sub: user._id, username: user.username, get_flag: false },
      JWT_SECRET
    );

    res.json({ token });
  });

  app.get("/customers", async (req, res) => {
    const authorizationHeader = req.header("Authorization");
    if (authorizationHeader === undefined) {
      res.sendStatus(401).end();
      return;
    }

    try {
      jwt.verify(authorizationHeader.slice("Bearer ".length), JWT_SECRET);
    } catch (ex) {
      res.sendStatus(401).end();
      return;
    }

    const filterFunc = new Function("customer", req.query.filter);

    // deep copy customers so they can't modify the actual customers list
    res.json(JSON.parse(JSON.stringify(customers)).filter(filterFunc));
  });

  await app.listen(PORT, () =>
    console.log(`vulnerable-backend listening on port ${PORT}!`)
  );

  client.close();
});
