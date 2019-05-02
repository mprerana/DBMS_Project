<template>
    <div>
        <nav>
            <v-toolbar flat app color="white">
                <v-toolbar-title>
                <span class="font-weight-bold text-uppercase">
                    <router-link class="logo" tag="span" to="/">
                        BlogIn'
                    </router-link>
                </span>
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <v-text-field
                        hide-details
                        prepend-icon="search"
                        single-line
                        class="mx-2"
                ></v-text-field>
                
                <Blog />
               

                <v-dialog v-model="dialog" persistent max-width="600px">
                    <template v-slot:activator="{ on }">
                        <v-btn outline color="primary" flat v-on="on">Sign Up</v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                        <span class="display-1 font-weight-bold pl-3">Sign Up</span>
                        <v-spacer></v-spacer>
                        <v-btn fab color="blue darken-1" flat @click="dialog = false"><v-icon>cancel</v-icon></v-btn>
                        </v-card-title>
                        <v-card-text>
                        <v-container grid-list-md>
                            <v-layout wrap>
                            <v-flex xs12>
                                <v-text-field v-model="this.username" label="Username*" required></v-text-field>
                                <p v-if="this.error"  class="error-message">{{this.result.username_error}}</p>
                            </v-flex>
                            
                            <v-flex xs12>
                                <v-text-field v-model="email" label="Email*" required></v-text-field>
                                <p v-if="this.error"  class="error-message">{{this.result.email_error}}</p>
                            </v-flex>
                            <v-flex xs5>
                                <v-text-field v-model="password" label="Password*" type="password" required></v-text-field>
                                <p v-if="this.error"  class="error-message">{{this.result.password_error}}</p>
                            </v-flex>
                            <v-flex xs5 class="ml-2">
                                <v-text-field v-model="password1" label="Confirm Password*" type="password" required></v-text-field>
                                <p v-if="this.error"  class="error-message">{{this.result.password2_error}}</p>
                            </v-flex>
                            </v-layout>
                        </v-container>
                        <small class="pl-3">*indicates required field</small>
                        </v-card-text>
                        <v-card-actions>
                        
                        <v-btn large dark color="blue darken-1 ml-3 mb-3" flat @click="sendData">Next</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>

                

                <v-dialog v-model="dialog3" persistent max-width="600px">
                    <template v-slot:activator="{ on }">
                        <v-btn outline color="primary" flat v-if="!userLoaded" v-on="on">Log In</v-btn>
                        <v-btn outline color="primary" flat v-else @click="logout">Log Out</v-btn>
                    </template>
                    <v-card>
                       
                            <v-card-title>
                            <span class="display-1 font-weight-bold pl-3">Log In</span>
                            <v-spacer></v-spacer>
                            <v-btn fab color="blue darken-1" flat @click="dialog3 = false"><v-icon>cancel</v-icon></v-btn>
                            </v-card-title>
                            <v-card-text>
                            <v-container grid-list-md>
                                <v-layout wrap>
                                <v-flex xs12>
                                    <v-text-field v-model="this.username" label="Username*" required></v-text-field>
                                </v-flex>
                            
                                <v-flex xs12>
                                    <v-text-field v-model="password" label="Password*" type="password" required></v-text-field>
                                </v-flex>
                                <p v-if="this.error"  class="error-message">{{this.result.non_field_errors}}</p>
                                </v-layout>
                            </v-container>
                            <small class="pl-3">*indicates required field</small>
                            </v-card-text>
                            <v-card-actions>
                            
                            <v-btn large dark color="blue darken-1 ml-3 mb-3" flat @click="authenticate">Login</v-btn>
                            </v-card-actions>
                    </v-card>
                </v-dialog>
                
            </v-toolbar>
        </nav>
    </div>
</template>

<script>
import Blog from './Blog'
import axios from 'axios'



export default {
    name:'Navbar',

    components:{
        Blog
    },

    data(){
        return{
            dialog: false,
            dialog3: false,
            email: '',
            password: '',
            password1: '',
            result:null,
            error:false,
            userLoaded:false
        }
    },

    methods: {

        // printFunction(data){
        //     console.log(data)
        // },
        

        async sendData(){
            
            axios.post('http://localhost:8000/api/register/', {
                username: this.username,
                email: this.email,
                password: this.password,
                password1: this.password1
            })
            .then(
                response => {

                    // this.printFunction(response)

                    this.result = response.data
                
                    if( this.result.error == "False" ){
                        this.dialog = false
                    }
                    else{
                        this.error = true;
                    }
                        
                }
            )
        },
       
        authenticate () {
            const payload = {
                username: this.username,
                password: this.password
            }
            axios.post(this.$store.state.endpoints.obtainJWT, payload)
                .then((response) => {
                        this.result = response
                        this.$store.commit('updateToken', response.data.token)
                        this.userLoaded = true
                        this.dialog3 = false
                })
                .catch(e =>{
                    if(e){
                        this.result = {non_field_errors:"Login Credentials Not Valid"};
                        this.error=true
                    }
                })
            },

            logout(){
                this.$store.commit('removeToken')
                this.userLoaded = false
            }
    }
    
}
</script>

<style lang="css">
    .logo{
        cursor:pointer;
    }
    .error-message{
        color:red;
        font-size:1em;
    }
</style>
