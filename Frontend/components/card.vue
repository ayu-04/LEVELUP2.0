<template>
    <div class="card w-60 rounded-lg  card-color p-4 text-center flex flex-col gap-y-4">
      <div class="img text-center px-2 w-full">
        <img class="rounded-full h-32 w-32 mx-auto"
          src="https://www.mashed.com/img/gallery/the-kid-from-the-popeyes-meme-is-all-grown-up-and-now-a-state-champ/l-intro-1638908850.jpg"
          alt="">
      </div>
      <div class="card-title mt-16">
        <h2 class="text-lg text-pink-dark font-bold">Lamavoooo</h2>
      </div>
      <v-divider></v-divider>
      <div class="card-info flex flex-col gap-y-2 pb-4">
        <span class="subheading">languages</span>
        <v-chip-group class="chipgrp" v-for="i in skills">
          <v-chip size="small">{{i}}</v-chip>
        </v-chip-group>
        <v-divider class="mx-4"></v-divider>
        <span class="subheading">skills</span>
        <v-chip-group class="chipgrp" v-for="i in skills">
          <v-chip size="small" >{{i}}</v-chip>
        </v-chip-group>
      </div>
      <button class="btn-pink w-[110px] border" :disabled="disable" @click="sendRequest">Send Mentorship Request</button>
    </div>
</template>

<script>
props: {
  username: String,
  name: String, 
  skills: Array, 
  levels_completed: Array,
  languages: Array,
}, 
</script>

<style scoped>
.card {
  position: relative;
  border: solid 1.5px var(--pink-dark)
}

button {
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translate(-50%, 50%);
}

.card-color {
  background-color: #212121;
}

.card-info {
  text-align: justify;
  color: var(--pink-med);
}

.img {
  position: absolute;
  top: -18%;
  transform: translate(-20px);
}

.chipgrp {
  display: flex;
  flex-wrap: wrap;
}
</style>