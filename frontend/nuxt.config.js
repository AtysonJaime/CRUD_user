export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'CRUD User',
    htmlAttrs: {
      lang: 'pt-br',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: 'Simples sistema de cadastro de usuários',
      },
      {
        hid: 'designer',
        name: 'designer',
        content: 'Atyson Jaime <atysonjaime@gmail.com>',
      },
      { hid: 'og:type', name: 'og:type', content: 'website' },
      { hid: 'og:title', name: 'og:title', content: 'CRUDUser' },
      {
        hid: 'og:description',
        name: 'og:description',
        content: 'Simples sistema de cadastro de usuários',
      },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    // https://go.nuxtjs.dev/stylelint
    '@nuxtjs/stylelint-module',
  ],

  modules: [
    'nuxt-buefy',
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/toast',
  ],

  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        localStorage: {
          prefix: 'auth.',
        },
        token: {
          prefix: 'access_token.',
          property: 'access_token',
          maxAge: 86400,
          type: 'Bearer',
        },
        refreshToken: {
          prefix: 'refresh_token.',
          property: 'refresh_token',
          data: 'refresh_token',
          maxAge: 60 * 60 * 24 * 15,
        },
        user: {
          property: 'user',
          autoFetch: true,
        },
        endpoints: {
          login: { url: '/login', method: 'post' },
          refresh: { url: '/token/refresh/', method: 'post' },
          user: { url: '/user', method: 'get' },
          logout: { url: '/logout', method: 'post' },
        },
      },
    },
  },

  axios: {
    baseURL: 'http://localhost:8000/api/v1/',
  },

  toast: {
    position: 'top-center',
    iconPack: 'fontawesome',
    duration: 3000,
    register: [
      {
        name: 'defaultSuccess',
        message: (payload) =>
          !payload.msg ? 'Operação bem sucedida' : payload.msg,
        options: {
          type: 'success',
          icon: 'check',
        },
      },
      {
        name: 'defaultError',
        message: (payload) =>
          !payload.msg ? 'Oops.. Erro inesperado' : payload.msg,
        options: {
          type: 'error',
          icon: 'times',
        },
      },
    ],
  },

  styleResources: {
    scss: ['assets/sass/main.scss'],
  },

  build: {},
}
