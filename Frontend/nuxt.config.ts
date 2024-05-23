// https://nuxt.com/docs/api/configuration/nuxt-config

export default ({

  ssr: false,

  css: [
    '~/assets/css/main.css',
    '~/assets/scss/index.scss',
    'vuetify/lib/styles/main.sass',
    '@mdi/font/css/materialdesignicons.min.css',
    '@fortawesome/fontawesome-svg-core/styles.css',
  ],
  build:{
    transpile:[
      '@fortawesome/fontawesome-svg-core',
      '@fortawesome/free-brands-svg-icons',
      '@fortawesome/free-regular-svg-icons',
      '@fortawesome/free-solid-svg-icons',
      '@fortawesome/vue-fontawesome',
      'mdb-vue-ui-kit',
      'vuetify',
      'cometChat'

    ],

    

  },
  
  
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },

  fontawesome: {
    icons:{
     solid:true,
     brands:true
    }
   },
 
   buildModules: [
    '@nuxt/postcss8',
    '@nuxtjs/google-fonts',
    '@nuxtjs/fontawesome',
    '@nuxtjs/vuetify',
    '@nuxtjs/axios',
    '@nuxtjs/proxy'
    // ...
  ],
  axios: {
    proxy: true,
  },

  proxy: {
    '/api/': {
      target: 'https://app.talkjs.com',
      changeOrigin: true,
      headers: {
        'Access-Control-Allow-Origin': 'http://localhost:3000',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      },
    },
  },
  
  // ...

})
