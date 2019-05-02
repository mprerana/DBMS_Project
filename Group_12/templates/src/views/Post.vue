<template>
    <v-container class="mt-5">
        <v-layout row class="mt-5">
            <v-flex xs12 sm12 md12 lg12>
                <v-img :src="blog.cover_photo"></v-img>
                <div class="px-5 py-4">
                    <h1 class="display-2 font-weight-bold" style="font-family: 'Montserrat', sans-serif!important;">{{blog.heading}}</h1><br/>
                    <v-layout row>
                        <!-- <v-flex md1 lg1>
                            <v-list-tile-avatar>
                                <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg">
                            </v-list-tile-avatar>
                        </v-flex>
                        <v-flex md11 lg11>
                            <span class="mr-2">John Doe</span>
                            <v-icon size="7px" class="mx-2 pb-1">lens</v-icon>
                            <span class="mx-2">24 Mar'2019</span>
                            <v-icon size="7px" class="mx-2 pb-1">lens</v-icon>
                            <span class="mx-2">7 Min Read</span>
                        </v-flex> -->
                        <v-list-tile-avatar>
                            <img src="https://cdn.vuetifyjs.com/images/lists/2.jpg">
                        </v-list-tile-avatar>
                        
                        <span class="mr-2 pt-1">{{blog.author}}</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">{{blog.post_date}}</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <span class="mx-2 pt-1">{{blog.readtime}} min read</span>
                        <v-icon size="7px" class="mx-2 pb-3 pt-1">lens</v-icon>
                        <v-btn small v-if="!isFollow" outline color="indigo" @click="follow">Follow</v-btn>
                        <v-btn small v-else color="indigo white--text" @click="unfollow">Following</v-btn>

                    </v-layout>


                    <!-- Icons for bookmark, share and like  -->

                    <v-layout row class="pt-5">
                        <v-flex lg1 class="fix">
                            <!-- Bookmark icon -->
                            <v-icon large class="icon py-2">bookmark_border</v-icon><br/> 

                            <!-- Like icons -->
                            <v-icon large v-if="!liked" class="icon py-2" @click="like">favorite_border</v-icon>
                            <v-icon large v-else class="icon py-2" @click="unlike">favorite</v-icon>
                            <v-flex>
                                <span class="pl-2 subheading blue--text">{{upvotes}}</span>
                            </v-flex>
                            <br/>
                            <!-- <v-icon large v-if="liked" class="icon" @click="unlike">favorite</v-icon><br/> -->

                            <!-- Icons for facebook - start -->
                            <social-sharing url="http://127.0.0.1:8080/post/340" 

                                title="blog.heading"
                                description="blog.content || truncate(50)"
                                inline-template>
                                    <div>
                                        <network network="facebook">
                                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"  
                                                width="35" height="35"
                                                viewBox="0 0 24 24"
                                                class="icon"
                                            >  
                                                <path d="M17.525,9H14V7c0-1.032,0.084-1.682,1.563-1.682h1.868v-3.18C16.522,2.044,15.608,1.998,14.693,2 C11.98,2,10,3.657,10,6.699V9H7v4l3-0.001V22h4v-9.003l3.066-0.001L17.525,9z"></path>
                                            </svg>
                                        </network><br/>
                                        <network network="linkedin">
                                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                                                width="35" height="35"
                                                viewBox="0 0 24 24"
                                                class="my-2 icon">    
                                                    <path d="M19,3H5C3.895,3,3,3.895,3,5v14c0,1.105,0.895,2,2,2h14c1.105,0,2-0.895,2-2V5C21,3.895,20.105,3,19,3z M9,17H6.477v-7H9 V17z M7.694,8.717c-0.771,0-1.286-0.514-1.286-1.2s0.514-1.2,1.371-1.2c0.771,0,1.286,0.514,1.286,1.2S8.551,8.717,7.694,8.717z M18,17h-2.442v-3.826c0-1.058-0.651-1.302-0.895-1.302s-1.058,0.163-1.058,1.302c0,0.163,0,3.826,0,3.826h-2.523v-7h2.523v0.977 C13.93,10.407,14.581,10,15.802,10C17.023,10,18,10.977,18,13.174V17z"></path>
                                            </svg>
                                        </network><br/>
                                        <network network="twitter">
                                            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px"
                                                width="35" height="35"
                                                viewBox="0 0 24 24"
                                                class="my-2 icon"
                                                >    
                                                    <path d="M19,3H5C3.895,3,3,3.895,3,5v14c0,1.105,0.895,2,2,2h14c1.105,0,2-0.895,2-2V5C21,3.895,20.105,3,19,3z M17.05,9.514 c0,0.086,0,0.171,0,0.343c0,3.257-2.486,7.029-7.029,7.029c-1.371,0-2.657-0.429-3.771-1.114c0.171,0,0.429,0,0.6,0 c1.114,0,2.229-0.429,3.086-1.029c-1.114,0-1.971-0.771-2.314-1.714c0.171,0,0.343,0.086,0.429,0.086c0.257,0,0.429,0,0.686-0.086 c-1.114-0.257-1.971-1.2-1.971-2.4c0.343,0.171,0.686,0.257,1.114,0.343c-0.686-0.6-1.114-1.286-1.114-2.143 c0-0.429,0.086-0.857,0.343-1.2c1.2,1.457,3,2.486,5.057,2.571c0-0.171-0.086-0.343-0.086-0.6c0-1.371,1.114-2.486,2.486-2.486 c0.686,0,1.371,0.257,1.8,0.771c0.6-0.086,1.114-0.343,1.543-0.6c-0.171,0.6-0.6,1.029-1.114,1.371 c0.514-0.086,0.943-0.171,1.457-0.429C17.907,8.743,17.479,9.171,17.05,9.514z"></path>
                                                </svg>
                                        </network>
                                    </div>
                                    </social-sharing>  
                                
                            <!-- Icons for facebook - end -->

                        </v-flex>

                        <v-flex lg11>
                            <p class="headline font-weight-light post-content px-3">{{blog.content}}</p>
                        </v-flex>
                    </v-layout>
                    
                         
                </div>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import axios from 'axios'

