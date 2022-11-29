<template>
  <section id="services-section" class="my-10 py-10 bg-main-primary text-gray-300">
    <div class="container mx-auto px-4">
      
      
      <div class="flex justify-center items-center my-6">
        <p class="text-6xl text-center">
          Our Services
        </p>          
      </div>


      <div class="flex items-center my-6">
        <div class="">
          <p class="text-3xl text-center">TRADE IN</p>
          <div class="">
            <p>
              {{ tradein }}
            </p>
          </div>          
        </div>
        <div class=""><img src="~/assets/css/images/tradein.png" width="300" /></div>
      </div>

      <div class="flex items-center my-6">
        <div class=""><img src="~/assets/css/images/repair.png" width="300" /></div>
        <div class="">
          <p class="text-3xl text-center">REPAIR AND UPGRADE</p>
          <div class="">
            <p>
              {{ repair }}
            </p>
          </div>          
        </div>
      </div>

      <div class="flex items-center my-6">
        <div class="">
          <p class="text-3xl text-center">SERVICE MAINTENANCE</p>
          <div class="">
            <p>
              {{ service }}
            </p>
          </div>          
        </div>
        <div class=""><img src="~/assets/css/images/service.png" width="300" /></div>
      </div>

      <!-- <div class="flex justify-end items-center my-6">
        <p class="text-3xl text-center">
          REPAIR AND UPGRADE
        </p>          
      </div>

      <div class="flex items-center my-6">
        <p class="text-3xl text-center">
          SERVICE MAINTENANCE
        </p>          
      </div>
     -->
    
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
        tradein: "Is your welding equipment outworn no longer meeting modern requirements?Technosvar technology centre can accept your outworn equipment in payment for new or fully repaired machines! Exchanging your used equipment for new machines saves your money preserving efficiency and quality.",
        repair: "We are ready to completely repair used welding machines and improve their specifications",
        service: "We are ready to completely repair used welding machines and improve their specifications Welding machines require regular service – just like any other complex equipment. Our technology centre offers qualified maintenance service for any equipment produced by us or any other manufacturer."
      }
    },
  }
</script>