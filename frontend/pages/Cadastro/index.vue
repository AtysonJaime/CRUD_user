<template lang="pug">
.inside-content.box
    <HeaderPage />
    .body-content
        .content-cadastro
            .content
                p.subtitle Realize seu cadastro.
            .form-cadastro
                .content-field
                    //- :type="{ 'is-danger': hasError }"
                    //- :message="{ 'Username is not available': hasError }"
                    b-field(label='Nome' :type="{'is-danger':error.name !== ''}" :message='error.name')
                        b-input(v-model='user.name' rounded require)
                    b-field(label="E-Mail" :type="{'is-danger':error.email !== ''}" :message='error.email')
                        b-input(type="email" v-model='user.email' rounded require)
                .content-field
                    b-field(label='Senha' :type="{'is-danger':error.password !== ''}" :message='error.password')
                        b-tooltip(label='Senha precisar ter mais que 8 digitos e conter @!_- e letras e numeros')
                            b-input(type='password' v-model='user.password' rounded require password-reveal)
                    b-field(label="Confirme a Senha" :type="{'is-danger':error.confirmepassword !== ''}" :message='error.confirmepassword')
                        b-input(type='password' v-model='user.confirmepassword' rounded require password-reveal)
                .content-field
                    b-field(label='País' :type="{'is-danger':error.pais !== ''}" :message='error.pais')
                        b-input(v-model='user.pais' rounded require)
                    b-field(label="Estado" :type="{'is-danger':error.estado !== ''}" :message='error.estado')
                        b-input(v-model='user.estado' rounded require)
                .content-field
                    b-field(label='Município' :type="{'is-danger':error.municipio !== ''}" :message='error.municipio')
                        b-input(v-model='user.municipio' rounded require)
                    b-field(label="CEP" :type="{'is-danger':error.cep !== ''}" :message='error.cep')
                        b-input(v-model='user.cep' rounded require v-cleave='marks.cepCustom' max-length='10')
                .content-field
                    b-field(label='Rua' :type="{'is-danger':error.rua !== ''}" :message='error.rua')
                        b-input(v-model='user.rua' rounded require)
                .content-field
                    b-field(label='Numero' :type="{'is-danger':error.numero !== ''}" :message='error.numero')
                        b-input(type='number' v-model='user.numero' rounded require)
                    b-field(label="Complemento")
                        b-input(v-model='user.complemento' rounded)
                .content-field
                    b-field(label='CPF' :type="{'is-danger':error.cpf !== ''}" :message='error.cpf')
                        b-input(v-model='user.cpf' rounded require v-cleave='marks.cpf' max-length='14')
                    b-field(label="PIS" :type="{'is-danger':error.pis !== ''}" :message='error.pis')
                        b-input(v-model='user.pis' rounded v-cleave='marks.pis' max-length='18')
            .button-content
                nuxt-link(to="/login")
                    b-button(type="is-danger is-light is-large" rounded) Cancelar
                b-button(type="is-success is-light is-large" rounded @click='cadastrar') Cadastrar
</template>

<script>
import Cleave from 'cleave.js'
import HeaderPage from '~/components/HeaderPage.vue'

const cleave = {
  name: 'cleave',
  bind(el, binding) {
    const input = el.querySelector('input')
    input._vCleave = new Cleave(input, binding.value)
  },
  unbind(el) {
    const input = el.querySelector('input')
    input._vCleave.destroy()
  },
}

