import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)


axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

export const store = new Vuex.Store({
  state: {
    authUser: {},
    isAuthenticated: false,
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: 'http://localhost:8000/auth/obtain_token/',
      refreshJWT: 'http://localhost:8000/auth/refresh_token/'
    },

    interests:[
        {name:'Technology'}, 
        {name:'Fitness'}, 
        {name:'Health'}, 
        {name:'Art'}, 
        {name:'Business'}, 
        {name:'Food'}, 
        {name:'Gaming'},
        ],

    tags: ['html', 'css', 'vue', 'laravel', 'react', 'angular'],

    blogData: null,

    featuredData:null,

    feed: 'yourfeed',

    profile:[
      {title:'Profile'},
      {title:'Posts'},
      {title:'Drafts'},
      {title:'Likes'},
      {title:'Bookmarks'},
      {title:'Followers'},
      {title:'Following'},
   ],

    topics: null,
    tab:null
  },


  getters:{

    getProfile: state => state.profile,

    getInterest: state => state.interests,

    getTags: state => state.tags,

    getTab: state => state.tab,

    getBlogData: state => state.blogData,

    getTopics: state => state.topics,

    getFeaturedData: state => state.featuredData
  },


  mutations: {
    updateTab(state, prop){
      state.tab = prop
    },
    updateFeaturedData(state, prop){
      state.featuredData = prop;
    },
    updateBlogData(state,prop){
      state.blogData = prop;
    },
    setAuthUser(state, {
      authUser,
      isAuthenticated
    }) {
      Vue.set(state, 'authUser', authUser)
      Vue.set(state, 'isAuthenticated', isAuthenticated)
    },
    updateToken(state, newToken) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.setItem('token', newToken);
      state.jwt = newToken;
    },
    removeToken(state) {
      // TODO: For security purposes, take localStorage out of the project.
      localStorage.removeItem('token');
      state.jwt = null;
    }
  },
  
  actions: {
  
    async queryTopic({commit}, prop ){

      var urlfeatured = 'https://newsapi.org/v2/everything?' +
          'q=' + prop + '&'+
          'from=2019-04-01&' +
          'sortBy=popularity&' +
          'apiKey=ed7767f07ae745dd9a229ca0b63d3a92';

      var reqfeatured = new Request(urlfeatured);
      var data = await fetch(reqfeatured)
                          .then(function(response) {
                          return response.json();
                      })
      commit('updateFeaturedData', data)
                      

      var url = 'http://localhost:8000/api/Blog/'+prop;
      var req = new Request(url)
      var dataBlog = await fetch(req)
                                    .then(function (response) {
                                      return response.json();
                                    });
      commit('updateBlogData',dataBlog)
      
      },

     
      
    }
})
