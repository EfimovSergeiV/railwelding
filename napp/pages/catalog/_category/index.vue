<template>
  <div class="">
    <!-- <HeaderSection />
    <MainSliderSection /> -->

    <div class="my-20 container mx-auto">
      <div class="mx-4">

        


        <div class="flex justify-center items-center my-6">
          <p class="text-6xl text-center my-32">
            Products...
            
          </p>

        </div>
        <div class="flex justify-center items-center my-6">
          <nuxt-link :to="localePath({name: 'catalog-category-id', params: { category: 'welding', id: 10}})" class="">to product page</nuxt-link>   
        </div>



      </div>
    </div>


    
    <FooterSection />
  </div>
</template>

  
<script>
// import HeaderSection from '~/components/sections/HeaderSection.vue';
// import MainSliderSection from '~/components/sections/MainSliderSection.vue';
// import FooterSection from '~/components/sections/FooterSection.vue';
  
  export default {
    name: 'CatalogPage',
    components: {
      // HeaderSection,
      // MainSliderSection,
      // FooterSection,
    }
  }
</script>