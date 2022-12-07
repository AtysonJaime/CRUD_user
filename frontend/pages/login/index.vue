<template lang="pug">
  .content-login.box
    .content
      .header
        b-image(:src='image')
        h1.title CRUD de Usuário
      p.subtitle Um simples sistema para cadastro e visualização de usuário.
    .form-login
      b-field(label='Login')
        b-tooltip(label='Acessar utilizando Email, CPF ou PIS')
          b-input(v-model='user.login' icon='account' rounded)
      b-field(label="Senha")
        b-input(type="password" v-model='user.senha' pack='fas' icon='lock' password-reveal rounded)
    .button-content
      b-button(type="is-primary is-light is-large" rounded) Criar usuário
      b-button(type="is-success is-light is-large" rounded @click='login') Entrar



</template>

<script>
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
.content-login {
  max-width: 500px;
  width: 100%;
  padding: 1.875rem;

  .content {
    .title {
      font-size: 2rem;
      font-weight: 500;
      line-height: 1.125;
      color: #363636;
      margin: 0;
    }
    .subtitle {
      color: #7a7a7a;
      font-size: 1.25rem;
      font-weight: 400;
      line-height: 1.25;
      text-align: center;
    }
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
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    padding: 1.875rem;
  }
}
</style>
