<template lang="pug">
.inside-content.box
  <HeaderPage />
  .body-content
    .content-index
      .content
        p.subtitle Um simples sistema para cadastro e visualização de usuário.
      .button-content
        nuxt-link(to="/cadastro")
          b-button(type="is-success is-large" rounded) Criar novo usuário
        nuxt-link(to="/login")
          b-button(type="is-primary is-light is-large" rounded) Realizar Login
</template>

<script>
import { mapState } from 'vuex'
import HeaderPage from '~/components/HeaderPage.vue'
export default {
  component: {
    HeaderPage,
  },
  computed: {
    ...mapState('auth', ['loggedIn']),
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/user')
    }
  },
}
</script>

<style lang="scss" scoped>
.inside-content {
  max-width: 43.75rem;
}
.content-index {
  width: 100%;
  padding: 1.875rem;
}
</style>
