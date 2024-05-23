<template>
  <NuxtLayout name="mentor-sidenav" :username="username" :profile="profile">
    <NuxtPage />
    <div class="title text-center gradient-text text-[30px] my-5">
      <h1>MY MENTEES</h1>
    </div>
    <div
      class="mentee-list text-center container mx-auto px-10 rounded-lg shadow-[rgba(0,_0,_0,_0.25)_0px_25px_50px_-12px] bg-bg-secondary h-[90vh]">
      <div class="filter-box w-11/12 lg:w-10/12 mt-8">
        <div class="search">
          <v-text-field density="compact" bg-color="grey-darken-4" variant="solo" label="Search templates"
            append-inner-icon="mdi-magnify" single-line hide-details></v-text-field>  
        </div>
      </div>
      <v-progress-circular v-if="loading" :size="70" :width="7" color="purple" indeterminate></v-progress-circular>

      <div v-if="!mentee_list.length" class="mt-12 text-xl">
        <h1>NO MENTEES AVAILABLE</h1>
      </div>
      <div class="list grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-1 gap-y-32 mt-24 place-items-center">

        <cardMentee v-for="(i, idx) in mentee_list" :key="idx" class="grid-item" :name="i.username"
          :skills="i.skills" :weaknesses="i.weaknesses" :username="username" :profile="i.profile" :phno="i.phone_number">
        </cardMentee>

      </div>
    </div>
  </NuxtLayout>
</template>

<script>
import axios from 'axios';
import { CometChat } from '@cometchat-pro/chat';
import { CometChatConfig } from '~~/consts';

export default {
  data() {
    return {
      username: useRoute().params.username,
      profile: "",
      drawer: true,
      rail: true,
      "languages": ["Arabic", "English", "Hindi"],
      "skills": ["python", "java", "webdev"],
      "locations": ["Hyderabad", "Chennai", "Mumbai"],
      skill_list: [],
      language_list: [],
      location_list: [],
      mentee_list:[],
    }
  },
methods:{
  get() {
      console.log('in get')
      this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
      const path = `http://localhost:5000/api/dashboard/mentor/${this.username}`;
      console.log('got path')
      let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            "Access-Control-Allow-Origin": "*",
            "Authoriaztion": this.token,
        }
      };

      axios.get(path, axiosConfig)
        .then((res) => {
          this.mentee_list = res.data.mentee_list;
          console.log(this.mentee_list)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });

    },
    async initUserCometChat() {

      if (process.client) {
        //GET USER DETAILS
        let user = await this.getUserDetails()

        //INITIALISE NEW COMETCHAT USER OBJECT
        const cometChatUser = new CometChat.User(String(user.id))

        //SET NAME FOR THE COMETCHAT USER
        cometChatUser.setName(user.uname)

        // CREATING COMETCHAT USER
        CometChat.createUser(cometChatUser, CometChatConfig.AUTH_KEY).then(
          user => {
            console.log("user created", user)
            
            //LOGIN THE COMETCHAT USER
            CometChat.login(user.getUid(), CometChatConfig.AUTH_KEY).then(
              user => {

                console.log("user logged in")

              }, error => {

                console.log("failed to login user", error)

              }
            )
          }, error => {
            // IF THE USER ALREADY EXISTS
            if (error.code = 'ERR_UID_ALREADY_EXISTS') {

              // LOGIN THE USER
              CometChat.login(user.id, CometChatConfig.AUTH_KEY).then(
                user => {

                  console.log("existing user logged in")

                }, error => {

                  console.log("failed to login existing user", error)
                }
              )
            }
          }
        )

      }

    },

    async getUserDetails() {

      let mentor
      const path = `http://localhost:5000/api/id/${this.username}`;
      const pfpPath = `http://localhost:5000/api/mentor/profile/${this.username}`;

      await axios.get(path).then((res) => {

        mentor = {
          id: res.data.id,
          uname: res.data.username,
          role: res.data.role
        }

      })
        .catch((err) => console.log(err))

      await axios.get(pfpPath)
        .then((res) => {
          mentor['profile'] = res.data.profile
        })
        .catch((err) => console.log(err))

      return mentor
    },

  },

  mounted() {
    const profilePath = `http://localhost:5000/api/mentor/profile/${this.username}`
    axios.get(profilePath).then((res) => {
      this.profile = res.data.profile
    }).catch((error) => {
      console.log(error)
    })
    this.initUserCometChat()
    .then(()=>{this.get()})
    
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
