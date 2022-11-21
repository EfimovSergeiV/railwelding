<template>
  <div class="">
    <p>L18N {{ $t('language') }}</p>
    <nuxt-link :to="switchLocalePath('en')">English</nuxt-link>
    <nuxt-link :to="switchLocalePath('de')">Deutsch</nuxt-link>
    <nuxt-link :to="switchLocalePath('ru')">Русский</nuxt-link>

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
            src="https://picsum.photos/1024/400/?image=41"
            style="width: 100%;"
            class="rounded-sm"
            onerror="https://picsum.photos/1024/400/?image=41"
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
