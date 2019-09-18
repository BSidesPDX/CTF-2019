<template>
  <div class="login">
    <form v-on:submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <input type="submit" value="Login" />
    </form>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
      const resp = await fetch(`${process.env.VULNERABLE_API_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      });

      const body = await resp.json();

      window.localStorage.setItem('token', body.token);

      this.$router.push('customers');
    },
  },
};
</script>

<style scoped>
.login {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 200px;
}

.login input {
  margin: 0.3em;
  padding: 1em;
  border: none;
  box-shadow: none;
  border: thin solid gray;
  border-radius: 5px;
}

.login input[type="submit"] {
  background: lightpink;
  border: none;
}
</style>
