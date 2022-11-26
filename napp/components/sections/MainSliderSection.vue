<template>
  <div>
    <hooper
      :center-mode="true"
      :wheel-control="false"
      :auto-play="false"
      :play-speed="7000"
      style="width: 100%; height: 360px;"
      class="main-hooper"
    >
      <slide v-for="i in 10" :key="i" class="">
        <img
          src="https://www.hollandco.com/images/MOW/Slider/LaserWelder.jpg"
          style="width: 100%;"
          class="rounded-sm"
          @error="src='error.png'"
        />
      </slide>
      
      <hooper-navigation slot="hooper-addons"></hooper-navigation>
      <hooper-pagination slot="hooper-addons"></hooper-pagination>
    </hooper>
  </div>
</template>

<script>
  import {
      Hooper,
      Slide,
      Navigation as HooperNavigation,
      Pagination as HooperPagination,
    } from 'hooper'

  export default {
    name: 'HeaderSection',
    components: {
      Hooper,
      Slide,
      HooperNavigation,
      HooperPagination,
    },
    data() {
      return {
        data: 'data',
      }
    },
  }
</script>