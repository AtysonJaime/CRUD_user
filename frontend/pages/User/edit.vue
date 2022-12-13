<template lang="pug">
.inside-content.box
    <HeaderPage />
    .body-content
        .content-cadastro
            .content
                p.subtitle Edite suas informações <b>{{user.name}}</b>
            .form-cadastro
                .content-field
                  b-field(label='Deseja alterar a senha ?')
                    b-switch(type='is-success' v-model="userEdit.changeSenha" true-value="Sim" false-value="Não") {{userEdit.changeSenha}}
                  b-field(label='Deseja alterar o E-mail ?')
                    b-switch(type='is-success' v-model="userEdit.changeEmail" true-value="Sim" false-value="Não") {{userEdit.changeEmail}}
                .content-field
                    b-field(label='Nome' :type="{'is-danger':error.name !== ''}" :message='error.name')
                        b-input(v-model='userEdit.name' rounded require)
                    b-field(v-show='userEdit.changeEmail === "Sim"' label="E-Mail" :type="{'is-danger':error.email !== ''}" :message='error.email')
                        b-input(type="email" v-model='userEdit.newEmail' rounded require)

                .content-field(v-show='userEdit.changeSenha === "Sim"')
                    b-field(label='Senha' :type="{'is-danger':error.password !== ''}" :message='error.password')
                        b-tooltip(label='Senha precisar ter mais que 8 digitos e conter @!_- e letras e numeros')
                            b-input(type='password' v-model='userEdit.password' rounded require password-reveal)
                    b-field(label="Confirme a Senha" :type="{'is-danger':error.confirmepassword !== ''}" :message='error.confirmepassword')
                        b-input(type='password' v-model='userEdit.confirmepassword' rounded require password-reveal)
                .content-field
                    b-field(label='País' :type="{'is-danger':error.pais !== ''}" :message='error.pais')
                        b-input(v-model='userEdit.pais' rounded require)
                    b-field(label="Estado" :type="{'is-danger':error.estado !== ''}" :message='error.estado')
                        b-input(v-model='userEdit.estado' rounded require)
                .content-field
                    b-field(label='Município' :type="{'is-danger':error.municipio !== ''}" :message='error.municipio')
                        b-input(v-model='userEdit.municipio' rounded require)
                    b-field(label="CEP" :type="{'is-danger':error.cep !== ''}" :message='error.cep')
                        b-input(v-model='userEdit.cep' rounded require v-cleave='marks.cepCustom' max-length='10')
                .content-field
                    b-field(label='Rua' :type="{'is-danger':error.rua !== ''}" :message='error.rua')
                        b-input(v-model='userEdit.rua' rounded require)
                .content-field
                    b-field(label='Numero' :type="{'is-danger':error.numero !== ''}" :message='error.numero')
                        b-input(type='number' v-model='userEdit.numero' rounded require)
                    b-field(label="Complemento")
                        b-input(v-model='userEdit.complemento' rounded)
                .content-field
                    b-field(label='CPF' :type="{'is-danger':error.cpf !== ''}" :message='error.cpf')
                        b-input(v-model='userEdit.cpf' rounded require v-cleave='marks.cpf' max-length='14')
                    b-field(label="PIS" :type="{'is-danger':error.pis !== ''}" :message='error.pis')
                        b-input(v-model='userEdit.pis' rounded v-cleave='marks.pis' max-length='18')
            .button-content
                nuxt-link(to="/user")
                    b-button(type="is-danger is-light is-large" icon-left='arrow-left' rounded) Cancelar
                b-button(type="is-danger is-large" icon-left="delete" rounded :loading='isLoadingDel') Deletar
                b-button(type="is-info is-large" icon-left="pencil" rounded @click='editar' :loading='isLoading') Editar
</template>

