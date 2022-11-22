<template>
  <div class="">
    <HeaderSection />
    <FirstSection />
    <IndexAboutSection />
    <ContactDriver />
    <FooterSection />
  </div>

</template>

<script>
import HeaderSection from '@/components/sections/HeaderSection.vue'
import FirstSection from '@/components/sections/FirstSection.vue'
import IndexAboutSection from '@/components/sections/IndexAbout.vue'
import ContactDriver from '@/components/ContactDriwer.vue'
import FooterSection from '@/components/sections/FooterSection.vue'

export default {
  name: 'IndexPage',
  components: {
    HeaderSection,
    FirstSection,
    IndexAboutSection,
    ContactDriver,
    FooterSection,
  }
}
</script>
