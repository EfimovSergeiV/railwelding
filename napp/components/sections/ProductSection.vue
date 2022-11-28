<template>
  <!-- eslint-disable vue/no-v-html -->
  <div class="container mx-auto">
    <div class="mx-4 my-4">

      <div class="">
        
        <div class="">

        </div>

      </div>


      <div class="">

        <!-- <div class="flex gap-2 items-center">
          
          <div class="">
            <div class="w-28">
              <img src="~/assets/css/images/weldmashine.png" />
            </div>
          </div>
          
          <div class="">
            <p class="">{{ product.name }}</p>
          </div>
        
        </div> -->

        <div class="flex gap-8">
          <div class="">
            <div class="w-[340px] h-full bg-main-primary">
              <div class="flex items-center px-2 h-full">
                <nuxt-link to="#" class="text-gray-300">Мобильный рельсосварочный комплекс на комбинированном ходу</nuxt-link>
              </div>
            </div>
          </div>

          <div class="w-full">
            <div class="flex justify-between items-center">
              <div class="">
                <div class="flex gap-2 items-center my-4">
              
                  <div class="">
                    <div class="w-28">
                      <img src="~/assets/css/images/weldmashine.png" />
                    </div>
                  </div>
                  
                  <div class="">
                    <p class="">{{ product.name }}</p>
                  </div>
                
                </div>  
              </div>
              <div class="">
                <button class="px-10 py-2.5 text-white bg-main-secondary shadow-sm transition duration-500 ease-in-out">ЗАКАЗАТЬ</button>
              </div>
            </div>
          </div>
          <!-- <div class="flex justify-between">
            <div class="w-full">
              <div class="">
                <div class="flex gap-2 items-center my-4">
              
                  <div class="">
                    <div class="w-28">
                      <img src="~/assets/css/images/weldmashine.png" />
                    </div>
                  </div>
                  
                  <div class="">
                    <p class="">{{ product.name }}</p>
                  </div>
                
                </div>                
              </div>


            </div>

              <div class="">

                <button class="">
                  Заказать
                </button>

              </div>


          </div> -->
        </div>



        <div class="flex gap-8">

          <div class="flex flex-col gap-8">

            <!-- <div class="bg-main-primary my-4">
              <div class="px-2 py-4">
                <nuxt-link to="#" class="text-gray-300">Мобильный рельсосварочный комплекс на комбинированном ходу</nuxt-link>
              </div>
            </div> -->

            <div class="">
              <hooper
                :center-mode="true"
                :wheel-control="false"
                :auto-play="false"
                :play-speed="7000"
                style="width: 340px; height: 260px;"
                class="main-hooper cursor-zoom-in"
              >
                <slide v-for="i in 4" :key="i" class="">
                  <img
                    src="~/assets/css/images/weldmashine.png"
                    style="width: 340px; height: 260px;"
                    class="rounded-sm w-80"
                    @error="src='error.png'"
                  />
                </slide>
                
                <hooper-navigation slot="hooper-addons"></hooper-navigation>
                <hooper-pagination slot="hooper-addons"></hooper-pagination>
              </hooper>              
            </div>

            <div class="">
              <iframe 
                width="340" 
                height="200" 
                src="https://www.youtube.com/embed/oVBdrK9Is_A" 
                title="YouTube video player" 
                frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
              </iframe>
            </div>              
          </div>

          <div class="">

            <!-- <div class="flex gap-2 items-center my-4">
          
              <div class="">
                <div class="w-28">
                  <img src="~/assets/css/images/weldmashine.png" />
                </div>
              </div>
              
              <div class="">
                <p class="">{{ product.name }}</p>
              </div>
            
            </div> -->



            <div class="mb-1 bg-main-primary">
              <div class="flex gap-4 px-2 py-3">
                <button class="text-gray-100 underline">{{ $t('description') }}</button>
                <button class="text-gray-300">{{ $t('feature') }}</button>                
              </div>
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

            <div class="my-6">
              <p class="text-xl">{{ $t('advantage') }}:</p>
              <div v-for="advantage in product.advantages_product" :key="advantage.id" class="my-1">
                <p class="mdi mdi-circle-multiple-outline text-lg"> {{ advantage.text }}</p>
              </div>
            </div>

          </div>

        </div>



      </div>
    </div>



  </div>
  <!--eslint-enable-->
</template>

<script>
import {
    Hooper,
    Slide,
    Navigation as HooperNavigation,
    Pagination as HooperPagination,
  } from 'hooper'

  export default {
    name: 'ProductSection',
    components: {
      Hooper,
      Slide,
      HooperNavigation,
      HooperPagination,
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
.prop-line {
  border-color: #ababab;
  border-bottom-width: 1px;
}
.property-collection {
  margin-top: 8px;
}
</style>