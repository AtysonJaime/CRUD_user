<template lang="pug">
  header.header
    b-image(:src='image')
    h1.title CRUD de Usuário
</template>

<script>
export default {
  data() {
    return {
      image: require('~/assets/logo.png'),
    }
  },
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  padding: 0.625rem;
  border-bottom: 0.125rem solid #2980b9;
  .image {
    margin: 0;
    width: 2.5rem;
    margin-right: 0.625rem;
  }
}
</style>
