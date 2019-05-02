<template>
    <div class="sidemenu">
      <v-navigation-drawer permanent>
            <v-list class="pt-0 pl-2">
                <v-flex  v-for="item in items" :key="item.title">
                  <p class="headline font-weight-bold link" @click="updateTab(item.title)">{{ item.title }}</p>
                </v-flex>
            </v-list>
        </v-navigation-drawer>  
    </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
    name:'SideMenu',
    props:{
      items:Array
    },
    data () {
      return {
        right: null
      }
    },

    methods: {
      ...mapMutations([
        'updateTab'
      ])
    },
}
</script>

<style lang="css" >
  .route{
    cursor:pointer;
  }
  .sidemenu{
    position:fixed;
  }
  .theme--light.v-navigation-drawer:not(.v-navigation-drawer--floating) .v-navigation-drawer__border {
    background-color:rgb(255,255,255) ! important; 
}
  .link{
    cursor:pointer;
  }
</style>