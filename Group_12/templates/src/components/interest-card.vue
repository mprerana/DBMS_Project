
<template>
    <v-flex xs12 sm12 md3 lg3>
      <v-card >
        <v-card-title primary-title>
          <div>
            <div class="headline">{{topic.interest_name}} 
                <v-btn outline fab color="indigo" small>
                <v-icon v-if="!is_following" @click="followTopic">add</v-icon>
                <v-icon v-else @click="unfollowTopic">done</v-icon>
            </v-btn>
            </div>
            <span class="grey--text pr-1">{{followercount}} Followers</span>
          </div>
        </v-card-title>
        <v-img
          :src="imageUrl"
          height="200px"
          v-if="loaded"
        >
        </v-img>
        
      </v-card>
    </v-flex>

</template>

<script>
  import axios from 'axios'

  export default {
    name:'InterestCard',
    props:{
      topic:{
        interest_name:String,
        followers:Number,
        isFollowing:Boolean
      }
    },
    data: () => ({
      is_following:null,
      imageUrl:null,
      loaded:null,
      followercount:null
    }),

    async created(){
        this.is_following = this.topic.isFollowing,
        this.followercount = this.topic.followers
        
        this.loaded = false
        var urlFeatured = 'https://newsapi.org/v2/everything?' +
          'q=' + this.topic.interest_name + '&'+
          'from=2019-04-05&' +
          'sortBy=popularity&' +
          'apiKey=ed7767f07ae745dd9a229ca0b63d3a92';

        var reqFeatured = new Request(urlFeatured);
        var data = await fetch(reqFeatured)
                            .then(function(response) {
                            return response.json();
                        })
        this.imageUrl = data.articles[0]["urlToImage"]
        this.loaded = true
      
    },

    methods:{
      async followTopic(){
        axios.post('http://localhost:8000/api/interests/',{
          id:this.topic.interest_name,
          username:'laxman'
          }).then( (response) => {
            this.is_following = true,
            this.followercount = response.data.followers
          }
          )
      },

      async unfollowTopic(){
        axios.post('http://localhost:8000/api/interests/',{
          id:this.topic.interest_name,
          username:'laxman'
          }).then( (response) => {
            this.is_following = false,
            this.followercount = response.data.followers
          } 
          )
      }
    }
  }
</script>