<script>
import Cleave from 'cleave.js'
import { mapState } from 'vuex'
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
      isLoading: false,
      isLoadingDel: false,
      userEdit: {
        name: '',
        email: '',
        newEmail: '',
        changeEmail: 'Não',
        changeSenha: 'Não',
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
  head: {
    title: 'CRUD User - Editar Usuário',
  },
  computed: {
    ...mapState('auth', ['loggedIn', 'user']),
  },
  created() {
    if (!this.loggedIn) {
      this.$router.push('/login')
    }
  },
  mounted() {
    this.userEdit.name = this.user.name
    this.userEdit.email = this.user.email
    this.userEdit.newEmail = this.user.email
    this.userEdit.pais = this.user.pais
    this.userEdit.estado = this.user.estado
    this.userEdit.municipio = this.user.municipio
    this.userEdit.cep = this.user.cep
    this.userEdit.rua = this.user.rua
    this.userEdit.numero = this.user.numero
    this.userEdit.complemento = this.user.complemento
    this.userEdit.cpf = this.user.cpf
    this.userEdit.pis = this.user.pis
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
    validaFormTypeEmail() {
      const RegEx = /^[\w-.]+@([\w-]+.)+[\w-]{2,4}$/

      if (this.userEdit.newEmail === '') {
        this.error.email = 'Esse campo é obrigatorio'
        this.ahError = true
      } else if (!RegEx.test(this.userEdit.newEmail)) {
        this.error.email = 'Adicione um email valido'
        this.ahError = true
      } else {
        this.error.email = ''
      }
    },
    validaFormTypePassword() {
      const RegEx = /[-.@!_]/
      if (this.userEdit.password === '') {
        this.error.password = 'Campo é obrigatorio'
        this.ahError = true
      } else {
        const error = []
        let ahErroAqui = false
        if (!RegEx.test(this.userEdit.password)) {
          error.push('Campo precisar conter um dos seguintes caracteres: @!_-')
          this.ahError = true
          ahErroAqui = true
        }
        if (this.userEdit.password.length < 8) {
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
      if (this.userEdit.confirmepassword === '') {
        this.error.confirmepassword = 'Campo é obrigatorio'
        this.ahError = true
      } else if (this.userEdit.confirmepassword !== this.userEdit.password) {
        this.error.confirmepassword = 'As senhas estão diferentes'
        this.ahError = true
      } else {
        this.error.confirmepassword = ''
      }
    },
    validaFormTypeText(inputName) {
      if (this.userEdit[inputName] === '') {
        this.error[inputName] = 'Esse campo é obrigatorio'
        this.ahError = true
      } else {
        this.error[inputName] = ''
      }
    },
    validaFormTypeNumber(inputName, quantidade) {
      if (this.userEdit[inputName] === '') {
        this.error[inputName] = 'Esse campo é obrigatorio'
      } else if (this.userEdit[inputName] < quantidade) {
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
      if (this.userEdit.changeEmail === 'Sim') {
        this.validaFormTypeEmail()
      }
      if (this.userEdit.changeSenha === 'Sim') {
        this.validaFormTypePassword()
      }
    },
    async editar() {
      this.ahError = false
      this.isLoading = true
      this.validaForm()
      if (!this.ahError) {
        const data = this.userEdit
        data.cpf = this.replaceItens(data.cpf)
        data.pis = this.replaceItens(data.pis)
        data.cep = this.replaceItens(data.cep)
        data.cpf = data.cpf.length > 11 ? data.cpf.substr(0, 11) : data.cpf
        data.pis = data.pis.length > 14 ? data.pis.substr(0, 14) : data.pis
        data.cep = data.cep.length > 8 ? data.cep.substr(0, 8) : data.cep
        data.complemento = data.complemento === '' ? 'vazio' : data.complemento

        try {
          const res = await this.$axios.put('/update', data)
          // eslint-disable-next-line no-console
          console.log(res)
          this.$axios
            .get('/user')
            .then((resposta) => {
              this.$auth.setUser(resposta.data.user)
              this.$toasted.global.defaultSuccess({
                msg: `Informações editadas com sucesso`,
              })
              this.$router.push('/user')
            })
            .catch((err) => {
              this.$toasted.global.defaultSuccess({
                msg: `Algo deu errado ao salvar edição, verificar console`,
              })
              // eslint-disable-next-line no-console
              console.log(err)
            })
        } catch (err) {
          // eslint-disable-next-line no-console
          console.log(err)
          this.isLoading = false
          this.$toasted.global.defaultError({
            msg: `Error inesperado ao editar o usuario: ${err}. Verificar console.log!`,
          })
        }
      } else {
        this.isLoading = false
        this.$toasted.global.defaultError({
          msg: 'Formulário apresenta algum erro, por favor verificar.',
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
@import '~/assets/sass/main.scss';
.inside-content {
  max-width: 50rem;
  overflow: auto;
  height: 80vh;
}
.content-cadastro {
  width: 100%;
  padding: 0.625rem;
  .form-cadastro {
    margin-bottom: 1.25rem;
    .b-tooltip {
      width: 100%;
    }
    .content-field {
      display: flex;
      justify-content: space-between;

      @media (max-width: '700px') {
        flex-wrap: wrap;
      }

      .field {
        width: 100%;
        padding: 0.625rem;
      }
    }
  }
}
</style>
