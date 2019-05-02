import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Interest from './views/Interest.vue'
import Post from './views/Post.vue'
import Profile from './views/Profile.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/interest',
      name: 'interest',
      component: Interest
    },
    {
      path: '/post',
      name: 'post',
      component: Post
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/post/:id',
      name: 'post',
      component: Post
    },
   
  ]
})
