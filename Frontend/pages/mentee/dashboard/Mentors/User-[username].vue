<template>
  <NuxtLayout name="mentee-sidenav" :username="username" :profile="profile">
    <NuxtPage></NuxtPage>
    <div class="title text-center text-pink-dark text-[30px] my-5">
      <h1>Mentors</h1>
    </div>

    <div @scroll="changeBg"
      class="mentee-list text-center container mx-auto px-10 rounded-lg shadow-[rgba(0,_0,_0,_0.25)_0px_25px_50px_-12px] bg-bg-secondary h-[90vh] overflow-scroll overflow-x-auto">
      <div class="filter-box w-full lg:w-11/12 mt-8 shadow-[rgba(0,_0,_0,_0.25)_0px_25px_50px_-12px] mx-auto">
        <div class="search">
          <v-text-field density="compact" bg-color="grey-darken-4" variant="solo" label="Search Mentors"
            append-inner-icon="mdi-magnify" single-line hide-details color="black" v-model="searchtxt"
            @input="search"></v-text-field>
          <div class="filter d-flex flex-col md:flex-row justify-content-between gap-x-4 mt-[15px]">
            <div class="grid grid-cols-2 gap-x-3 col-span-2 grow">
              <v-combobox class="text-text-primary placeholder-green-dark" variant="solo" v-model="language"
                bg-color="grey-darken-4" chips :items="languages_options" label="language"></v-combobox>
              <v-combobox class="text-text-primary placeholder-green-dark" variant="solo" v-model="skill"
                bg-color="grey-darken-4" chips :items="skills_options" label="skill"></v-combobox>
            </div>
            <div class="d-flex justify-center gap-x-3">
              <button class="btn-pink bg-[#212121] h-[56px] w-14" @click="filter"><v-icon
                  icon="mdi-filter"></v-icon></button>
              <button class="btn-green text-red hover:bg-red hover:text-white bg-[#212121] h-[56px] w-14"
                @click="reset"><v-icon icon="mdi-cancel"></v-icon></button>
            </div>
          </div>
        </div>
      </div>

      <!-- leave this div -->
      <v-progress-circular v-if="loading" :size="70" :width="7" color="purple" indeterminate></v-progress-circular>

      <div v-if="!new_mentor_list.length" class="mt-12 text-xl">
        <h1>NO MENTORS AVAILABLE</h1>
      </div>
      <div
        class="list grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-1 gap-y-32 mt-24 place-items-center">

        <cardNotMentor v-for="(i, idx) in new_mentor_list" :key="idx" class="grid-item" :name="i.username"
          :skills="i.skills" :languages="i.languages" :username="username" :profile="i.profile">
        </cardNotMentor>

      </div>
      
    </div>
  </NuxtLayout>
</template>
<script>
import axios from 'axios';
import { CometChat } from '@cometchat-pro/chat';
import { CometChatConfig } from '../../../../consts';

export default {
  data() {
    return {
      username: useRoute().params.username,
      profile: "",
      drawer: true,
      rail: true,
      token: "",
      languages_options: [],
      skills_options: [],
      mentor_list: [],
      new_mentor_list: [],
      menteeDets: {},

      searchtxt: "",
      skill: "",
      language: "",

      loading: false,
    }



  },

  watch: {

  },

  methods: {
    reset() {
      this.skill = "";
      this.language = "";
      this.searchtxt = "";
      this.new_mentor_list = this.mentor_list;
    },

    get() {
      this.loading = true;
      this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
      const path = `http://localhost:5000/api/dashboard/mentee/${this.username}`;
      console.log('got path')

      axios.get(path, {
        headers: {
          'Authoriaztion': this.token,
        }
      }).then((res) => {
        this.mentor_list = res.data.mentor_list;
        this.new_mentor_list = res.data.mentor_list;

        this.mentor_list.forEach((mentor) => {
          mentor.languages.forEach((lang) => {
            if (lang != "undefined" && !this.languages_options.includes(lang))
              this.languages_options.push(lang)

            mentor.skills.forEach((skill) => {
              if (skill != "undefined" && !this.skills_options.includes(skill))
                this.skills_options.push(skill)
            })
          })
        })

      })
        .catch((error) => {
          console.error(error);
        });
      this.loading = false;
    },


    search() {

      this.new_mentor_list = this.mentor_list.filter((m) => m.username.toLowerCase().match(this.searchtxt.toLowerCase()))
    },

    filter() {

      if (this.language && this.skill) {
        this.new_mentor_list = this.mentor_list.filter((m) => {
          if (m.languages.includes(this.language) && m.skills.includes(this.skill)) {
            return true
          }
        })
      }

      else if (this.language) {
        this.new_mentor_list = this.mentor_list.filter((m) => {
          if (m.languages.includes(this.language))
            return true
        })
      }

      else if (this.skill) {
        this.new_mentor_list = this.mentor_list.filter((m) => {
          if (m.skills.includes(this.skill))
            return true
        })
      }


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

      let mentee
      const path = `http://localhost:5000/api/id/${this.username}`;
      const pfpPath = `http://localhost:5000/api/mentee/profile/${this.username}`;

      await axios.get(path).then((res) => {

        mentee = {
          id: res.data.id,
          uname: res.data.username,
          role: res.data.role
        }

      })
        .catch((err) => console.log(err))

      await axios.get(pfpPath)
        .then((res) => {
          mentee['profile'] = res.data.profile
        })
        .catch((err) => console.log(err))

      return mentee
    },




  },

  mounted() {
    console.log("in mounted")
    this.initUserCometChat()

  },

  created() {
    console.log("in created")
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