<template>
  <footer class="mx-auto lg:max-w-7xl ">
    <div class="py-8 px-8 bg-white">

      <div class="flex justify-between">
        <div class="flex items-center">
          <p class="text-3xl uppercase">Partners</p>
        </div>
        <div class="">
          <div class="grid grid-cols-4 gap-4  place-items-center">

            <div class="grid grid-cols-1 gap-4">
              <div class="flex items-center justify-center">
                <img src="partners/belrailswelding.png" class=" h-12"/>
              </div>
              <div class="flex items-center justify-center">
                <p class="text-center">Belarusian railways</p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-4">
              <div class="flex items-center justify-center">
                <img src="partners/kazakhrails.png" class=" h-12"/>
              </div>
              <div class="flex items-center justify-center">
                <p class="text-center">Kazakh Railways</p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-4">
              <div class="flex items-center justify-center">
                <img src="partners/latrails.png" class=" h-12"/>
              </div>
              <div class="flex items-center justify-center">
                <p class="text-center">Lithuanian Railways</p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-4">
              <div class="flex items-center justify-center">
                <img src="partners/uzbekrails.png" class=" h-12"/>
              </div>
              <div class="flex items-center justify-center">
                <p class="text-center">Ozbekiston temir yollari</p>     
              </div>
            </div>

          </div>
        </div>
      </div>

    </div>
  </footer>
</template>

<script>
// import HeaderSection from '@/components/sections/HeaderSection.vue'

export default {
  name: 'PartnerSection',
  components: {
    // HeaderSection,
  }
}
</script>