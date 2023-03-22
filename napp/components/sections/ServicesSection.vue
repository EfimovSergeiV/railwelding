<template>
  <div class="mx-auto lg:max-w-7xl">

    <div class="px-8 bg-white">

      <!-- <div class="flex justify-center items-center">
        <p class="mb-4 text-xl font-semibold text-slate-800 uppercase">Услуги</p>
      </div> -->

      <!-- <p class="text-xs">{{ services }}</p> -->

      <div class="grid grid-cols-1">

        <div v-for="service, item in services" :key="service.id" class="break-inside-avoid-column">
          
          <div v-if="item % 2 == 0" class="my-8">
            <div class="grid grid-cols-2 ggap-4">
              <div class="grid grid-cols-1 ">
                <div class="flex items-center h-full">
                  <div class=" -mr-32 py-2 px-4 bg-white/60 backdrop-blur-sm border border-white/40 rounded-md shadow-md shadow-main-secondary">
                    <div class="my-1">
                      <p class="font-semibold text-lg text-slate-800">{{ service.name }}</p>
                    </div>
                    <!-- eslint-disable vue/no-v-html -->
                      <p class="text-slate-800 text-sm" v-html="service.text"></p>
                    <!--eslint-enable-->
                  </div>                    
                </div>
              </div>
              <div>
                <div class="flex items-center h-full">
                  <img :src="service.img" />
                </div>
              </div>
            </div>
          </div>

          <div v-else class="my-8">
            <div class="grid grid-cols-2 gap-4">
              
              <div class="flex items-center h-full">
                <img :src="service.img" />
              </div>

              <div class="grid grid-cols-1 ">
                <div class="flex items-center h-full">

                  <div class="-ml-32 py-2 px-4 bg-white/60 backdrop-blur-sm border border-white/40 rounded-md shadow-md shadow-main-secondary">
                    <div class="my-1">
                      <p class="font-semibold text-lg text-slate-800">{{ service.name }}</p>
                    </div>
                    <!-- eslint-disable vue/no-v-html -->
                      <p class="text-slate-800 text-sm" v-html="service.text"></p>
                    <!--eslint-enable-->                    
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
    name: 'ContactSection',
    components: {
      // HeaderSection,
    },
    props: {
      services: {
        type: Array,
        default: Array,
      },
    },
    data() {
      return {
        textOne: "Cервисное обслуживание и устранение неполадок на месте для всего ассортимента продуктов и оборудования Contrail Machinery. Наши специалисты готовы оперативно вмешаться, чтобы работы можно было возобновить как можно скорее.",
        textTwo: "Cпециализированное техническое обучение и консультации по электросварке рельсов. Наша команда состоит из опытных инженеров и квалифицированных рабочих, которые всегда готовы и рады поделиться своими знаниями с другими профессионалами в этой области.",
        textThird: "Мы предлагаем нашим клиентам высококачественные запасные части для широкого спектра железнодорожной строительной техники. Детали разрабатываются и изготавливаются по запросу с учетом особенностей каждой машины."
      }
    },
  }
  </script>