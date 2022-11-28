<template>
  <div class="">
    <HeaderSection />

    <div class="my-20 container mx-auto">
      <div class="mx-4">
        <p>This catalog index page</p>
        <div class="flex gap-8 my-10">
          <nuxt-link :to="localePath({name: 'catalog-category', params: { category: 'welding'}})" class="">to category page</nuxt-link>
          <nuxt-link :to="localePath({name: 'catalog-category-id', params: { category: 'welding', id: 10}})" class="">to product page</nuxt-link>
        </div>
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