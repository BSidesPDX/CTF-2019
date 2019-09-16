<template>
  <div class="flag">
    <h3>{{flag}}</h3>
  </div>
</template>

<script>
export default {
  name: 'Flag',
  data() {
    return {
      flag: '',
    };
  },
  async created() {
    const resp = await fetch(`${process.env.SECURE_API_URL}/flag`, {
      headers: {
        Authorization: `Bearer ${window.localStorage.getItem('token')}`,
      },
    });

    if (resp.status !== 200) {
      return;
    }

    this.flag = (await resp.json()).flag;
  },
};
</script>

<style scoped>
</style>
