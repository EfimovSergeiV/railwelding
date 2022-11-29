<template>
  <div class="">
    <HeaderSection />
    <MainSliderSection />
    <ProductsSection />
    <ServicesSection />
    <AboutSection />
    <ContactDriver />
    <FooterSection />
  </div>

</template>

<script>
import HeaderSection from '@/components/sections/HeaderSection.vue'
import MainSliderSection from '~/components/sections/MainSliderSection.vue'
import ProductsSection from '@/components/sections/ProductsSertion.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
import ContactDriver from '@/components/ContactDriwer.vue'
import FooterSection from '@/components/sections/FooterSection.vue'

export default {
  name: 'IndexPage',
  components: {
    HeaderSection,
    MainSliderSection,
    ProductsSection,
    ServicesSection,
    AboutSection,
    ContactDriver,
    FooterSection,
  },
  async asyncData({ $axios }) {
    const about = await $axios.$get('con/about/')

    return { about }
  },
}
</script>
