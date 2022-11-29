<template>
  <section id="about-section" class="my-10 py-10">
    <div class="container mx-auto px-4">

      <div class="flex justify-center items-center my-8">
        <p class="text-6xl text-center">
          About US
        </p>          
      </div>

      <div class="flex justify-center items-center">
        <div class="w-9/12">
          <p class="text-4xl text-center" v-html="title"></p>
        </div>
      </div>

      <div class="flex justify-center items-center my-8">
        <div class="w-8/12">
          <p class="text-2xl text-center" v-html="text"></p>
        </div>
      </div>

      <div class="flex justify-center items-center">
        <div class="w-8/12">
          <p class="text-xl text-center">
            {{ latest }}
          </p>          
        </div>
      </div>

      <div class="flex justify-center items-center my-8 gap-32">
        <div class="" v-for="partner in  partners" :key="partner.id"><img :src="partner.logo" width="80" /></div>
      </div>

    </div>
  </section>
</template>

<script>
// import HeaderSection from '@/components/sections/HeaderSection.vue'

  export default {
    name: 'AboutSection',
    components: {
      // HeaderSection,
    },
    props: {
      about: {
        type: Object,
        default: Object,
      },
    },
    data() {
      return {
        title: 'Railwelding is a modern company <br /> that has been specializing in develop-ment and production <br /> of rail welding equipment since 2005.',
        text: 'We develop and manufacture mobile and stationary rail welding systems designed for welding rails during construction or repair of continuos hightspeed railways, tram lines, as well as subway lines',
        latest: 'Close cooperation with major companies in Europe and Asia, and a strict attitude to quality form the key to efficient activities of our company.',
        partners: [
          {id: 1, logo: 'https://www.weldingeu.com/static/assets/images/photos/belrailswelding.png'},
          {id: 2, logo: 'https://www.weldingeu.com/static/assets/images/photos/kazakhrails.png'},
          {id: 3, logo: 'https://www.weldingeu.com/static/assets/images/photos/uzbekrails.png'},
          {id: 4, logo: 'https://www.weldingeu.com/static/assets/images/photos/latrails.png'},
        ]
      }
    },
  }
</script>