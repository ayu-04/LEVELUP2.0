<template>
  <NuxtLayout name="mentor-sidenav" :username="username" :profile="profile">
    <NuxtPage />
    <div class="title text-center gradient-text text-[30px] my-5">
      <h1>REQUESTS</h1>
    </div>
    <div
      class="mentee-list text-center container mx-auto px-10 rounded-lg shadow-[rgba(0,_0,_0,_0.25)_0px_25px_50px_-12px] bg-bg-secondary h-[90vh]">
      <div class="filter-box w-11/12 lg:w-10/12 mt-8">
        <div class="search">
          <v-text-field density="compact" bg-color="grey-darken-4" variant="solo" label="Search templates"
            append-inner-icon="mdi-magnify" single-line hide-details></v-text-field>
        
        </div>
      </div>
      <div class="list">
        <div v-for="(i, idx) in menteelist" :key="idx">
          <request  class="grid-item" :mentee="i.username" :username="this.username" :menteePfp="i.profile" />
        </div>
      </div>
    </div>
  </NuxtLayout>
</template>

<script>
import axios from 'axios';
import request from '../../../../components/request.vue';

export default {
  components: { request },
  data() {
    return {
      username: useRoute().params.username,
      profile: "",
      menteelist: [],
      list: [],
    }
  },
  methods:{
    get() {
      this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;

      const path = `http://localhost:5000/api/mentorshiprequest/mentor/${this.username}`;
      let axiosConfig = {
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                "Access-Control-Allow-Origin": "*",
                'Authoriaztion': this.token,
                
            }
          };
      axios.get(path,axiosConfig)
        .then((res) => {
          this.list = res.data.menteelist;
            for(let i of this.list){
              if (i.status=="pending"){
                this.menteelist.push(i);
                console.log(this.menteelist)
              }
            }
        })
        .catch((error) => {
          console.error(error);
        });
    },

  },



  mounted() {
    const profilePath = `http://localhost:5000/api/mentor/profile/${this.username}`
    axios.get(profilePath).then((res) => {
      this.profile = res.data.profile
    }).catch((error) => {
      console.log(error)
    })
    this.get();
  },

}
</script>

<style lang="scss">
// body{
//   padding: 25px;
// }
.mentee-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 15px;
}
</style>
