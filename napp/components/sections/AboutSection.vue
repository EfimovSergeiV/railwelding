<template>
  <footer class="mx-auto lg:max-w-7xl ">
    <div class="py-8 px-8  bg-white">

      <!-- <div class="">


        <div class="flex justify-center py-4">
          <p class="text-slate-900 uppercase text-xl font-bold">География продаж</p>
        </div>

        <div class="flex justify-center">
          <img src="maps.png" />
        </div>
        
      </div> -->
      
      <div class="flex items-center justify-center">
        <p class="text-slate-900 uppercase text-xl font-bold">Компания Railwelding</p>
      </div>

      <div class="flex items-center justify-center px-10 py-2">
        <p class="text-slate-800 text-center">{{ about }}</p>
      </div>



      <div class="flex items-center justify-center py-4 px-10">
        <p class="text-slate-800 text-center">С нами вы можете быть уверены, что ваш процесс сварки рельсов будет проходить без задержек и неполадок!</p>
      </div>

      <div class="flex items-center justify-center py-10">
        <img src="logo.png" class=" h-8"/>
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