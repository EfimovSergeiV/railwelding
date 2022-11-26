<template>
  <div class="">
    <HeaderSection />

    <div class="my-20 container mx-auto">
      <div class="mx-4">
        <p>This catalog index page</p>
      </div>
    </div>
    
    <FooterSection />
  </div>
</template>

<script>
import HeaderSection from '~/components/sections/HeaderSection.vue';
import FooterSection from '~/components/sections/FooterSection.vue';

export default {
  name: 'CatalogPage',
  components: {
    HeaderSection,
    FooterSection,
  }
}
</script>