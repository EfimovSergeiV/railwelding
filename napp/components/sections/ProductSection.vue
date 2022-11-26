<template>
  <!-- eslint-disable vue/no-v-html -->
  <div class="container mx-auto">
    <div class="mx-4 my-4">

      <div class="flex gap-2 items-center">
        
        <div class="">
          <div class="w-28">
            <img src="~/assets/css/images/weldmashine.png" />
          </div>
        </div>
        
        <div class="">
          <p class="">{{ product.name }}</p>
        </div>
      
      </div>

      <div class="flex gap-4 my-4">
        <button class="">{{ $t('description') }}</button>
        <button class="">{{ $t('feature') }}</button>
      </div>

      <!-- <div class="">
        <div class="">
          <p v-html="product.description"></p>
        </div>
      </div> -->

      <div class="">
        <div v-for="properties in product.properties_product" :key="properties.id">
          <div class="">
            <div :class="`${properties.styles} flex justify-between py-1`" style="">
              <div class=""><p class="">{{ properties.text }}</p></div>
              <div class=""><p class="">{{ properties.value }}</p></div>              
            </div>
          </div>
          
        </div>
      </div>

      <div class="my-4">
        <p>{{ $t('advantage') }}</p>
        <div v-for="advantage in product.advantages_product" :key="advantage.id" class="my-1">
          <p class="mdi mdi-card-plus-outline"> {{ advantage.text }}</p>
        </div>
      </div>
      
    </div>
  </div>
  <!--eslint-enable-->
</template>

<script>

  export default {
    name: 'ProductSection',
    components: {
      // HeaderSection,
    },
    props: {
      product: {
        type: Object,
        default: Object,
      },
    },
  }
</script>

<style scoped>
.border-sec {
  border-color: #ababab;
  border-bottom-width: 2px;
}
</style>