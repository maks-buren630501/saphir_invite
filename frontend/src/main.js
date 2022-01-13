import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000'
});

Vue.use(VueAxios, instance)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
