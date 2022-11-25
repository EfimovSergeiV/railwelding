export default {
  // Global page headers: https://go.nuxtjs.dev/config-head

  head: {
    title: 'napp',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/main.css',
    '@assets/low-priorty.pcss',
    '@assets/high-priorty.pcss',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config.js',
    exposeConfig: true,
    config: {},
    injectPosition: 0,
    viewer: true,
    injectPosition: { 
      // 'low-priority' will have lower priority than Tailwind stylesheet, 
      // while 'high-priorty' will override it
      after: 'assets/low-priorty.pcss'
    }
  },

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    "~/plugins/i18n.js",
    '~/plugins/axios.js',
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/eslint
    '@nuxtjs/eslint-module',
    '@nuxt/postcss8',
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/i18n', 
  ],

  i18n: {
    nuxtI18nHead: true,
    strategy: 'prefix_except_default',
    // defaultLocale: "ru",    
    locales: [
      {
        code: 'de',
        ico: 'de-DE',
        file: 'de-DE.json'
      },
      {
        code: 'ru',
        ico: 'ru-RU',
        file: 'ru-RU.json'
      },
      {
        code: 'en',
        ico: 'en-US',
        file: 'en-US.json'
      },
    ],
    lazy: true,
    langDir: "lang/",
    // baseUrl: 'https://my-nuxt-app.com',
    // skipSettingLocaleOnNavigate: false,
    detectBrowserLanguage: {
      // alwaysRedirect: false,
      // fallbackLocale: '',
      // redirectOn: 'root',
      // useCookie: true,
      // cookieAge: 365,
      // cookieCrossOrigin: false,
      // cookieDomain: null,
      // cookieKey: 'i18n_redirected',
      // cookieSecure: false,
      useCookie: true,
      cookieKey: "i18n_redirected",
      alwaysRedirect: false,
      // fallbackLocale: "en",
      redirectOn: 'root',
    }
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: 'http://127.0.0.1:8000',
    // headers: {
    //   common: {
    //     'Accept-Language': 'de'
    //   },      
    // }
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en',
    },
  },

  loading: {
    color: 'blue',
    height: '1px',
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    postcss: {
      plugins: {
        tailwindcss: {},
        autoprefixer: {},
      },
    },
  },
}
