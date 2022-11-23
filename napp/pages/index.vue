<template>
  <div class="">
    <HeaderSection />
    <MainSliderSection />
    <FirstSection />
    <IndexAboutSection />
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
  }
}
</script>
