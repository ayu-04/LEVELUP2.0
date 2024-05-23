<template>
    <div class="card w-60 rounded-lg  card-color p-4 text-center flex flex-col gap-y-4">
      <div class="img text-center px-2 w-full">
        <img class="rounded-full h-32 w-32 mx-auto"
          :src="profile"
          alt="">
      </div>
      <div class="card-title mt-16">
        <h2 class="text-lg text-pink-dark font-bold">{{name}}</h2>
      </div>
      <v-divider></v-divider>
      <div class="card-info flex flex-col gap-y-2 pb-4">
        <span class="subheading">weaknesses</span>
        <v-chip-group class="chipgrp">
          <v-chip v-for="w in weaknesses" size="small">{{ w }}</v-chip>
        </v-chip-group>
        <v-divider class="mx-4"></v-divider>
        <span class="subheading">skills</span>
        <v-chip-group class="chipgrp">
          <v-chip v-for="skill in skills" size="small">{{ skill }}</v-chip>
        </v-chip-group>
      </div>
      <v-divider></v-divider>
      
      <v-dialog
        transition="dialog-bottom-transition"
        width="auto"
      >
      <template v-slot:activator="{ props }">
    <button class="btn-pink w-[110px] border" @click="chat" v-bind="props" >CHAT</button>
    </template>
    <template v-slot:default="{ isActive }">
          <v-card>
            <v-toolbar
              color="primary"
              title="Chat"
            ></v-toolbar>
            <v-card-text>
              <!-- <CometChatUserListWithMessages /> -->
              <CometChatUserListWithMessages/>

            </v-card-text>
            <!-- <v-card-actions class="justify-end">
              <v-btn
                variant="text"
                @click="isActive.value = false"
              >Close</v-btn>
            </v-card-actions> -->
          </v-card>
        </template>
      </v-dialog>
    </div>
</template>

<script>
import axios from 'axios';
import {CometChatUserListWithMessages, CometChatConversationListWithMessages, CometChatUI} from '~~/cometchat-pro-vue-ui-kit/CometChatWorkspace/src';
export default{
  components: {
    CometChatUserListWithMessages,
    CometChatUI,
    CometChatConversationListWithMessages,
  },
 props: {
     username: String,
     name: String, 
     weaknesses: Array,
     skills: Array,  
     profile:String,
     phno: Number,
 },
 data(){
  return{
    token: "",
  }
 },
}
</script>

<style scoped>
.card {
  position: relative;
  -webkit-box-shadow: 11px 18px 10px -3px rgb(60, 59, 59);
-moz-box-shadow: 11px 18px 10px -3px rgb(31, 30, 30);
box-shadow: 8px 10px 20px -2px rgb(0, 0, 0);
transition: transform linear 0.2s;

  /* border: solid 1.5px var(--pink-dark); */
}
.card:hover{
  transform:scale(1.05);
}
button {
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translate(-50%, 50%);
}

.card-color {
  background-color: rgb(19, 19, 19);
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

:deep(.v-card-text){
  height: 800px !important;

}


</style>