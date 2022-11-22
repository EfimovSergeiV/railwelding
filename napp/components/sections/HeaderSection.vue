<template>
  <div class="">

    <div class="bg-slate-700">
      <div class="h-3 bg-main-light" style="box-shadow: 0px 5px 5px #00000095;"></div>
      <div class="py-2 container mx-auto px-4">
        <div class="flex justify-between">
          <div class="">
            <p class="text-gray-300">{{ $t('welcome') }}</p>
          </div>
          <div class="">
            <select v-model="locale" class="py-0.5 text-xs rounded" aria-label="">
              <option value="en">English</option>
              <option value="de">Deutsch</option>
              <option value="ru">Русский</option>
            </select>            
          </div>
        </div>
      </div>
    </div>




    
    <div class="container mx-auto px-4 my-10">
      
      <div class="flex">
        <nuxt-link :to="localePath('index')">
          <img src="~/assets/css/images/railwelding-logo.png" width="220" />
        </nuxt-link>        
      </div>
    </div>

    <div class="container mx-auto px-4r my-4">
      <div class="flex justify-center items-cente gap-4">

        <div class="mx-2"><nuxt-link :to="localePath({ name: 'catalog' })" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('catalog') }}</nuxt-link></div>
        <div class="mx-2"><nuxt-link :to="localePath({ name: 'services'})" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('services') }}</nuxt-link></div>
        <div class="mx-2"><nuxt-link :to="localePath({ name: 'about' })" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('about_us') }}</nuxt-link></div>

      </div>      
    </div>






    <div>
      <hooper
        :center-mode="true"
        :wheel-control="false"
        :auto-play="false"
        :play-speed="7000"
        style="height: 100%;"
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
      locale: this.$i18n.locale,
    }
  },
  watch: {
    locale (lang) {
      this.$router.push(this.switchLocalePath(lang))
    }
  }
}
</script>

<!-- 
<NuxtLink :to="localePath('index')">{{ $t('home') }}</NuxtLink>
<NuxtLink :to="localePath('/')">{{ $t('home') }}</NuxtLink>
<NuxtLink :to="localePath('index', 'en')">Homepage in English</NuxtLink>
<NuxtLink :to="localePath('/user/profile')">Route by path to: {{ $t('profile') }}</NuxtLink>
<NuxtLink :to="localePath('user-profile')">Route by name to: {{ $t('profile') }}</NuxtLink>
<NuxtLink :to="localePath({ name: 'category-slug', params: { slug: category.slug } })">
-->
