<template>

<!-- Noto Sans", "Open Sans" -->

  <div class="">

    <div class=" bg-main-primary/90">
      <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">

        <div class="flex items-center h-20 justify-between">

          <div class="flex items-center gap-4"><span class="font-bold text-white text-[32px]">+150</span><p class="text-gray-100 text-sm">Сотрудников</p></div>
          <div class="flex items-center gap-4"><span class="font-bold text-white text-[32px]">+3500</span><p class="text-gray-100 text-sm">Реализованных проектов</p></div>
          <div class="flex items-center gap-4"><span class="font-bold text-white text-[32px]">+560 Га</span><p class="text-gray-100 text-sm">Площадь производства</p></div>
          <div class="flex items-center gap-4"><span class="font-bold text-white text-[32px]">+200</span><p class="text-gray-100 text-sm">Волнистых попугаев</p></div>

        </div>

      </div>
    </div>


    <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
      <div class="grid grid-cols-1 content-center bg-white min-h-screen">
        <div class="py-8">
          <div class="grid grid-cols-4 gap-4">
            <div v-for="i in 6" :key="i">
              <div class="border border-gray-700 rounded-md h-80 w-full shadow-md shadow-main-secondary">
              </div>
            </div>
            <div class="border border-gray-700 rounded-md h-80 w-full">
              <div class="flex items-center justify-center h-full">
                <p>Read more...</p>
              </div>
            </div>
          </div>
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


