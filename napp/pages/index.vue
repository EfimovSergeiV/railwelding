<template>
  <div class="">
    <HeaderSection />
    
    <ServicesSection />
    <QuestSection />
    <AboutSection />


    <!-- <NavSection /> -->
    <!-- <MainSliderSection /> -->
    <!-- <ProductsSection :products="products" /> -->
    

    <PartnerSection />
    <FooterSection />
  </div>

</template>

<script>
import HeaderSection from '@/components/sections/HeaderSection.vue'
import QuestSection from '~/components/sections/QuestSection.vue'
// import NavSection from '~/components/sections/NavSection.vue'
// import MainSliderSection from '~/components/sections/MainSliderSection.vue'
// import ProductsSection from '@/components/sections/ProductsSertion.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
// import ContactDriver from '@/components/ContactDriwer.vue'
import PartnerSection from '~/components/sections/PartnerSection.vue'
import FooterSection from '@/components/sections/FooterSection.vue'

export default {
  scrollToTop: false,
  name: 'IndexPage',
  components: {
    HeaderSection,
    QuestSection,
    // NavSection,
    // MainSliderSection,
    // ProductsSection,
    ServicesSection,
    AboutSection,
    PartnerSection,
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
