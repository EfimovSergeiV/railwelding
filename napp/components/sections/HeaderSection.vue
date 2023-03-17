<template>


  <header class="mx-auto lg:max-w-7xl lg:px-8">





    <div class="h-0.5 bg-main-primary"></div>
    
      <div class="bg-[url('images/header-bg.jpg')] h-[380px] bg-no-repeat bg-left-bottom bg-cover">

        <div class="bg-main-primary/80 hover:bg-main-primary/90 transition-all duration-1000 h-full relative">

          <div class="absolute w-full h-full">



            <div class="">
              <div class="grid grid-cols-7">
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">Машины для сварки</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">Комплектующие</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">Испытательное оборудование</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">Рельсосварочный комплекс</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">Услуги</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">О компании</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-sm text-center text-white">Язык</p>
                </div>
              </div>
            </div>


            <div class="flex justify-between items-center px-8 h-full">
              <div class="">
                <p class="text-white text-4xl w-4/5 select-none">Разработка и производство <br> индивудуальных машин для сварки рельсов</p>
              </div>
              <div class="">
                <nuxt-link :to="localePath({name: 'index'})">
                  <img src="logo-white.png" class=" h-9" />
                </nuxt-link>
              </div>
            </div>

          </div>

        </div>
      </div>

    <div class="bg-main-primary">


      <div class="flex items-center justify-between px-8 py-8">
        <div class="flex gap-8">
          <p class="text-white">info@railwelding.com</p>
          
        </div>
        <div class="">
          <p class="text-white font-semibold text-2xl text-center">+49 451 45 84</p>
          <div class="px-8 mt-4 py-2 bg-gray-100">
            <p class="font-bold uppercase text-gray-700">Заказать звонок</p>
          </div>
          
        </div>
      </div>
    </div>

  </header>

    <!-- <div class="bg-slate-700">
      <div class="h-3 bg-main-primary" style="box-shadow: 0px 5px 5px #00000095;"></div>
      <div class="py-2 container mx-auto px-4">
        <div class="flex justify-between">
          <div class="">
            <p class="text-gray-300">{{ $t('welcome') }}</p>
          </div>
          <div class="">
            <select v-model="locale" class="py-0.5 text-xs rounded" aria-label="">
              <option value="en">English</option>
              <option value="de">Deutsch</option>
              <option value="ru">Русский</option>
            </select>            
          </div>
        </div>
      </div>
    </div> -->

    
    <!-- <div class="container mx-auto px-4 my-10 relative">
      <div class="flex justify-between items-center">
        <div class="flex items-center">
          <nuxt-link :to="localePath({name: 'index'})">
            <img src="~/assets/css/images/railwelding-logo.png" width="220" />
          </nuxt-link>        
        </div>
        
        <div class="flex items-center gap-6">
          <div class=""><nuxt-link :to="localePath({ name: 'index' })" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('home') }}</nuxt-link></div>
          <div class=""><nuxt-link :to="localePath({ name: 'index' }) + '#catalog-section'" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('catalog') }}</nuxt-link></div>
          <div class=""><nuxt-link :to="localePath({ name: 'index' }) + '#services-section'" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('services') }}</nuxt-link></div>
          <div class=""><nuxt-link :to="localePath({ name: 'index' }) + '#about-section'" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('about_us') }}</nuxt-link></div>
          <div class=""><button class="text-xl bg-main-info px-3 py-2 text-white font-bold hover:bg-main-primary transition duration-500 ease-in-out">{{ $t('contact_us') }}</button></div>
        </div> 
      </div>
    </div> -->

</template>

<script>
  export default {
    name: 'HeaderSection',
    components: {

    },
    data() {
      return {
        locale: this.$i18n.locale,
      }
    },
    watch: {
      locale (lang) {
        this.$router.push(this.switchLocalePath(lang))
      }
    }
  }
</script>
