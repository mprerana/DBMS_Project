<template>
<div class="home">
  <SubNav/>
  <v-container>
    <!--  Second layout -->
    <v-layout row>
      <v-flex xs12 sm12 md12 lg8>
        <!-- {{getBlogData.articles}} -->
        <BlogCard v-for="blog in getBlogData" :key="blog.title" v-bind:blog="blog" v-bind:loaded="loaded" />
        <infinite-loading @infinite="infiniteHandler"></infinite-loading>
        <!-- <div v-for="blog in blogData.articles" :key="blog.title">
          {{blog.urlToImage}}
        </div> -->
       
      </v-flex>
      <v-flex xs12 sm12 md12 lg4 class="px-5 pb-5">
        <h2 v-if="getFeaturedData.articles != null" class="pb-3">Qucik Reads</h2>
        <FeaturedBlogCard v-for="blog in getFeaturedData.articles" :key="blog.title" v-bind:blog="blog" v-bind:loaded="loaded"/>
      
      <div class="mb-5">
        <h2 class="pb-3">Tags</h2>
        <v-chip color="primary" v-for="tag in getTags" :key="tag" text-color="white">{{tag}}</v-chip>
      </div>
        
      </v-flex>
    </v-layout> 
  </v-container>
</div>
</template>

<script>
  import FeaturedBlogCard from '../components/featured-blog-card'
  import BlogCard from '../components/blog-card'
  import SubNav from '../components/SubNav'
  import InfiniteLoading from 'vue-infinite-loading';
  import {mapGetters} from 'vuex'
  // import axios from 'axios'

  export default {
    name:'Home',
    
    components: {
     BlogCard,
     FeaturedBlogCard, 
     SubNav,
     InfiniteLoading,
    },
   
   data: ()=>({
      loaded: false
    }),

    computed:{
      ...mapGetters([
        'getTags',
        'getBlogData',
        'getFeaturedData'
      ])
    },


  async mounted(){
    var prop = this.$store.state.feed


    var urlFeatured = 'https://newsapi.org/v2/everything?' +
          'q=' + prop + '&'+
          'from=2019-04-01&' +
          'sortBy=popularity&' +
          'apiKey=ed7767f07ae745dd9a229ca0b63d3a92';

    var reqFeatured = new Request(urlFeatured);
    this.$store.state.featuredData = await fetch(reqFeatured)
                        .then(function(response) {
                        return response.json();
                    })
    
    var url = 'http://localhost:8000/api/Blog/'+prop;
    var req = new Request(url)
    this.$store.state.blogData = await fetch(req)
                                  .then(function (response) {
                                    return response.json();
                                  })
    this.loaded = true
                
                                

  },

    methods: {
    //   infiniteHandler($state) {
    //   axios.get(api, {
    //     params: {
    //       page: this.page,
    //     },
    //   }).then(({ data }) => {
    //     if (data.hits.length) {
    //       this.page += 1;
    //       this.list.push(...data.hits);
    //       $state.loaded();
    //     } else {
    //       $state.complete();
    //     }
    //   });
    // }
  },

    
  }
</script>

<style scoped> 
    .router-link-active{
        text-decoration: none;
    }
</style>
