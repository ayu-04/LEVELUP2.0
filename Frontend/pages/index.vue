<template>
  <NuxtLayout>
    <NuxtPage/>
    <div class="main container mt-14 mx-auto grid justify-items-center gap-y-8 grow px-2 lg:w-8/12 lg:gap-y-10 lg:p-0 md:p-28">
    <div class="w-full grid justify-items-center gap-y-8 lg:inline-grid lg:grid-cols-2 lg:gap-4">
    <div class="img w-8/12 lg:order-last lg:w-11/12 mb-6">
      <img class="item-center" src="../assets/images/hero-img-cropped.svg" alt="hero-image">
    </div>
    <div class="header sm:text-center md:text-center leading-[0.9] grid gap-y-6 lg:gap-y-8 lg:flex flex-col lg:justify-center">
      <p class=" text-[11vw]  text-text-primary  lg:text-[6vw] lg:text-left lg:text-[5vw] ">
          <span>LEARNING</span><br/> FROM THE BEST
      </p>
      <div class="info-text lg:mx-0 md:mx-auto">
        <p class="text-text-secondary leading-[1.2] text-[1.5em]  lg:text-left lg:text-[1.3vw]">Learn from the best mentors from all over the world anywhere, anytime and anyplace</p>
      </div>
    </div>
  </div>
    <div class="buttons flex gap-x-8">
      <NuxtLink to="mentor/signUp"> <button class="btn-green">Start Teaching</button></NuxtLink>
      <NuxtLink to="mentee/signUp"> <button class="btn-pink">Start Learning</button></NuxtLink>
    </div>
    <div class="w-full inline-grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4">
      <div class="card-main">
        <h1 class="card-head"> One-To-One Chat</h1>
        <p class="text-text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid ab minima ducimus fugiat</p>
      </div>
      <div class="card-main">
        <h1 class="card-head"> Scheduled Meetings</h1>
        <p class="text-text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid ab minima ducimus fugiat</p>
      </div>
      <div class="card-main">
        <h1 class="card-head">Explore Through Mentors</h1>
        <p class="text-text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid ab minima ducimus fugiat</p>
      </div>
      <div class="card-main ">
        <h1 class="card-head">Clean Learning And Teaching Experience</h1>
        <p class="text-text-secondary">Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquid ab minima ducimus fugiat</p>
      </div>
    </div>
  </div>  
  <NuxtPage/>
  </NuxtLayout>
</template>