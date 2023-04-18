// this.$axios.setHeader('Accept-Language', this.$i18n.locale )

// export default function ({ app, $axios }) {
//   $axios.setHeader('Accept-Language', app.i18n.locale )
//   app.i18n.onLanguageSwitched = (oldLocale, newLocale) => {
//     $axios.setHeader('Accept-Language', newLocale )
//   }
// }

export function findLocaleConfig (i18n, locale) {
  return (
    i18n.locales.find(({ iso, code }) => [iso, code].includes(locale)) || {}
  );
}

export default function ({ app }) {
  app.store.commit("localeChange", findLocaleConfig(app.i18n, app.i18n.locale));
  
  app.i18n.onLanguageSwitched = (oldLocale, newLocale) => {
    app.store.commit("localeChange", findLocaleConfig(app.i18n, newLocale));
  };
}
