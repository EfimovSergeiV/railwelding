<template>
  <div class="container mx-auto px-4">

    <div class="my-4">

      <div class="flex justify-center items-center">
        <div class="text-center">
          <p class="select-none">{{ $t('lorem_ipsum') }}</p>
        </div>
      </div>

      <div class="flex justify-center items-center gap-4 my-4">
        <nuxt-link :to="localePath('about')">To About Page</nuxt-link>
        <button type="button" class="inline-block px-6 py-2.5 bg-main-primary text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-main-info hover:shadow-lg focus:bg-main-info focus:shadow-lg focus:outline-none focus:ring-0 active:bg-main-500 active:shadow-lg transition duration-500 ease-in-out">Contact US</button>
      </div>

    </div>

    <div class="flex gap-2 my-2">
      <button class="px-6 py-2.5 text-xs text-white bg-main-primary rounded shadow-sm transition duration-500 ease-in-out">Primary button</button>
      <button class="px-6 py-2.5 text-xs text-white bg-main-secondary rounded shadow-sm transition duration-500 ease-in-out">Secondary button</button>
      <button class="px-6 py-2.5 text-xs text-white bg-main-dark rounded shadow-sm transition duration-500 ease-in-out">Dark button</button>
      <button class="px-6 py-2.5 text-xs text-white bg-main-info rounded shadow-sm transition duration-500 ease-in-out">Info button</button>
      <button class="px-6 py-2.5 text-xs text-white bg-main-light rounded shadow-sm transition duration-500 ease-in-out">Light button</button>
    </div>

  </div>
</template>

<script>
// import HeaderSection from '@/components/sections/HeaderSection.vue'

export default {
  name: 'IndexAboutSection',
  components: {
    // HeaderSection,
  }
}
</script>