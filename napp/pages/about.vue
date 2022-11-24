<template>
  <div class="">

    <HeaderSection />
    <IndexAboutVue class="my-20" :about="about" />
    <FooterSectionVue />

  </div>
</template>

<script>
import HeaderSection from '@/components/sections/HeaderSection.vue'
import IndexAboutVue from '@/components/sections/IndexAbout.vue'
import FooterSectionVue from '@/components/sections/FooterSection.vue'

export default {
  name: 'AboutPage',
  components: {
    HeaderSection,
    IndexAboutVue,
    FooterSectionVue,
  },
  async asyncData({ $axios }) {
    const about = await $axios.$get('con/about/')

    return { about }
  },
}
</script>