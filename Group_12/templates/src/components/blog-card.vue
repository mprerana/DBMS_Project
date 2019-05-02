<template>
    <v-layout row class="mb-5">
        <router-link tag="ul" :to="'/post/'+blog.id">
        <v-flex xs12 sm12 md12 lg12 class="mx-auto">
            <v-card flat hover>
                <v-layout row>
                    <v-flex xs12 sm12 lg4 md3>
                        <!-- <skeleton-box
                            v-if="!loaded"
                            width="250px"
                            height="100%"
                        /> -->
                        <v-img
                            :src="blog.cover_photo"
                            height="100%"
                        ></v-img>
                    </v-flex>


                    <v-flex xs12 sm12 lg7 md9>
                        <v-card-title primary-title>
                            <div class="">
                                <!-- <skeleton-box
                                    v-if="!loaded"
                                    width="380px"
                                    height="50px"
                                /> -->
                                <h3 class="display-1 font-weight-bold md-0">{{blog.heading | truncate(60) }}</h3>

                                <v-layout row>
                                    <span class="mr-2">{{blog.author | truncate(20)}}</span>
                                    <v-icon size="7px" class="mx-2">lens</v-icon>
                                    <span class="mx-2">{{blog.post_date}}</span>
                                    <v-icon size="7px" class="mx-2">lens</v-icon>
                                    <span class="mx-2">{{blog.readtime}} Min Read</span>
                                </v-layout>

                                <!-- <div v-if="!loaded">
                                    <skeleton-box />
                                    <skeleton-box />
                                    <skeleton-box />
                                    <skeleton-box />
                                </div> -->
                                
                                <div class="py-4 subheading">{{blog.content | truncate(270) }}</div>

                                <v-layout row align-items-start>

                                    <!-- <v-icon size="27px">visibility</v-icon>
                                    <span class="headline">533</span> -->

                                    <!-- <v-icon size="27px" class="ml-4">thumb_up</v-icon>
                                    <span class="headline">533</span> -->

                                    <!-- <v-icon size="25px" class="mr-4 icon">share</v-icon>
                                    <v-icon size="25px" class="mr-4 icon">bookmark_border</v-icon>
                                    <v-icon v-if="this.$route.path == '/profile'" size="25px" class="mr-4 icon">delete</v-icon> -->
                                    <v-icon v-if="this.$route.path == '/profile'" size="35px" class="icon py-2">delete</v-icon><br/>
                                </v-layout>

                            </div>
                        </v-card-title>
                    </v-flex>


                    <v-flex lg1 md1>
                        <v-icon class="py-2">
                            arrow_forward
                        </v-icon>
                    </v-flex>
                </v-layout>
            </v-card>
        </v-flex>
        </router-link>
    </v-layout>
</template>

<script>
// import SkeletonBox from './SkeletonBox.vue';

export default {
    name:'BlogCard',
    components:{
        // 'skeleton-box':SkeletonBox
    },
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

<style lang="css" scoped>
    .icon{
        transition: transform 0s;
    }
    .icon:hover{
        transform: scale(1.1);
        fill:blueviolet;
        color:blueviolet;
    }
    .blog-card{
        list-style-type: none;
    }
</style>