export default {
  comments: {
    HeaderPage,
  },
  directives: { cleave },
  data() {
    return {
      user: {
        name: '',
        email: '',
        password: '',
        confirmepassword: '',
        pais: '',
        estado: '',
        municipio: '',
        cep: '',
        rua: '',
        numero: '',
        complemento: '',
        cpf: '',
        pis: '',
      },
      marks: {
        cepCustom: {
          delimiters: ['.', '-'],
          blocks: [2, 3, 3],
          numericOnly: true,
        },
        cpf: {
          delimiters: ['.', '.', '-'],
          blocks: [3, 3, 3, 2],
          numericOnly: true,
        },
        pis: {
          delimiters: ['.', '.', '/', '-'],
          blocks: [2, 3, 3, 4, 2],
          numericOnly: true,
        },
      },
      error: {
        name: '',
        email: '',
        password: '',
        confirmepassword: '',
        pais: '',
        estado: '',
        municipio: '',
        cep: '',
        rua: '',
        numero: '',
        cpf: '',
        pis: '',
      },
      ahError: false,
    }
  },
  methods: {
    replaceItens(s) {
      let item = s
      item = item
        .replace('.', '')
        .replace('.', '')
        .replace('.', '')
        .replace('-', '')
        .replace('/', '')
      return item
    },
    validaFormTypeText(inputName) {
      if (this.user[inputName] === '') {
        this.error[inputName] = 'Esse campo é obrigatorio'
        this.ahError = true
      } else {
        this.error[inputName] = ''
      }
    },
    validaFormTypeEmail() {
      const RegEx = /^[\w-.]+@([\w-]+.)+[\w-]{2,4}$/

      if (this.user.email === '') {
        this.error.email = 'Esse campo é obrigatorio'
        this.ahError = true
      } else if (!RegEx.test(this.user.email)) {
        this.error.email = 'Adicione um email valido'
        this.ahError = true
      } else {
        this.error.email = ''
      }
    },
    validaFormTypePassword() {
      const RegEx = /[-.@!_]/
      if (this.user.password === '') {
        this.error.password = 'Campo é obrigatorio'
        this.ahError = true
      } else {
        const error = []
        let ahErroAqui = false
        if (!RegEx.test(this.user.password)) {
          error.push('Campo precisar conter um dos seguintes caracteres: @!_-')
          this.ahError = true
          ahErroAqui = true
        }
        if (this.user.password.length < 8) {
          error.push('Campo precisar ter no minimo 8 caracteres')
          this.ahError = true
          ahErroAqui = true
        }
        if (ahErroAqui) {
          this.error.password = error
        } else {
          this.error.password = ''
        }
      }
      if (this.user.confirmepassword === '') {
        this.error.confirmepassword = 'Campo é obrigatorio'
        this.ahError = true
      } else if (this.user.confirmepassword !== this.user.password) {
        this.error.confirmepassword = 'As senhas estão diferentes'
        this.ahError = true
      } else {
        this.error.confirmepassword = ''
      }
    },
    validaFormTypeNumber(inputName, quantidade) {
      if (this.user[inputName] === '') {
        this.error[inputName] = 'Esse campo é obrigatorio'
      } else if (this.user[inputName] < quantidade) {
        this.error[inputName] = `A campo precisa ter ${quantidade} caracteres`
        this.ahError = true
      } else {
        this.error[inputName] = ''
      }
    },
    validaForm() {
      this.validaFormTypeText('name')
      this.validaFormTypeText('pais')
      this.validaFormTypeText('municipio')
      this.validaFormTypeText('estado')
      this.validaFormTypeNumber('cep', 10)
      this.validaFormTypeText('rua')
      this.validaFormTypeText('numero')
      this.validaFormTypeNumber('cpf', 14)
      this.validaFormTypeNumber('pis', 18)
      this.validaFormTypeEmail()
      this.validaFormTypePassword()
    },
    async cadastrar() {
      this.validaForm()
      if (!this.ahError) {
        const data = this.user
        data.cpf = this.replaceItens(data.cpf)
        data.pis = this.replaceItens(data.pis)
        data.cep = this.replaceItens(data.cep)
        data.cpf = data.cpf.length > 11 ? data.cpf.substr(0, 11) : data.cpf
        data.pis = data.pis.length > 14 ? data.pis.substr(0, 14) : data.pis
        data.cep = data.cep.length > 8 ? data.cep.substr(0, 8) : data.cep
        data.complemento = data.complemento === '' ? 'vazio' : data.complemento

        try {
          const res = await this.$axios.post('/cadastrar', data)
          // eslint-disable-next-line no-console
          console.log(res)
          this.$toasted.global.defaultSuccess({
            msg: `Usuário cadastrado com sucesso`,
          })
          this.$route.push('/login')
        } catch (err) {
          // eslint-disable-next-line no-console
          console.log(err)
          this.$toasted.global.defaultError({
            msg: `Error inesperado ao cadastrar usuario: ${err}. Verificar console.log!`,
          })
        }
      } else {
        this.$toasted.global.defaultError({
          msg: 'Formulário apresenta algum erro, por favor verificar.',
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.inside-content {
  max-width: 50rem;
  overflow: auto;
  height: 80vh;
}
.content-cadastro {
  width: 100%;
  padding: 1.875rem;
  .form-cadastro {
    margin-bottom: 1.25rem;
    .b-tooltip {
      width: 100%;
    }
    .content-field {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;

      .field {
        width: 100%;
        padding: 0.625rem;
      }
    }
  }
}
</style>
