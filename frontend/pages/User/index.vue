<template lang="pug">
.inside-content.box
  <HeaderPage />
  .body-content
    .content-index
      .content
        p.subtitle Ola <b>{{this.user.name}}</b>
      .button-content
        b-button(type="is-dark is-large" icon-left='exit-to-app' rounded @click='logout') Deslogar
        nuxt-link(to="/user/edit")
          b-button(type="is-info is-large" icon-left="pencil" rounded) Editar
</template>

<script>
import { mapState } from 'vuex'
import HeaderPage from '~/components/HeaderPage.vue'
export default {
  component: {
    HeaderPage,
  },
  head: {
    title: 'CRUD User - User',
  },
  computed: {
    ...mapState('auth', ['loggedIn', 'user']),
  },
  created() {
    if (!this.loggedIn) {
      this.$router.push('/login')
      this.$toasted.global.defaultSuccess({
        msg: 'Usuário deslogado',
      })
    }
  },
  methods: {
    async logout() {
      await this.$auth.logout()
    },
  },
}
</script>

<style lang="scss" scoped>
.inside-content {
  max-width: 43.75rem;
  overflow: auto;
  height: 80vh;
}
.content-index {
  width: 100%;
  padding: 0.625rem;
}
</style>
