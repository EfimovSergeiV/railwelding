<template>
  <div class="mx-auto lg:max-w-7xl lg:px-8">

    <div class="select-none py-8 px-8 bg-white">

      <div class="grid grid-cols-3 gap-4">
        <div class="text-center">
          <p class="text-xl py-2 font-semibold">Обслуживание и устранение неполадок</p>
          <p class="text-sm">{{ textOne }}</p>
        </div>
        <div class="text-center">
          <p class="text-xl py-2 font-semibold">Обучение и техническая поддержка</p>
          <p>{{ textTwo }}</p>
        </div>
        <div class="text-center">
          <p class="text-xl py-2 font-semibold">Запасные части и комплектующие</p>
          <p>{{ textThird }}</p>
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
    data() {
      return {
        textOne: "Cервисное обслуживание и устранение неполадок на месте для всего ассортимента продуктов и оборудования Contrail Machinery. Наши специалисты готовы оперативно вмешаться, чтобы работы можно было возобновить как можно скорее.",
        textTwo: "Cпециализированное техническое обучение и консультации по электросварке рельсов. Наша команда состоит из опытных инженеров и квалифицированных рабочих, которые всегда готовы и рады поделиться своими знаниями с другими профессионалами в этой области.",
        textThird: "Мы предлагаем нашим клиентам высококачественные запасные части для широкого спектра железнодорожной строительной техники. Детали разрабатываются и изготавливаются по запросу с учетом особенностей каждой машины."
      }
    },
  }
  </script>