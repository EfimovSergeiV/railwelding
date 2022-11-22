<template>
  <footer class="bg-main-primary text-gray-300">
    <div class="container mx-auto">


      <div class="py-4 px-4">
        <div class="md:flex md:justify-between">
          <div class="mb-6 md:mb-0">
            <img src="~/assets/css/images/railwelding-white.png" width="200" />
          </div>
          <div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-3">
              <div>
                  <h2 class="mb-6 text-sm font-semibold uppercase text-white">Resources</h2>
                  <ul class="">
                      <li class="mb-4">
                          <a href="https://flowbite.com/" class="hover:underline">Flowbite</a>
                      </li>
                      <li>
                          <a href="https://tailwindcss.com/" class="hover:underline">Tailwind CSS</a>
                      </li>
                  </ul>
              </div>
              <div>
                  <h2 class="mb-6 text-sm font-semibold uppercase text-white">Follow us</h2>
                  <ul class="">
                      <li class="mb-4">
                          <a href="https://github.com/themesberg/flowbite" class="hover:underline ">Github</a>
                      </li>
                      <li>
                          <a href="https://discord.gg/4eeurUVvTy" class="hover:underline">Discord</a>
                      </li>
                  </ul>
              </div>
              <div>
                  <h2 class="mb-6 text-sm font-semibold uppercase text-white">Legal</h2>
                  <ul class="">
                      <li class="mb-4">
                          <a href="#" class="hover:underline">Privacy Policy</a>
                      </li>
                      <li>
                          <a href="#" class="hover:underline">Terms &amp; Conditions</a>
                      </li>
                  </ul>
              </div>
          </div>
        </div>
        <hr class="my-6 border-gray-200 sm:mx-auto lg:my-8" />
        <div class="sm:flex sm:items-center sm:justify-between">
            <span class="text-sm sm:text-center">© 2023 <a href="#" class="hover:underline">RAILWELDING</a>
            </span>
            <div class="flex mt-4 space-x-6 sm:justify-center sm:mt-0">
                <a href="#" class="">
                  <span class="sr-only">Facebook page</span>
                </a>
            </div>
        </div>
      </div>

    </div>
  </footer>
</template>

<script>
// import HeaderSection from '@/components/sections/HeaderSection.vue'

export default {
  name: 'IndexAboutSection',
  components: {
    // HeaderSection,
  }
}
</script>