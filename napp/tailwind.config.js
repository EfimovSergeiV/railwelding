/** @type {import('tailwindcss').Config} */
// primary #002F52
module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        'main-primary': '#074866',
        'main-secondary': '#0F293E',
        'main-dark': '#001E35',
        'main-info': '#2A72A9',
        'main-light': '#4C80A9',
      },
      fontFamily: {
        'sans': ['Noto Sans', 'Open Sans', 'Proxima-Regular', ],
        'serif': ['Noto Sans', 'Open Sans', 'Proxima-Regular', ],
        'mono': ['Noto Sans', 'Open Sans', 'Proxima-Regular', ],
        'display': ['Noto Sans', 'Open Sans', 'Proxima-Regular', ],
        'body': ['Noto Sans', 'Open Sans', 'Proxima-Regular', ],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/container-queries'),
  ],
}
