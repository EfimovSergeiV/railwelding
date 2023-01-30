<template>
  <div class="mx-auto px-4 lg:max-w-7xl lg:px-8">
    
    <!-- <div class="bg-[url('images/header-bg.jpg')] h-[480px] bg-no-repeat bg-left-bottom bg-cover">

      <div class="bg-main-primary/70 hover:bg-main-primary/80 transition-all duration-1000 h-full relative">

        <div class="absolute w-full h-full">

          <div class="flex justify-between items-center px-8 py-4">
            <div class=""><p class="text-white font-semibold">English</p></div>
            <div class="flex items-center gap-4">
              <a href="mailto:info@railwelding.com" class="text-white font-semibold mdi mdi-email-outline"> info@railwelding.com</a>
              <a href="tel:+494514584" class="text-white font-semibold mdi mdi-phone"> +49 451 45 84</a>
            </div>
          </div>

          <div class="flex justify-between items-center px-8 pb-16 h-full">
            <div class="">
              <p class="text-white text-3xl font-bold">Разработка и производство <br> индивудуальных машин для сварки рельсов</p>
            </div>
            <div class="">
              <nuxt-link :to="{ name: 'index'}">
                <img src="logo-white.png" class="" />
              </nuxt-link>
            </div>
          </div>

        </div>



      </div>

    </div> -->

  </div>

<!-- <div class="z-10">
    <hooper
      :center-mode="true"
      :wheel-control="false"
      :auto-play="false"
      :play-speed="7000"
      style="width: 100%; height: 460px;"
      class="main-hooper z-10"
    >
      <slide v-for="i in 10" :key="i" class="">
        <img
          src="https://www.hollandco.com/images/MOW/Slider/LaserWelder.jpg"
          style="width: 100%;"
          class="rounded-sm z-10"
          @error="src='error.png'"
        />
      </slide>
      
      <hooper-navigation slot="hooper-addons"></hooper-navigation>
      <hooper-pagination slot="hooper-addons"></hooper-pagination>
    </hooper>
  </div> -->
</template>

<script>
  // import {
  //     Hooper,
  //     Slide,
  //     Navigation as HooperNavigation,
  //     Pagination as HooperPagination,
  //   } from 'hooper'

  export default {
    name: 'HeaderSection',
    components: {
      // Hooper,
      // Slide,
      // HooperNavigation,
      // HooperPagination,
    },
    data() {
      return {
        data: 'data',
      }
    },
  }
</script>