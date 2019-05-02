<template>
    <div class="interest">
        <SubNav/>
        <v-container>
            <v-layout row>
                <v-flex lg12 md12>
                    <v-layout row wrap class="ml-5">
                        <InterestCard v-for="topic in getTopics" :key="topic.id"  v-bind:topic="topic" class="mx-3 my-3"/>
                    </v-layout>
                </v-flex>
            </v-layout>
        </v-container>
         
    </div>
</template>

<script>
import InterestCard from '../components/interest-card'
import SubNav from '../components/SubNav'
import { mapGetters } from 'vuex';

export default {
    name: 'Interest',

    components:{
        InterestCard,
        SubNav
    },

    data: () => ({
        loaded:false
    }),

    computed: {
         ...mapGetters([
            'getTopics'
        ])
    },

    async mounted(){
        this.loaded = false
        var url = 'http://localhost:8000/api/interests/';
        var req = new Request(url)
        this.$store.state.topics = await fetch(req)
                                    .then(function (response) {
                                        return response.json();
                                    })
        this.loaded = true
    }
       
    

}
</script>
