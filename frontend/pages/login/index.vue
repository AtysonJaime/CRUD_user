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
            b-input(type="password" v-model='user.senha' pack='fas' icon='lock' password-reveal rounded placeholder='Digite sua senha...')
        .button-content
          nuxt-link(to="/cadastro")
            b-button(type="is-primary is-light is-large" rounded) Criar usuário
          b-button(type="is-success is-light is-large" rounded @click='login') Entrar



</template>

<script>
import HeaderPage from '~/components/HeaderPage.vue'
export default {
  data() {
    return {
      image: require('~/assets/logo.png'),
      user: {
        login: '',
        senha: '',
      },
    }
  },
  component: {
    HeaderPage,
  },
  head: {
    title: 'CRUD User - Login',
  },
  methods: {
    async login() {
      try {
        await this.$auth.loginWith('local', {
          data: this.user,
        })
        this.$toasted.global.defaultSuccess({
          msg: 'Usuário autenticado com sucesso',
        })
      } catch (err) {
        this.$toasted.global.defaultError({
          msg: 'Usuário ou senha inválidos.',
        })
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
