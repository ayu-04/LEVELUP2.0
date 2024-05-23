<template>
  <v-layout>
      <v-navigation-drawer
        expand-on-hover
        rail
        color="pink-accent-4"
      >
        <v-list>
          <v-list-item
          :prepend-avatar="profile"
          :title="username"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <NuxtLink :to="{name:`mentee-dashboard-Mentors-User-username`,params:{username:username}}"><v-list-item prepend-icon="mdi-account-group" title="Explore Mentors"></v-list-item></NuxtLink>
          <NuxtLink :to="{name:`mentee-dashboard-myMentors-username`, params:{username:username}}"><v-list-item prepend-icon="mdi-account-group" title="My Mentors" ></v-list-item></NuxtLink>
          <v-list-item prepend-icon="mdi-account-plus" title="About Me" ></v-list-item>
          <v-list-item prepend-icon="mdi-badge-account-alert" title="Mentorship requests" ></v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main>
        <slot></slot>
      </v-main>
    </v-layout>
</template>

<script>

export default({
  props:{
    username: String,
    profile: String,
  },
  data(){
    return{
     
    }
  },

  
})
</script>
<style scoped>


</style>