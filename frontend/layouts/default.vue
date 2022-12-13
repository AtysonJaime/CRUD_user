<template lang="pug">
  .main-content
    Nuxt
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>

<style lang="scss">
body,
html {
  overflow: auto !important;
}

.main-content {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  padding: 1.875rem;
  width: 100%;
  height: 100vh;
  background: #2980b9
    url('https://static.tumblr.com/03fbbc566b081016810402488936fbae/pqpk3dn/MRSmlzpj3/tumblr_static_bg3.png')
    repeat 0 0;
  -webkit-animation: 10s linear 0s normal none infinite animate;
  -moz-animation: 10s linear 0s normal none infinite animate;
  -ms-animation: 10s linear 0s normal none infinite animate;
  -o-animation: 10s linear 0s normal none infinite animate;
  animation: 10s linear 0s normal none infinite animate;

  .inside-content {
    width: 100%;
  }
  .title {
    font-size: 2.1875rem;
    font-weight: 500;
    line-height: 1.125;
    color: #363636;
    margin: 0;
  }
  .subtitle {
    color: #7a7a7a;
    font-size: 1.55rem;
    font-weight: 400;
    line-height: 1.25;
    text-align: center;
  }
  .button-content {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    padding: 0.9375rem;

    a {
      padding: 0.625rem;
      button {
        margin: 0;
      }
    }
    button {
      margin: 0.625rem;
    }
  }
}
@-webkit-keyframes animate {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 500px 0;
  }
}

@-moz-keyframes animate {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 500px 0;
  }
}

@-ms-keyframes animate {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 500px 0;
  }
}

@-o-keyframes animate {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 500px 0;
  }
}

@keyframes animate {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 500px 0;
  }
}
</style>
