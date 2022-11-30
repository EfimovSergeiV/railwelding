<template>
  <div class="container mx-auto px-4 my-10 relative">
    <div class="flex justify-between items-center">
      <div class="flex items-center">
        <nuxt-link :to="localePath({name: 'index'})">
          <img src="~/assets/css/images/railwelding-logo.png" width="220" />
        </nuxt-link>        
      </div>
      
      <div class="flex items-center gap-6">
        <div class=""><nuxt-link :to="localePath({ name: 'index' })" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('home') }}</nuxt-link></div>
        <div class=""><button @click="changeRoute('catalog-section')" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('catalog') }}</button></div>
        <div class=""><button @click="changeRoute('services-section')" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('services') }}</button></div>
        <div class=""><button @click="changeRoute('about-section')" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('about_us') }}</button></div>
        <div class=""><button @click="changeRoute('catalog-section')" class="text-xl bg-main-info px-3 py-2 text-white font-bold hover:bg-main-primary transition duration-500 ease-in-out">{{ $t('contact_us') }}</button></div>
      </div> 
    </div>
  </div>
</template>

<script>
  export default {
    name: 'NavSection',
    components: {

    },
    data() {
      return {
      }
    },
    methods: {
      changeRoute(route) {
        document
          .getElementById(route)
          .scrollIntoView({ behavior: 'smooth' })
      },
    }
  }
</script>
