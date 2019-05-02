<template>
    <v-app class="white">
      <Navbar/>
      <!-- <SubNav></SubNav> -->
      <v-content class="pt-0">
        <router-view></router-view>
      </v-content>
    </v-app>
</template>

<script>
import Navbar from './components/Navbar'
// import SubNav from './components/SubNav'


export default {
  name: 'App',
  components: {
    Navbar, 
    // SubNav
  },
  data () {
    return {
      //
    }
  }
}
</script>

<style lang="css">
  @import url('https://fonts.googleapis.com/css?family=Montserrat:400,700');

</style>

