<template>
          <v-layout>
          <v-flex xs12 sm12 md12 lg12 class="mb-5">
            <v-card flat hover>
              <v-img
                :src="blog.urlToImage"
                aspect-ratio="2.75"
              ></v-img>

              <v-card-title primary-title>
                <div>
                  <h3 class="subheading font-weight-bold mb-2 ">{{blog.title || truncate(10)}}</h3>
                  <div class="caption"> {{blog.description || truncate(15) }} </div>
                </div>
              </v-card-title>

              <v-card-actions>
               

              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
</template>

<script>
export default {
  name:'FeaturedBlogCard',
   props:{
        blog:{
            author:String,
            content:String,
            post_date:String,
            heading:String,
            cover_photo:String,
            readtime:Number
        },

    }
}
</script>
