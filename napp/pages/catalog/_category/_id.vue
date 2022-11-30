<template>
  <div class="">
    <HeaderSection />
    <!-- <MainSliderSection /> -->
    <ProductSection :product="product" />
    <FooterSection />
  </div>
</template>
  
  <script>
  import HeaderSection from '~/components/sections/HeaderSection.vue';
  // import MainSliderSection from '~/components/sections/MainSliderSection.vue';
  import ProductSection from '~/components/sections/ProductSection.vue';
  import FooterSection from '~/components/sections/FooterSection.vue';
  
  export default {
    name: 'CatalogPage',
    components: {
      HeaderSection,
      // MainSliderSection,
      ProductSection,
      FooterSection,
    },
    async asyncData({ $axios }) {
      const product = await $axios.$get('c/product/')

      return { product }
    },
  }
  </script>