<template>

  <header class="h-screen min-h-screen bg-[url('images/header-bg.jpg')] bg-no-repeat bg-center">
    <div class="bg-gradient-to-br from-main-primary/70 via-main-secondary/30 to-main-primary/70 h-full">
      <div class=" h-full">

        <div class="grid grid-cols-1 content-between h-full">

          <div id="nav-container" class="fixed z-50 w-full">
            <div class="hidden md:block container mx-auto px-4 lg:max-w-7xl lg:px-8">

              <div class=""></div>

              <!-- <transition name="fade"> -->
                <div id="navbar" v-scroll="handleScroll" class="flex items-center justify-between gap-12 my-6 12 py-2 px-4 backdrop-blur-sm border border-white/40 rounded-md shadow-md shadow-main-secondary duration-700 transition-all">
                  <div class="py-1">
                    <nuxt-link :to="localePath({name: 'index'})">
                      <img src="logo.png" class=" h-6" />
                    </nuxt-link>                
                  </div>
                  <div class="flex gap-4 items-center px-4">
                    <div class="flex items-center justify-center py-1">
                      <p class="text-sm text-center text-main-primary font-semibold">{{ show }} Рельсосварочное оборудование</p>
                    </div>
                    <div class="flex items-center justify-center py-1">
                      <p class="text-sm text-center text-main-primary font-semibold">Испытательное оборудование</p>
                    </div>
                    <div class="flex items-center justify-center py-1">
                      <p class="text-sm text-center text-main-primary font-semibold">Услуги</p>
                    </div>
                    <div class="flex items-center justify-center py-1">
                      <p class="text-sm text-center text-main-primary font-semibold">О компании</p>
                    </div>
                    <div class="flex items-center justify-center py-1">
                      <p class="text-sm text-center text-main-primary font-semibold">Язык</p>
                    </div>                
                  </div>
                </div>
              <!-- </transition> -->

            </div>

          </div>


          <div></div>

          <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
            <div class="my-8">
              <!-- <nuxt-link :to="localePath({name: 'index'})">
                <img src="logo.png" class=" h-6" />
              </nuxt-link> -->
            </div>
            <p class="text-slate-200 font-black text-[36px]">Разработка и производство <br> индивудуальных машин для сварки рельсов</p>
          </div>

          <div class="bg-gradient-to-br from-main-primary/50 via-main-primary/40 to-main-secondary/60 backdrop-blur-sm border-t border-main-primary/40 py-8">
            <div class="container mx-auto px-4 lg:max-w-7xl lg:px-8">
              
              <div class="flex items-end justify-between">
                <div class="">
                  <p class="text-white font-black text-xl my-4">Почему выбирают нас ?</p>
                  <div class="grid grid-cols-3 gap-4 text-gray-100">
                    <div class=""><p class="text-sm mdi mdi-brightness-1"> Более 17 лет успешной работы</p></div>
                    <div class=""><p class="text-sm mdi mdi-brightness-1"> Собственное конструкторское бюро</p></div>
                    <div class=""><p class="text-sm mdi mdi-brightness-1"> Полный производственный цикл</p></div>
                    <div class=""><p class="text-sm mdi mdi-brightness-1"> Сервисное обслуживание и поддержка</p></div>
                    <div class=""><p class="text-sm mdi mdi-brightness-1"> Персональный менеджер</p></div>
                    <div class=""><p class="text-sm mdi mdi-brightness-1"> Решение нестандартных задач</p></div>
                  </div>                  
                </div>
                <div class="grid grid-cols-1 gap-2 text-right">
                  <div class="grid grid-cols-1 gap-1">
                    <p class="text-gray-100">info@railwelding.ru</p>
                    <p class="text-white font-semibold text-xl">+49 (123) 000 45 45</p>
                  </div>
                  <div class="">
                    <button class="bg-gradient-to-tr from-white via-gray-200 to-gray-200 font-semibold text-main-secondary px-12 py-2 rounded-md shadow-xl shadow-main-secondary mt-2">Заказать звонок</button>
                  </div>
                </div>
              </div>
            </div>            
          </div>
        </div>





      </div>
    </div>
  </header>

    <!-- <div class="h-0.5 bg-main-primary"></div>
    
      <div class="  hh-[500px] bg-no-repeat bg-left-bottom bg-cover">

        <div class="bg-gradient-to-br from-main-primary/80 via-main-secondary/40 to-main-primary/90 transition-all duration-1000 h-full relative">

          <div class="absolute w-full h-full">



            <div class="font-bold absolute w-full">
              <div class="flex items-center justify-center gap-12 py-8">
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">Машины для сварки</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">Комплектующие</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">Испытательное оборудование</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">Рельсосварочный комплекс</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">Услуги</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">О компании</p>
                </div>
                <div class="flex items-center justify-center py-1">
                  <p class="text-base text-center text-white">Язык</p>
                </div>
              </div>
            </div>


            <div class="flex justify-between items-center px-20 h-full">
              <div class="">
                <div class="my-4">
                  <nuxt-link :to="localePath({name: 'index'})">
                    <img src="logo-white.png" class=" h-9" />
                  </nuxt-link>
                </div>                
                <p class="text-slate-200 font-black text-[48px] w-5/5">Разработка и производство <br> индивудуальных машин для сварки рельсов development</p>
              </div>

            </div>



          </div>

        </div>
        
      </div> -->

    

    <!-- <div class="bg-main-primary bg-gradient-to-br from-[#002F52] via-[#003863] to-[#002F52]">


      <div class="flex items-center justify-between px-8 py-5">
        <div class="flex gap-8">
          <p class="text-white text-4xl">info@railwelding.com</p>
          
        </div>
        <div class="">
          <p class="text-white text-2xl text-center">+ 49 (451) 045 84 84</p>
          <div class="px-8 mt-3 py-2 bg-gray-100">
            <p class="font-semibold text-xl  text-gray-700">Заказать звонок</p>
          </div>
          
        </div>
      </div>
    </div> -->

  

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
        show: true,
      }
    },
    watch: {
      locale (lang) {
        this.$router.push(this.switchLocalePath(lang))
      }
    },
    beforeMount () {
      window.addEventListener('scroll', this.handleScroll)
    },
    beforeDestroy () {
      window.removeEventListener('scroll', this.handleScroll)
    },
    methods: {
      handleScroll () {
        const navMenu = document.getElementById('navbar')
        const navContainer = document.getElementById('nav-container')
        if (window.scrollY > 50) {
          navMenu.classList.add('bg-white/60')
          navContainer.classList.add('fixed')
          // this.show = true
        } else {
          // this.show = false
          navMenu.classList.remove('bg-white/60')
          navContainer.classList.remove('fixed')
        }
      }
    }
  }
</script>
