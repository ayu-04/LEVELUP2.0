<template>
  <nav class=" m-[2em] gap-y-8 flex flex-col items-center  md:flex-row  md:justify-between md:w-11/12 md:mx-auto">
    <div class="brand  flex items-center md:block ml-9">
      <img src="../assets/images/Brand.svg" alt="brand" class="w-48 h-28">
      <!-- <button @click="open()" class=" rounded-lg text-pink-dark text-[2.5em] hover:bg-pink-dark hover:text-text-primary  transition-all duration-500 px-2 md:hidden"><font-awesome-icon :icon="['fas', 'bars']" class="icon alt"/></button> -->
    </div>
    <div class="menu flex gap-x-4 md:flex md:justify-around md:items-center md:mb-[1em] md:w-5/12  text-2xl text-text-secondary">
      <div class="menu-item">
        <NuxtLink to="/">
          <button class="h-14  rounded-lg hover:bg-green-dark hover:text-text-primary transition-all duration-500 px-2">
            <b>HOME</b>
          </button>
        </NuxtLink>
      </div>
      <div class="menu-item">
        <NuxtLink to="/about">
          <button class="h-14  rounded-lg hover:bg-green-dark hover:text-text-primary transition-all duration-500 px-2">
            <b>ABOUT</b>
          </button>
        </NuxtLink>
      </div>
      <div class="menu-item">
        <NuxtLink to="/contact">
          <button class="h-14 rounded-lg hover:bg-green-dark hover:text-text-primary transition-all duration-500 px-2">
            <b>CONTACT</b>
          </button>
        </NuxtLink>
      </div>
      <!-- <div class="menu-item text-pink-dark ">
        <button class="h-14 rounded-lg hover:bg-pink-dark hover:text-text-primary transition-all duration-500 px-2"><NuxtLink><b>SIGN-IN</b></NuxtLink></button>
      </div> -->
    </div>
  </nav>
  <div>
    <slot/>
  </div>
</template>

<script>
  export default{
    data(){
      return{

      }
    },

    methods:{
      open(){
        var nav = document.querySelector('.menu');
        nav.classList.toggle('hidden');
        
      }
    }
  }
</script>

<style>

</style>