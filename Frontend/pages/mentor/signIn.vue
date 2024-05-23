<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
  <div class="sign-up mt-14 md:mt-28 text-center shrink-0 flex flex-col gap-y-6 md:gap-y-8">
    <h1 class="text-3xl text-green-dark">MENTOR SIGN IN</h1>
    <form>
      <div class=" signup-form d-flex justify-center bg-login-window bg-contain container mx-auto w-full p-[2em] rounded-lg h-[585px] md:bg-center md:w-[47%] md:gap-x-6">
        <div class="rounded-lg d-flex flex-col justify-center items-center grow gap-y-6 md:border-solid md:p-[2em] md:w-6/12 ">
          <div class="input w-7/12 ">
            <v-text-field class="text-green-dark-900 rounded-lg" type="text" v-model="username"
              label="username"></v-text-field>
          </div>
          <div class="input w-7/12 ">
            <v-text-field class="text-green-dark-900 rounded-lg" type="password" v-model="password"
              label="password"></v-text-field>
          </div>
          <div class="clas w-full">
            <button class="text-text-primary text-lg bg-green-dark rounded-lg w-44 h-11 hover:bg-pink-dark hover:text-text-primary  transition-all duration-500 px-2" @click.prevent="post()">Sign-In</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
<script>

import axios from "axios";

export default({
  data(){
    return{
      username: "",
      password:"",

    }
  },
  methods:{
    post(){
      const path = `http://localhost:5000/api/login`
      const creds = {
        'username': this.username,
        'password': this.password,
        'role': 'mentor',

      }
    console.log(creds);
   
    axios.post(path, creds)
    .then((data) => {
     let token = data.data.token;
     localStorage.setItem('token',token);
     this.$router.push({ path: '/mentor/dashboard/User-'+ this.username, params: { username: this.username,password:this.password } });
     console.log('logged in')
    })
    .catch((error,data) => {
      if(error.response.status == '401'){
        alert("incorrect password");
      }
      console.log(data.data)
    })

    }
  },
})
</script>

<style scoped>

.v-field__field{
  background-color:var(--green-med);
  border-radius: 8px;
}

</style>