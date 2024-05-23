<template>
    <NuxtLayout :name="layout" :username="username" :profile="profile">
     <NuxtPage/>
      {{ params }}
    </NuxtLayout>
</template>

<script setup>
 const layout = "mentor-sidenav"
 const params = useRoute().params.age;
</script>

<script>
import axios from 'axios';
export default defineComponent({

  data(){
    return{
      username: useRoute().params.username,
      drawer: true,
      rail: true,
      token: "",
      data:"",
      profile:"",
    }
  },

  created() {
    this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
    const path = `http://localhost:5000/api/dashboard/mentor/${this.username}`;
    console.log(this.token);

    axios.get(path, {
      headers: {
        'Authoriaztion': this.token,
      }
    }).then((res) => {

      console.log(res.data);
      this.profile = res.data.profile

    }).catch((error) => {

      if (error.response.status == '401') {

        alert(error.response.data.message)
      }
      if (error.response.status == '404') {

        this.isLists = error.response.data.isLists
        this.data = error.response.data.profile
      }
    })
  }

})
</script>

