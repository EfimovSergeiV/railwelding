<template>
  <div class="">
    <HeaderSection />
    <ProductSection :product="product" />
    <FooterSection />
  </div>
</template>
  
  <script>
  import HeaderSection from '~/components/sections/HeaderSection.vue';
  import ProductSection from '~/components/sections/ProductSection.vue';
  import FooterSection from '~/components/sections/FooterSection.vue';
  
  export default {
    name: 'CatalogPage',
    components: {
      HeaderSection,
      ProductSection,
      FooterSection,
    },
    async asyncData({ $axios, params }) {
      const product = await $axios.$get(`c/product/${params.id}`)

      return { product }
    },
  }
  </script>