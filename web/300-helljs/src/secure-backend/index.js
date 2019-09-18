const express = require("express");
const cors = require("cors");
const assert = require("assert");
const jwt = require("jsonwebtoken");

const JWT_SECRET = process.env.JWT_SECRET;
const PORT = process.env.PORT;

assert.notStrictEqual(JWT_SECRET, undefined);
assert.notStrictEqual(PORT, undefined);

const app = express();

app.use(express.json());
app.use(cors());

app.get("/flag", async (req, res) => {
  const authorizationHeader = req.header("Authorization");
  if (authorizationHeader === undefined) {
    res.sendStatus(401).end();
    return;
  }

  let token;
  try {
    token = jwt.verify(authorizationHeader.slice("Bearer ".length), JWT_SECRET);
  } catch (ex) {
    res.sendStatus(401).end();
    return;
  }

  if (token.get_flag === false) {
    res.sendStatus(403).end();
    return;
  }

  res.json({
    flag: "BSidesPDX{7h3_f8_0f_my_4pp_r3575_w17h_l3f7-p4d?_cb017f1f}"
  });
});

app.listen(PORT, () =>
  console.log(`secure-backend listening on port ${PORT}!`)
);
