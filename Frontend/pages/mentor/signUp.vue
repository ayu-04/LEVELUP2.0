<template>
   
   <NuxtLayout>
    <NuxtPage />
   </NuxtLayout>

  <div class="sign-up md:mt-28 text-center flex flex-col gap-y-6 md:gap-y-11">
    <h1 class="text-3xl  mentor-sign-up text-green-dark">MENTOR SIGN UP</h1>
    <form>
      <div class=" signup-form container  mx-auto border-solid border-[0.4px] border-green-dark p-[2em] rounded-lg md:grid md:grid-cols-2 md:gap-x-6  md:p-[0px] md:border-opacity-0 lg:border-none">
        <div class="rounded-lg md:bg-[#2F2F2F] md:border md:border-solid md:border-current md:p-[2em] md:shadow-[rgba(0,_0,_0,_0.25)_0px_25px_50px_-12px]">
          <div class="input w-full ">
            <v-text-field class="text-text-primary placeholder-green-dark rounded-lg" type="email" v-model="emailid"
              label="email" variant="outlined"></v-text-field>
          </div>
          <div class="input grid grid-cols-2 gap-x-4">

            <v-text-field class="text-text-primary placeholder-green-dark rounded-lg" v-model="username" label="username"
              color="green-light" variant="outlined"></v-text-field>

            <v-text-field v-model="password" class="text-text-primary placeholder-green-dark rounded-lg"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'" :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'" name="input-10-1" label="Password" hint="At least 8 characters"
              counter @click:append="show1 = !show1" variant="outlined"></v-text-field>

          </div>
          <div class="input w-full ">
            <v-text-field class="text-text-primary placeholder-green-dark rounded-lg" type="tel" v-model="phno"
              label="phone number" variant="outlined"></v-text-field>
          </div>
          <div class="input grid grid-cols-2 gap-x-4">
            <v-text-field class="text-text-primary placeholder-green-dark rounded-lg" type="number" v-model="age"
              label="age" variant="outlined"></v-text-field>
            <v-combobox class="text-text-primary placeholder-green-dark " dense variant="outlined" v-model="location"
              :items="locations" label="your location"></v-combobox>
          </div>
          <div class="input w-full">
            <v-textarea class="text-text-primary placeholder-green-dark rounded-lg" label="Description"
                v-model="description" variant="outlined" clearable rows="1"></v-textarea>
          </div>
        </div>
        <div class="rounded-lg md:bg-bg-secondary md:border md:border-current md:p-[2em] md:shadow-[rgba(0,_0,_0,_0.25)_0px_25px_50px_-12px]">
          <div class="input w-full">
            <v-combobox class="text-text-primary placeholder-green-dark " v-model="language_list" :items="languages"
              label="your languages " multiple chips variant="outlined" transition="scale-transition"></v-combobox>
          </div>
          <div class="input grid grid-cols-2 gap-x-4">
            <v-text-field class="text-text-primary placeholder-green-dark rounded-lg" v-model="linkedin_link" type="url"
              label="linkedin link" variant="outlined"></v-text-field>
            <v-text-field class="text-text-primary placeholder-green-dark rounded-lg" v-model="calendly_link" type="url"
              label="calendly link" variant="outlined"></v-text-field>
          </div>
          <div class="input w-full ">
            <v-combobox class="text-text-primary placeholder-green-dark rounded-lg" v-model="skill_list" :items="skills"
              label="your skills " multiple chips variant="outlined"></v-combobox>

          </div>
          <div class="input w-full">
            
            <v-file-input class="text-text-primary placeholder-green-dark rounded-lg" :rules="imageRules" accept="image/png, image/jpeg, image/bmp" placeholder="Pick an avatar"
              prepend-icon="mdi-camera" variant ="outlined" label="Avatar" name="profile" @change="getImage"></v-file-input>
          </div>
          <div class="flex  justify-center gap-x-4 mt-2">
            <button class="text-text-primary  text-lg text-green-dark rounded-lg w-44 h-11 bg-zinc-800 hover:bg-green-dark hover:text-text-primary transition-all duration-500 px-2" @click.prevent="validate()">Sign-up</button>
            <button class="text-danger-red text-lg border-solid border-2 border-danger-red rounded-lg w-44 h-11 hover:bg-danger-red hover:text-text-primary  transition-all duration-500 px-2" @click.prevent="getEnv()">Clear</button>
            <h1>{{ config.public.bearerToken}}</h1>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>
