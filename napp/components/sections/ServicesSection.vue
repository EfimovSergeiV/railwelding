<template>
  <div class="mx-auto lg:max-w-7xl lg:px-8">

    <div class="select-none py-8 px-8 bg-white">

      <div class="flex justify-center items-center">
        <p class="mb-4 text-xl font-semibold text-slate-800 uppercase">Услуги</p>
      </div>

      <!-- <p class="text-xs">{{ services }}</p> -->

      <div class="gap-8 columns-1 xl:columns-2">

        <div v-for="service in services" :key="service.id" class="break-inside-avoid-column">
          <div class="mb-8">
            <div class="my-1">
              <p class="font-semibold text-lg text-slate-800">{{ service.name }}</p>
            </div>
          
            <p class="text-slate-800 text-sm" v-html="service.text"></p>
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