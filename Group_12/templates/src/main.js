import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import {store} from './store'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import CKEditor from '@ckeditor/ckeditor5-vue';
import './registerServiceWorker'

Vue.component('font-awesome-icon', FontAwesomeIcon)

var VueTruncate = require('vue-truncate-filter')
var SocialSharing = require('vue-social-sharing');

Vue.use(VueTruncate)
Vue.use( CKEditor )
Vue.use(SocialSharing);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
