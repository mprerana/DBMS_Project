<template>
    <div class="my-5">
        <v-toolbar flat color="white" class="pb-3">
            <v-container align-content-center>
                <v-layout row class="ml-5">
                    <v-flex>
                        <v-btn flat @click="queryTopic('yourfeed')">Your Feed</v-btn>
                    </v-flex>
                    <v-flex v-for="interest in getInterest" :key="interest.name">
                        <router-link to="/">
                            <v-btn flat @click="queryTopic(interest.name)">{{interest.name}}</v-btn>
                        </router-link>
                    </v-flex>
                    <v-flex>
                        <router-link to="/interest">
                            <v-btn flat>More</v-btn>
                        </router-link>
                    </v-flex>
                </v-layout>
            </v-container>  
        </v-toolbar>              
    </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
    name:'SubNav',
    data(){
        return{
        }
    },

    computed: {
        ...mapGetters([
            'getInterest'
        ])
    },

    methods: {
        ...mapActions([
            'queryTopic'
        ])
    }
    
}
</script>

<style scoped> 
    .router-link-active{
        text-decoration: none;
    }
</style>

