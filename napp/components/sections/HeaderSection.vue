<template>
  <div class="">
    <!-- <p>L18N {{ $t('language') }}</p>
    <nuxt-link :to="switchLocalePath('en')">English</nuxt-link>
    <nuxt-link :to="switchLocalePath('de')">Deutsch</nuxt-link>
    <nuxt-link :to="switchLocalePath('ru')">Русский</nuxt-link> -->



    <div class="bg-slate-700">
      <div class="h-3 bg-sky-600" style="box-shadow: 0px 5px 5px #00000095;"></div>
      <div class="py-2 container mx-auto">
        <div class="flex justify-between">
          <div class="">
            <p class="text-gray-300">{{ $t('welcome') }}</p>
          </div>
          <div class="">
            <select v-model="locale" class="" aria-label="">
              <option value="en" class="mdi mdi-translate-variant">English</option>
              <option value="de">Deutsch</option>
              <option value="ru">Русский</option>
            </select>            
          </div>
        </div>
      </div>
    </div>

    <div class="container mx-auto my-10">
      <div class="flex">
        <nuxt-link :to="localePath('index')">
          <img src="~/assets/css/images/railwelding-logo.png" width="220" />
        </nuxt-link>        
      </div>
    </div>

    <div class="flex justify-center items-center">

      <div class="mx-2"><nuxt-link :to="localePath('about')" class="text-sm text-gray-700 hover:text-gray-900">Mobile Flash-Butt Welding</nuxt-link></div>
      <div class="mx-2"><nuxt-link :to="localePath('about')" class="text-sm text-gray-700 hover:text-gray-900">Holland Automated Manganese Refurbishment</nuxt-link></div>
      <div class="mx-2"><nuxt-link :to="localePath('about')" class="text-sm text-gray-700 hover:text-gray-900">Thermite Welding</nuxt-link></div>
      <div class="mx-2"><nuxt-link :to="localePath('about')" class="text-sm text-gray-700 hover:text-gray-900">Track Measurement Technology</nuxt-link></div>
      <div class="mx-2"><nuxt-link :to="localePath('about')" class="text-sm text-gray-700 hover:text-gray-900">{{ $t('about_us') }}</nuxt-link></div>

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
            src="https://picsum.photos/1024/400/?image=48"
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
