<template>
  <div class="">
    <nuxt-link :to="switchLocalePath('en')">English</nuxt-link>
    <nuxt-link :to="switchLocalePath('de')">Deutsch</nuxt-link>
    <nuxt-link :to="switchLocalePath('ru')">Русский</nuxt-link>
    <HeaderSection />
    <MainSliderSection />
    <FirstSection />
    <IndexAboutSection :about="about" />
    <ContactDriver />
    <FooterSection />
  </div>

</template>

<script>
import HeaderSection from '@/components/sections/HeaderSection.vue'
import MainSliderSection from '~/components/sections/MainSliderSection.vue'
import FirstSection from '@/components/sections/FirstSection.vue'
import IndexAboutSection from '@/components/sections/IndexAbout.vue'
import ContactDriver from '@/components/ContactDriwer.vue'
import FooterSection from '@/components/sections/FooterSection.vue'

export default {
  name: 'IndexPage',
  components: {
    HeaderSection,
    MainSliderSection,
    FirstSection,
    IndexAboutSection,
    ContactDriver,
    FooterSection,
  },
  async asyncData({ $axios }) {
    const about = await $axios.$get('con/about/')

    return { about }
  },
}
</script>
