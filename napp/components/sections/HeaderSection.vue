<template>
  <div class="">

    <div class="bg-slate-700">
      <div class="h-3 bg-main-primary" style="box-shadow: 0px 5px 5px #00000095;"></div>
      <div class="py-2 container mx-auto px-4">
        <div class="flex justify-between">
          <div class="">
            <!-- <p class="text-gray-300">{{ $t('welcome') }}</p> -->
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
    </div>

    
    <div class="container mx-auto px-4 my-10 relative">
      <div class="flex justify-between items-center">
        <div class="flex items-center">
          <nuxt-link :to="localePath({name: 'index'})">
            <img src="~/assets/css/images/railwelding-logo.png" width="220" />
          </nuxt-link>        
        </div>
        
        <div class="flex items-center gap-6">
          <!-- <div class=""><nuxt-link :to="localePath({ name: 'index' })" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('home') }}</nuxt-link></div>
          <div class=""><nuxt-link :to="localePath({ name: 'index' }) + '#catalog-section'" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('catalog') }}</nuxt-link></div>
          <div class=""><nuxt-link :to="localePath({ name: 'index' }) + '#services-section'" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('services') }}</nuxt-link></div>
          <div class=""><nuxt-link :to="localePath({ name: 'index' }) + '#about-section'" class="text-xl text-main-dark hover:text-main-info transition duration-500 ease-in-out">{{ $t('about_us') }}</nuxt-link></div>
          <div class=""><button class="text-xl bg-main-info px-3 py-2 text-white font-bold hover:bg-main-primary transition duration-500 ease-in-out">{{ $t('contact_us') }}</button></div> -->
        </div> 
      </div>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'HeaderSection',
    components: {

    },
    data() {
      return {
        locale: this.$i18n.locale,
        categories: [
          { id: 1, name: 'Стационарные рельсосварочные машины' },
          { id: 2, name: 'Мобильные рельсосварочные машины' },
          { id: 3, name: 'Мобильный рельсосварочный комплекс' },
          { id: 4, name: 'Мобильный рельсосварочный комплекс на комбинированном ходу' },
          { id: 5, name: 'Пресс для испытания сварных соединений' },
          { id: 6, name: 'Запасные части для рельсосварочного оборудования' },
        ]
      }
    },
    watch: {
      locale (lang) {
        this.$router.push(this.switchLocalePath(lang))
      }
    }
  }
</script>
