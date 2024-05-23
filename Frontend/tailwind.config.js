/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./components/**/*.{js,vue,ts}",
      "./layouts/**/*.vue",
      "./pages/**/*.vue",
      "./plugins/**/*.{js,ts}",
      "./nuxt.config.{js,ts}",
      "./app.vue",
  ],
  theme: {
    extend: {
      colors:{
        'background':'#242424',
        'bg-secondary':"#2F2F2F",
        'green-dark': '#54B646',
        'green-med':'#98F286',
        'green-light':'#C5FFB6',
        'violet-dark':'#5546B6',
        'violet-med':'#BDB8FF',
        'violet-light':'#BDB8FF',
        'pink-dark':'#B6468A',
        'pink-med':'#F286CB',
        'pink-light':'#FFB6E8',
        'text-primary':'#DCDCDC',
        'text-secondary':"#9A9A9A",
        'secondary':"#484848",
        'danger-red':'#FA5757',
      },
      backgroundImage:{
        'login-window':"url(./assets/images/loginwindow.svg)",
      },
      fontFamily:{
        'sans-serif':['Josefin Sans','Noto Sans Mende Kikakui','Nunito','Nunito Sans','Poppins']
      }
    },
   
  },
  plugins: [],
}

