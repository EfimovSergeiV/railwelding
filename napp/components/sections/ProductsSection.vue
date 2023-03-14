<template>
    <div class="mx-auto lg:max-w-7xl lg:px-8">
      <div class="sselect-none bg-white">

        <div class="pt-8 flex justify-start items-center mx-8">
          <p class="text-xl uppercase font-semibold text-slate-800">Оборудование</p>
        </div>
  
        <div class="flex gap-4">

          <div class="grid grid-cols-1">

            <div class="mx-8 mb-8 w-[600px]">
              <div v-for="category in products" :key="category.id" class="my-4">
                
                <p class="text-lg font-semibold text-slate-800"> {{ category.name }}</p>
                <p v-if="category.description" class="text-sm my-2 text-slate-800"> {{ category.description }}</p>
                
                <div class="my-1">
                  <div v-for="product in category.products" :key="product.id" class="my-1">
                    <nuxt-link :to="localePath({name: 'catalog-category-id', params: { category: 'welding', id: 10}})" class="px-4 font-semibold text-slate-800"> {{ product.name }}</nuxt-link>
                  </div>                  
                </div>

              </div>
            </div>

          </div>
          <div class="w- [600px]">

            
          </div>

        </div>
  
      </div>
    </div>
  </template>
  
  <script>
  // import HeaderSection from '@/components/sections/HeaderSection.vue'
  
  export default {
    name: 'ProductsSection',
    components: {
      // HeaderSection,
    },
    props: {
      products: {
        type: Array,
        default: Array,
      },
    }
    // props: {
    //   products: {
    //     type: Array,
    //     default: [
    //       {"id": 1,"ct": "Оборудование", "inserted": [ { "id": 1, "cts": "Оборудование для стыковой сварки рельсов", "prods": [{"id": 1, "name": "Мобильная машина для стыковой сварки рельсов типа FBM-60"}, {"id": 2, "name": "Стационарная машина типа МСР-65.01 для стыковой сварки рельсов"}, {"id": 3, "name": "Мобильная машина для стыковой сварки рельсов типа FBM-140"}, {"id": 4, "name": "Стационарная машина типа МСО-120.01 для стыковой сварки рельсов"}] }, ]}
    //     ],
    //   },
    // },
  }
  </script>


