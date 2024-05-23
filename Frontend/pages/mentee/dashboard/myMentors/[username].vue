<template>
  <NuxtLayout name="mentee-sidenav" :username="username" :profile="profile">
    <NuxtPage/>
    <div class="title text-center text-pink-dark text-[30px] my-5">
      <h1>My Mentors</h1>
    </div>
      <!-- <v-progress-circular
      v-if="loading"
      :size="70"
      :width="7"
      color="purple"
      indeterminate
    ></v-progress-circular> -->

      <div v-if="!new_mymentor_list.length" class="mt-12 text-xl">
        <h1>YOU DON'T HAVE ANY MENTORS</h1>
      </div>
      <div
        class="list grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-1 gap-y-32 mt-24 place-items-center">

        <cardMentor v-for="(i, idx) in new_mymentor_list" :key="idx" class="grid-item" :name="i.username"
          :skills="i.skills" :languages="i.languages" :username="username" :profile="i.profile" :phno=i.phno :calendly_link=i.calendly_link>
        </cardMentor>
      </div>
      </NuxtLayout>
</template>

<script>


import axios from 'axios';


export default {
 
  data(){
    return {
      username: useRoute().params.username,
      profile: "",
      drawer: true,
      rail: true,
      token: "",
      mymentor_list: [],
      new_mymentor_list: [],
      searchtxt: "",
      skill: "",
      language: "",
      loading: false,
    }

  },


  methods: {
    get() {
      this.loading = true;
      this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
      console.log('in get')
      const path = `http://localhost:5000/api/dashboard/mentee/${this.username}`;
      console.log('got path')
      let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            "Access-Control-Allow-Origin": "*",
            "Authoriaztion": this.token,
        }
      };
      axios.get(path,axiosConfig)
        .then((res) => {
          this.mentor_list = res.data.mentor_list;
          const path2 = `http://localhost:5000/api/mentorshiprequest/mentee/${this.username}`
          axios.get(path2,axiosConfig)
            .then((res)=>{
              this.mymentor_list=res.data.mentorlist;
              for (let i of this.mymentor_list){
                if (i.status=="accepted"){
                  for(let j of this.mentor_list){
                    if (j.username==i.username){
                      this.new_mymentor_list.push(j);
                    }
                  }
                }
              }
            })
            .catch((error)=>{
              console.log(error)
            });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      
    },
   
  },


  mounted() {
    const profilePath = `http://localhost:5000/api/mentee/profile/${this.username}`
    axios.get(profilePath).then((res) => {
      this.profile = res.data.profile
    }).catch((error) => {
      console.log(error)
    })

  },

  created() {
    this.get();
  },

}
</script>

<style scoped>
.btn-green:hover {
  background-color: rgb(245, 40, 40) !important;
  color: #fff !important;
}

:deep(.v-label) {
  color: var(--pink-dark);
}

.filter-box {
  padding: 20px;
  border-radius: 8px;
  background-color: rgb(19, 19, 19);

  z-index: 3;
}

::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: var(--background);
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: var(--pink-dark);
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: var(--pink-med);
}
</style>
