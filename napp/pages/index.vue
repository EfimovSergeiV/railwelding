<template>
  <div class="">

    <HeaderSection />
    <ServicesSection />
    <QuestSection />
    <AboutSection />
    <FooterSection />

  </div>

</template>

<script>
import HeaderSection from '@/components/sections/HeaderSection.vue'
import QuestSection from '~/components/sections/QuestSection.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
import FooterSection from '@/components/sections/FooterSection.vue'

export default {
  scrollToTop: false,
  name: 'IndexPage',
  components: {
    HeaderSection,
    QuestSection,
    ServicesSection,
    AboutSection,
    FooterSection,
  },
  async asyncData({ $axios }) {
    const products = await $axios.$get('c/products/')
    // const about = await $axios.$get('con/about/')
    const about = []

    return { products, about }
  },
  // created () {
  //   window.addEventListener('scroll', this.onScroll);
  // },
  // destroyed () {
  //   window.removeEventListener('scroll', this.onScroll);
  // },
}
</script>
