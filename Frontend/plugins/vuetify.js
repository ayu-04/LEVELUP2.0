// plugins/vuetify.js
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    ssr: true,
    components,
    directives,
    theme:{
      themes:{
        'background':'#2F2F2F',
        'green-dark': '#54B646',
        'green-med':'#98F286',
        'green-light':'#C5FFB6',
        'violet-dark':'#5546B6',
        'violet-med':'#BDB8FF',
        'violet-light':'#BDB8FF',
        'pink-dark':'#B6468A',
        'pink-med':'#F286CB',
        'pink-light':'#FFB6E8',
        'text-primary':'#FFFFFF',
      }
    }
  })

  nuxtApp.vueApp.use(vuetify)
})
