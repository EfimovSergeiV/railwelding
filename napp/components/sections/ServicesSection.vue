<template>
  <!-- eslint-disable vue/no-v-html -->
  <section id="services-section" class="my-10 py-10 bg-main-primary text-gray-300">
    <div class="container mx-auto px-4">
      
      
      <div class="flex justify-center items-center">
        <p class="text-6xl text-center text-gray-100">
          Our Services
        </p>          
      </div>

      <div class="flex justify-center items-center my-6 gap-8">
        <div class="w-3/5">
          <p class="text-5xl text-right">TRADE IN</p>
          <div class="mt-4">
            <p class="text-xl text-right" v-html="tradein"></p>
          </div>          
        </div>
        <img src="~/assets/css/images/tradein.png" width="200" />
      </div>

      <div class="flex justify-center items-center my-12 gap-8">
        <img src="~/assets/css/images/repair.png" width="200" />
        <div class="">
          <p class="text-6xl text-center">REPAIR AND UPGRADE</p>
          <div class="">
            <p class="text-xl my-4">
              {{ repair }}
            </p>
          </div>          
        </div>
      </div>

      <div class="flex justify-center items-center my-6 gap-8">
        <div class="">
          <p class="text-5xl text-center">SERVICE MAINTENANCE</p>
          <div class="">
            <p class="text-xl text-center my-4" v-html="service"></p>
          </div>          
        </div>
        <img src="~/assets/css/images/service.png" width="200" />
      </div>

    </div>
  </section>
  <!--eslint-enable-->
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