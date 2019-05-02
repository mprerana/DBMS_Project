<template>

    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <template v-slot:activator="{ on }">
        
            <v-btn flat outline color="primary" v-on="on" class="mx-2">
                Create Post
            </v-btn>
            
      </template>
      
      <v-card>
        <v-toolbar flat color="white">
          <v-btn icon @click="dialog = false">
            <v-icon color="primary">close</v-icon>
          </v-btn>
          
          <v-spacer></v-spacer>
       
        <v-btn outline color="primary" flat @click="dialog = false">Draft</v-btn>
        <v-btn outline color="primary" flat @click="addPost">Post</v-btn>
        
        </v-toolbar>

        <v-container class="px-5">

        <v-layout row wrap>
            <v-flex xs12 sm6 md12 lg12>
                <v-flex xs12 sm6 md6 lg6>
                   <input v-model="heading" type="text" id="title" placeholder="Untitled Post" class="title">
                </v-flex>
            </v-flex>
            <v-layout row wrap class="mt-3 mb-3">  
                <v-flex xs12 sm6 md12 class="picture-box text-xs-center py-5">
                    <form enctype="multipart/form-data" novalidate v-if="isInitial || isSaving">
                        <h1>Upload images</h1>
                        <div class="dropbox">
                        <input type="file" multiple :name="uploadFieldName" :disabled="isSaving" @change="filesChange($event.target.name, $event.target.files); fileCount = $event.target.files.length"
                            accept="image/*" class="input-file">
                            <p v-if="isInitial">
                            Drag your file(s) here to begin<br> or click to browse
                            </p>
                            <p v-if="isSaving">
                            Uploading {{ fileCount }} files...
                            </p>
                        </div>
                    </form>
                </v-flex> 
            </v-layout>
            <v-flex lg12 md12 sm12 xs12 class="py-3">
                <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
            </v-flex>
        </v-layout>

        </v-container>
   
      </v-card>
    </v-dialog>
         

</template>


<script>
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
import axios from 'axios'

export default {
    name:'Blog',
    data:()=>({
        dialog: false,
        file:false,

        items: [
          { title: 'Home', icon: 'dashboard' },
          { title: 'About', icon: 'question_answer' }
        ],
        right: null,

        heading: '',
        notifications: false,
        sound: true,
        widgets: false,
        editor: ClassicEditor,
        editorData: '',
        editorConfig: {
            // The configuration of the editor.
        }
    }),

    methods: {
        async addPost(){
            axios.post('http://localhost:8000/api/create_blog/', {
                heading: this.heading,
                content: this.editorData,
                author : 5,
                interests : 2,
            } )
            .then(
                this.dialog = false
            )
        }
    },
}
</script>


<style lang="scss">
    .picture-box{
        border-style: dotted;
        height: 130px;
        width:100%;
    }
    dropbox {
    outline: 2px dashed grey; /* the dash box */
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
    padding: 10px 10px;
    min-height: 200px; /* minimum height */
    position: relative;
    cursor: pointer;
  }

  .input-file {
    opacity: 0; /* invisible but it's there! */
    width: 100%;
    height: 200px;
    position: absolute;
    cursor: pointer;
  }

  .dropbox:hover {
    background: lightblue; /* when mouse over to the drop zone, change color */
  }

  .dropbox p {
    font-size: 1.2em;
    text-align: center;
    padding: 50px 0;
  }
    .title{
        font-size: 2.7rem!important;
        height:50px;
        border:none;
        outline:none;
    }
</style>