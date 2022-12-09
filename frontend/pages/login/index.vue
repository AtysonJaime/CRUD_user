<template lang="pug">
  .inside-content.box
    <HeaderPage />
    .body-content
      .content-login
        .content
          p.subtitle Bem vindo, visitante!
        .form-login
          b-field(label='Login')
            b-tooltip(label='Acessar utilizando Email, CPF ou PIS')
              b-input(v-model='user.login' icon='account' rounded placeholder='Digite seu login...')
          b-field(label="Senha")
            b-input(type="password" v-model='user.password' pack='fas' icon='lock' password-reveal rounded placeholder='Digite sua senha...')
        .button-content
          nuxt-link(to="/cadastro")
            b-button(type="is-primary is-light is-large" rounded) Criar usuário
          b-button(type="is-success is-large" rounded @click='login' :loading='isLoading') Entrar



</template>

<script>
import { mapState } from 'vuex'
import HeaderPage from '~/components/HeaderPage.vue'
export default {
  data() {
    return {
      image: require('~/assets/logo.png'),
      isLoading: false,
      user: {
        login: '',
        password: '',
      },
    }
  },
  component: {
    HeaderPage,
  },
  head: {
    title: 'CRUD User - Login',
  },
  computed: {
    ...mapState('auth', ['loggedIn']),
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/user')
    }
  },
  methods: {
    async login() {
      this.isLoading = true
      try {
        const response = await this.$auth.loginWith('local', {
          data: this.user,
        })
        // Guarda no localStorege
        this.$auth.$storage.setUniversal('email', response.data.email)
        this.$auth.setUser(response.data)
        await this.$auth.setUserToken(
          response.data.access_token,
          response.data.refresh_token
        )
        this.$toasted.global.defaultSuccess({
          msg: 'Usuário autenticado com sucesso',
        })
      } catch (err) {
        this.isLoading = false
        this.$toasted.global.defaultError({
          msg: 'Usuário ou senha inválidos.',
        })
        console.log(err.message)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.inside-content {
  max-width: 31.25rem;
}
.content-login {
  width: 100%;
  padding: 1.875rem;

  .content {
    .header {
      display: flex;
      align-items: center;
      justify-content: center;
      .image {
        margin: 0;
        width: 15%;
        margin-right: 0.625rem;
      }
    }
  }
  .form-login {
    margin-bottom: 1.25rem;
    .b-tooltip {
      width: 100%;
    }
  }
  .button-content {
    padding: 0.9375rem;
  }
}
</style>
