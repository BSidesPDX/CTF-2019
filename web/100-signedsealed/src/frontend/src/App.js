import React from "react";
import "./App.css";

const API_URL = process.env.API_URL;

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
      error: "",
      flag: ""
    };

    this.login = this.login.bind(this);
    this.logout = this.logout.bind(this);
    this.register = this.register.bind(this);
    this.getFlag = this.getFlag.bind(this);
    this.decodedJWT = this.decodedJWT.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  jwt() {
    return localStorage.getItem("jwt");
  }

  setJWT(jwt) {
    if (!jwt) {
      localStorage.removeItem("jwt");
      return;
    }

    localStorage.setItem("jwt", jwt);
  }

  decodedJWT() {
    const jwt = this.jwt();
    if (!jwt) {
      return {};
    }

    const [h, p] = jwt
      .split(".")
      .slice(0, 2)
      .map(v => JSON.parse(atob(v)));
    return { header: h, payload: p };
  }

  async login(event) {
    event.preventDefault();

    try {
      const resp = await fetch(`${API_URL}/authenticate`, {
        method: "POST",
        body: JSON.stringify({
          username: this.state.username,
          password: this.state.password
        })
      });

      if (!resp.ok) {
        throw new Error(resp.status);
      }

      const jwt = (await resp.json()).jwt;

      this.setJWT(jwt);
      this.setState({ error: "", message: "" });
    } catch (ex) {
      this.setState({ error: ex.message });
    }
  }

  logout(event) {
    event.preventDefault();

    this.setJWT("");
    this.setState({ error: "", message: "Logged Out", username: "", password: "" });
  }

  async register(event) {
    event.preventDefault();

    try {
      const resp = await fetch(`${API_URL}/users`, {
        method: "POST",
        body: JSON.stringify({
          username: this.state.username,
          password: this.state.password
        })
      });

      if (!resp.ok) {
        throw new Error(resp.statusText);
      }

      this.setState({ error: "", message: "Created user" });
    } catch (ex) {
      this.setState({ error: ex.message });
    }
  }

  async getFlag(event) {
    event.preventDefault();

    try {
      const resp = await fetch(`${API_URL}/flag`, {
        headers: new Headers({ Authorization: `Bearer ${this.jwt()}` })
      });
      if (!resp.ok) {
        throw new Error(resp.statusText);
      }

      const flag = (await resp.json()).flag;

      this.setState({ flag });
    } catch (ex) {
      this.setState({ error: ex.message });
    }
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  render() {
    return (
      <div className="App">
        <h1>Signed, Sealed, Delivered, I'm Yours!</h1>
        {this.state.error && <p className="error">{this.state.error}</p>}
        {this.state.message && <p>{this.state.message}</p>}
        {this.jwt() ? (
          <>
            <p>Welcome {this.decodedJWT().payload.sub}</p>
            <input onClick={this.logout} type="button" value="Log Out" />
            <input type="button" value="Get flag" onClick={this.getFlag} />
          </>
        ) : (
          <form>
            <input
              value={this.state.username}
              onChange={this.handleChange}
              name="username"
              type="text"
              placeholder="Username"
            />
            <input
              value={this.state.password}
              onChange={this.handleChange}
              name="password"
              type="password"
              placeholder="Password"
            />
            <div className="buttons">
              <input onClick={this.login} type="button" value="Login" />
              <input onClick={this.register} type="button" value="Register" />
            </div>
          </form>
        )}
        {this.state.flag && <p>Flag: {this.state.flag}</p>}
      </div>
    );
  }
}

export default App;
