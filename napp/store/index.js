/* eslint-disable camelcase */
// export const state = () => ({
//     language: 'de'
// })

export const state = () => ({
    locale: { "code": "en", "ico": "en-US", "file": "en-US.json" },
    local: 'en'
  });
  
  export const mutations = {
    localeChange(state, locale) {
      console.log(locale)
      state.locale = locale.code
      state.local = locale.code
      // axios.defaults.headers.common['Accept-Language'] = locale.code

      // headers: {
      //   common: {
      //     'Accept-Language': 'de'
      //   },      
      // }
    },
  };