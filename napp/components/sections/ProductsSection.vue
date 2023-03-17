<template>
    <div class="mx-auto lg:max-w-7xl lg:px-8">
      <div class="bg-white">


        <div class="flex gap-4 py-4">

          <div class="flex items-center justify-center px-4">
            <div class="">
              <div class="flex">
                <p class="border-b-2 border-gray-700 py-2 text-2xl font-semibold">
                  Компания RAILWELDING
                </p>                
              </div>

              
             <div class="py-2">
              <p class="text-lg">
                Мы лидеруем в производстве рельсосварочного оборудования. Наши иновации
                и подход обеспечивают надёжность выпускаемого оборудования. Мы предлогаем рельсосварочное
                машины и комплексные решения, разработанные с учётом особенностей проектов и потребностей заказчика.
                Берём на себя организацию доставки и предлогаем сервисное обслуживание.
              </p> 
            </div>             

            </div>
            
          </div>


          <div class="">
            <div class="">
              <iframe width="560" height="315" src="https://www.youtube.com/embed/1H-vSHVOxoU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
            </div>
          </div>

        </div>

        <div class="py-4">
          <div class="grid grid-cols-4 gap-4">

            <div class="relative">
              <div class="flex justify-center items-center">
                <img src="img/1.jpg" class="w-full" />
                <div class="absolute h-20 w-full bottom-0">
                  <div class="h-full bg-main-primary/80">
                    
                    <div class="flex items-center justify-center p-2 h-full">
                      <p class="text-white">Машины для сварки</p>
                    </div>
                    
                  </div>
                  
                </div>
              </div>
            </div>

            <div class="relative">
              <div class="flex justify-center items-center">
                <img src="img/2.jpg" class="w-full" />
                <div class="absolute h-20 w-full bottom-0">
                  <div class="h-full bg-main-primary/80">
                    
                    <div class="flex items-center justify-center p-2 h-full">
                      <p class="text-white">Комплектующие</p>
                    </div>
                    
                  </div>
                  
                </div>
              </div>
            </div>

            <div class="relative">
              <div class="flex justify-center items-center">
                <img src="img/3.jpg" class="w-full" />
                <div class="absolute h-20 w-full bottom-0">
                  <div class="h-full bg-main-primary/80">
                    
                    <div class="flex items-center justify-center p-2 h-full">
                      <p class="text-white">Испытательное оборудование</p>
                    </div>
                    
                  </div>
                  
                </div>
              </div>
            </div>

            <div class="relative">
              <div class="flex justify-center items-center">
                <img src="img/1.jpg" class="w-full" />
                <div class="absolute h-20 w-full bottom-0">
                  <div class="h-full bg-main-primary/80">
                    
                    <div class="flex items-center justify-center p-2 h-full">
                      <p class="text-white">Рельсосварочный комплекс</p>
                    </div>
                    
                  </div>
                  
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


