<template>
  <div class="card w-72 rounded-lg  card-color p-4 text-center flex flex-col gap-y-4">
    <div class="img text-center px-2 w-full">
      <img class="rounded-full h-32 w-32 mx-auto"
        :src="profile">
    </div>
    <div class="card-title mt-16">
      <h2 class="text-lg text-pink-dark font-bold">{{mentee}}</h2>
    </div>
    <div class="btn-grp">
    <button class="btn-green w-[110px] border"  @click="AcceptRequest">Accept</button>
    <button class="btn-pink w-[110px] border"  @click="RejectRequest">Reject</button>
  </div>
  </div>
</template>


<script>
import axios from 'axios';

export default{
  props: {
    username: String,
    mentee: String, 
    menteePfp:String,
  }, 
  data(){
    return{
      disable: false,
      profile: this.menteePfp,
      url: '',
      token:"",
    }
  },
  methods: {
    AcceptRequest(){
        this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;
        const path= `http://localhost:5000/api/mentorshiprequest/mentor/${this.username}`;
        const payload={
            menteename: this.mentee, 
            decision: "accepted"
        }
        let axiosConfig = {
          headers: {
              'Content-Type': 'application/json;charset=UTF-8',
              "Access-Control-Allow-Origin": "*",
              "Authoriaztion": this.token,
          }
        };
        axios.post(path, payload, axiosConfig)
        .then(()=>console.log("Accepted"))
        .catch((error)=>console.log(error));
        alert("You accepted the request")
        this.disable=true;
    },
    RejectRequest(){
        const path= `http://localhost:5000/api/mentorshiprequest/mentor/${this.username}`;
        const payload={
            menteename: this.mentee, 
            decision: "rejected"
        }
        let axiosConfig = {
          headers: {
              'Content-Type': 'application/json;charset=UTF-8',
              "Access-Control-Allow-Origin": "*",
          }
        };
        axios.post(path, payload, axiosConfig)
        .then(()=>console.log("Rejected"))
        .catch((error)=>console.log(error));
        alert("You rejected the request");
        this.disable=true;
    },

    beforeMount(){
    this.getImgUrl();
  }
}
}
</script>

<style scoped>
.card {
  position: relative;
  -webkit-box-shadow: 11px 18px 10px -3px rgb(60, 59, 59);
-moz-box-shadow: 11px 18px 10px -3px rgb(31, 30, 30);
box-shadow: 8px 10px 20px -2px rgb(0, 0, 0);
transition: transform linear 0.2s;
height: 200px;

  /* border: solid 1.5px var(--pink-dark); */
}
.card:hover{
  transform:scale(1.05);
}
.btn-grp {
  position: absolute;
  left: 50%;
  bottom: 0;
  transform: translate(-50%, 50%);
  display: flex;
  column-gap: 4px;
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


</style>