export default {
    name:'Post',
    data(){
        return{
            liked:false,
            id: this.$route.params.id,
            interest_name: this.$route.params.interest_name,
            blog: {},
            isFollow:null,
            upvotes:null
        }
    },

    async created() {
        var url = 'http://localhost:8000/api/Blog_id/'+this.id;
        var req = new Request(url)
        this.blog = await fetch(req)
                            .then(function (response) {
                                return response.json();
                            })
        this.upvotes = this.blog.total_upvote
        this.isFollow = this.blog.is_follow

    },

    methods:{
        async like(){
            var url = 'http://localhost:8000/api/likebutton/';
            axios.patch(url,{
                id:this.id,
                username:'vineet29'
            }).then((response)=>{
                this.liked = true;
                this.upvotes = response.data.total_upvote  
            }          
            )  
        },

        async unlike(){
            var url = 'http://localhost:8000/api/likebutton/';
            axios.patch(url,{
                id:this.id,
                username:'vineet29'
            }).then( (response)=>{
                this.liked = false
                this.upvotes = response.data.total_upvote  
            }
            ) 
        },


        async follow(){
            var url = 'http://localhost:8000/api/followview/'
            axios.post(url, {
                id: this.blog.author,
                username:'laxman'
            }).then(
                this.isFollow = true
            )
        },


        async unfollow(){
            var url = 'http://localhost:8000/api/followview/'
            axios.post(url, {
                id: this.blog.author,
                username:'laxman'
            }).then(
                this.isFollow = false
            )
        }
    }
}

</script>

<style lang="css">
    .post-content{
        line-height:2.7rem!important;
    }
    p.post-content::first-letter {
    font-size: 200%;
    color: #3F51B5;
    }
    .icon{
        cursor: pointer;
        fill:#757575;
        transition:transform 0s;
    }
    .icon:hover{
        transform:scale(1.1);
        color:blue;
        fill:blue;
    }
</style>