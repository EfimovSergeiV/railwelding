<template>
  <section id="catalog-section" class="py-10">
    <div class="container mx-auto px-4">
      
      
      <div class="flex justify-center items-center">
        <p class="text-6xl text-center">
          Our Products
        </p>          
      </div>

        <div class="grid grid-cols-2 gap-4 my-10">
          <div class="p-2" v-for="product in products" :key="product.id">

            <div class="flex items-center gap-4 h-28">
              <div class="">
                <img :src="product.preview" class=" h-30" />
              </div>
              <div class="w-full">
                <div class="">
                  <p class="">{{ product.name }}</p>
                </div>

              </div>
              
            </div>
            <div class="flex items-end justify-end">
              <nuxt-link :to="localePath({name: 'catalog-category-id', params: { category: 'welding', id: product.id }})" class="pt-2 text-xl bg-main-info px-20 py-2 text-white font-bold hover:bg-main-primary transition duration-500 ease-in-out">{{ $t('more')}}</nuxt-link>
            </div>

          </div>

        </div>

      <!-- <div class="flex justify-center items-center my-6 gap-8">
        <nuxt-link :to="localePath({ name: 'catalog' })" class="text-xl bg-main-info px-20 py-2 text-white font-bold hover:bg-main-primary transition duration-500 ease-in-out">More</nuxt-link>
      </div> -->
      <!-- {{ products }} -->
    
    </div>
  </section>
</template>

<script>
// import HeaderSection from '@/components/sections/HeaderSection.vue'

  export default {
    name: 'ServicesSection',
    components: {
      // HeaderSection,
    },
    props: {
      products: {
        type: Array,
        default: Array,
      },
    },
    data() {
      return {
        tradein: "Is your welding equipment outworn no longer meeting modern requirements?<br />Our technology centre can accept your outworn equipment in payment for new <br />or fully repaired machines! Exchanging your used equipment for new machines saves your money preserving efficiency and quality.",
        repair: "We are ready to completely repair used welding machines and improve their specifications",
        service: "We are ready to completely repair used welding machines <br /> and improve their specifications Welding machines require regular service – just like any other complex equipment.<br /> Our technology centre offers qualified maintenance service for any equipment produced by us or any other manufacturer.",
      }
    },
  }
</script>