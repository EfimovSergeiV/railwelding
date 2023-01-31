<template>
  <footer class="mx-auto lg:max-w-7xl lg:px-8">
    <div class="py-8 px-8 select-none bg-white">

      
      <div class="flex items-center justify-center">
        <p class="text-gray-900 uppercase text-3xl font-bold">Компания Railwelding</p>
      </div>

      <div class="flex items-center justify-center px-10 py-6">
        <p class="text-gray-700 text-center">{{ about }}</p>
      </div>

      <div class="flex items-center justify-center px-10">
        <p class="text-gray-700 text-center">С нами вы можете быть уверены, что ваш процесс сварки рельсов будет проходить без задержек и неполадок!</p>
      </div>

      <div class="flex items-center justify-center py-10">
        <img src="logo.png" />
      </div>

    </div>
  </footer>
</template>

<script>
// import HeaderSection from '@/components/sections/HeaderSection.vue'

export default {
  name: 'AboutSection',
  components: {
    // HeaderSection,
  },
  data() {
    return {
      about: "Лидер в разработке и производстве рельсосварочного оборудования. Наши инновационные технологии и высокое качество материалов обеспечивают надёжность и долговечность нашего оборудования. Наша компания предлагает широкий ассортимент рельсосварочных машин, разработанных и изготовленных полностью внутри компании с учетом особенностей каждого проекта и потребностей каждого клиента. В нашем каталоге вы найдете оборудование, доступное в различных конфигурациях."
    }
  },
}
</script>