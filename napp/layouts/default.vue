<template>

  <div class="bg-white">
    <!-- container mx-auto max-w-7xl px-4 lg:max-w-7xl  bg-gradient-to-r from-white to-gray-200 text-main-dark-->

    <transition name="fade" mode="out-in">
      <Nuxt id="page"/>
    </transition>

  </div>
     
  
</template>
    
<script>

  export default {
    // head: {
    //   title: "Nuxt.js with TailwindCSS",
    //   meta: [
    //       { charset: "utf-8" },
    //       { name: "viewport", content: "width=device-width, initial-scale=1" },
    //       {
    //           hid: "description",
    //           name: "description",
    //           content: "Nuxt.js with TailwindCSS example",
    //       },
    //   ],
    //   link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.png" }],
    // },
    components: {

    },
    data() {
      return {
        dataset: true,
      }
    },
  //   methods: {
  //     addTodo (e) {
  //       this.$store.commit('todos/add', e.target.value)
  //       e.target.value = ''
  //     },
  //     ...mapMutations({
  //       toggle: 'todos/toggle'
  //     })
  //   },
  //   computed: {
  //     ...mapState({
  //       cartModal: (state) => state.modules.cart.cartModal,
  //       shopModal: (state) => state.shopModal
  //     }),
  //   },
  };
</script>