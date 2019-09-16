<template>
  <div class="customers">
    <input type="text" placeholder="query" v-on:change="getCustomers" v-model="filter" />
    <table>
      <tr>
        <td>ID</td>
        <td>First Name</td>
        <td>Last Name</td>
        <td>Gender</td>
        <td>E-Mail</td>
        <td>IP Address</td>
      </tr>
      <tr v-for="customer in customers" :key="customer.id">
        <td>{{customer.id}}</td>
        <td>{{customer.first_name}}</td>
        <td>{{customer.last_name}}</td>
        <td>{{customer.gender}}</td>
        <td>{{customer.email}}</td>
        <td>{{customer.ip_address}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Customers',
  data() {
    return {
      customers: [],
      filter: 'return true;',
    };
  },
  async created() {
    await this.getCustomers();
  },
  methods: {
    async getCustomers() {
      const url = new URL(`${process.env.VULNERABLE_API_URL}/customers`);
      url.searchParams.append('filter', this.filter);

      const resp = await fetch(url, {
        headers: {
          Authorization: `Bearer ${window.localStorage.getItem('token')}`,
        },
      });

      this.customers = await resp.json();
    },
  },
};
</script>

<style scoped>
table {
  border-collapse: collapse;
}

td {
  padding: 1em;
  margin: 0;
  background: #fff;
  border-bottom: thin solid black;
}

input {
  margin: 0.3em;
  padding: 1em;
  border: none;
  box-shadow: none;
  border: thin solid gray;
  border-radius: 5px;
}
</style>
