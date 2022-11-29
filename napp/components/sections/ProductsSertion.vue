<template>
  <section id="services-section" class="h-screen">
    <div class="container mx-auto px-4">
      
      
      <div class="flex justify-center items-center my-6">
        <p class="text-6xl text-center">
          Our Products
        </p>          
      </div>

      <div class="flex justify-center items-center my-6">
        <p class="text-6xl text-center my-32">
          ...
        </p>          
      </div>

      <div class="flex justify-center items-center my-6 gap-8">
        <nuxt-link :to="localePath({ name: 'catalog' })" class="text-xl bg-main-info px-20 py-2 text-white font-bold hover:bg-main-primary transition duration-500 ease-in-out">More</nuxt-link>
      </div>

    
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
      services: {
        type: Object,
        default: Object,
      },
    },
    data() {
      return {
        tradein: "Is your welding equipment outworn no longer meeting modern requirements?<br />Our technology centre can accept your outworn equipment in payment for new <br />or fully repaired machines! Exchanging your used equipment for new machines saves your money preserving efficiency and quality.",
        repair: "We are ready to completely repair used welding machines and improve their specifications",
        service: "We are ready to completely repair used welding machines <br /> and improve their specifications Welding machines require regular service – just like any other complex equipment.<br /> Our technology centre offers qualified maintenance service for any equipment produced by us or any other manufacturer."
      }
    },
  }
</script>