export function findLocaleConfig (i18n, locale) {
  return (
    i18n.locales.find(({ iso, code }) => [iso, code].includes(locale)) || {}
  );
}

export default function ({ app, $axios }) {
  app.store.commit("localeChange", findLocaleConfig(app.i18n, app.i18n.locale));

  app.i18n.onLanguageSwitched = (oldLocale, newLocale) => {

    console.log('Change locale', newLocale)
    // axios.defaults.headers.common['Accept-Language'] = newLocale
    // $axios.headers.common['Accept-Language'] = 'Hallo welt'
      


    app.store.commit("localeChange", findLocaleConfig(app.i18n, newLocale));
  };
}

// export default ({ $axios, env }) => {
//   $axios.onRequest(config => {
//     config.headers.common['Authorization'] = `Bearer ${env.WP_API_KEY}`;
//   });
// }