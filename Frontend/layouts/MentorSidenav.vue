<template>
  <v-layout>
    <v-navigation-drawer expand-on-hover rail color="green">
      <v-list>
        <v-list-item :prepend-avatar="profile" :title="username"></v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <NuxtLink :to="{ name: `mentor-dashboard-myMentees-User-username`, params: { username: username } }"><v-list-item
            prepend-icon="mdi-account-group" title="Mentors" value="mentors"></v-list-item></NuxtLink>
        <NuxtLink :to="{ name: `mentor-dashboard-requests-username`, params: {username: username}}"><v-list-item prepend-icon="mdi-account-plus" title="Mentorship Requests" value="requests"></v-list-item></NuxtLink>
        <v-list-item prepend-icon="mdi-badge-account-alert" title="Mentorship requests" value="mentorship"></v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <slot></slot>
    </v-main>
  </v-layout>
</template>

<script>

export default ({
  props: {
    username: String,
    profile: String,
  },
  data() {
    return {

    }
  }
})
</script>
<style scoped></style>