<script setup>
const config = useRuntimeConfig()
</script>

<script>
import axios from "axios";

export default {
  data() {
    return {
      "skills": ['Python', 'DSA', 'Java', 'Web development', 'ML', 'C/C++'],
      "locations": ['Asia', 'Europe', 'Africa', 'Austrailia', 'South America', 'North America'],
      "languages": ['English', 'Hindi', 'French', 'Spanish', 'Arabic'],
      show1: false,
      username: '',
      password: '',
      emailid: '',
      age: null,
      location: '',
      phno: null,
      language_list: [],
      skill_list: [],
      linkedin_link: '',
      calendly_link: '',
      description: '',
      profileURL:'',

      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters',
        emailMatch: () => (`The email and password you entered don't match`),
      },
      imageRules: [value => {
        return !value || !value.length || value[0].size < 2000000 || 'Avatar size should be less than 2 MB!'
      },],
    }
  },

  methods: {

    validate() {
      const regexp = /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
      if (this.username == '') {
        alert("Please enter a username")
      }
      else if (!this.emailid.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)) {
        alert("Please enter a valid Email Id")
      }
      else if (this.password.length < 8) {
        alert("Please enter a password of 8 or more characters")
      }
      else if (!String(this.phno).match(/^\d{10}$/)) {
        alert("Please enter a valid phone number")
      }
      else if (this.age == null || this.age < 15) {
        alert("Your age should be greater than 14")
      }
      else if (this.location == '') {
        alert("Please select a location")
      }
      else if (this.language_list.length == 0) {
        alert("Please select a language")
      }
      else if (!regexp.test(this.linkedin_link)) {
        alert("Please enter a valid LinkedIn link")
      }
      else if (!regexp.test(this.calendly_link)) {
        alert("Please enter a valid Calendly link")
      }
      else if (this.skill_list.length == 0) {
        alert("Please select a skill")
      }
      else if (this.description == '') {
        alert("Please enter description")
      }
      else {
        this.post()
      }
    },
  
    getImage(e){
      const files = e.target.files
      if (!files.length) return

      const reader = new FileReader()
      reader.readAsDataURL(files[0])
      reader.onload = () => (this.profileURL = reader.result)
      console.log(this.profileURL);
    },
    getEnv(){
      console.log("hello")
    },
    post() {
      const path = 'http://localhost:5000/api/signup/mentor';
      const payload = {
        'username': this.username,
        'password': this.password,
        'emailid': this.emailid,
        'age': this.age,
        'location': this.location,
        'phno': this.phno,
        'languages': this.language_list,
        'skills': this.skill_list,
        'linkedin_link': this.linkedin_link,
        'calendly_link': this.calendly_link,
        'description': this.description,
        'profile': this.profileURL,
      }
      let axiosConfig = {
        headers: {
          'Content-Type': 'application/json;charset=UTF-8',
          "Access-Control-Allow-Origin": "*",
        }
      };
      axios.post(path, payload, axiosConfig)
        .then((data) => {
          let token = data.data.token;
          localStorage.setItem('token', token)
          
          console.log('posted')
          console.log(useRoute().params)
          this.$router.push({ path: '/mentor/dashboard/User-'+ this.username, params: { username: this.username } });
        })
        .catch((error) => {
          if (error.response.status == '404') {
            this.error = "User already exists. Please use a different username";
            alert(this.error);
          }
        });
    },
    clear(){
      this.$v.$reset() 
      this.username = '',
      this.password = '',
      this.emailid ='',
      this.age = null,
      this.location = '',
      this.phno = null,
      this.language_list = [],
      this.skill_list = [],
      this.linkedin_link = '',
      this.calendly_link = '',
      this.description = '';
      console.log("cleared");
    }
   
  }
}
</script>

<style scoped>



</style>