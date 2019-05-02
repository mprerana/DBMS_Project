var firebase = require('firebase');
const express = require('express');
const hbs = require('hbs');


var app = express();
app.set('view engine','hbs');
app.use(express.static(__dirname+'/public'));


  var config = {
    apiKey: "AIzaSyBgPWlk5PDTXzbgeQ1IBwzc4eiez52SlKk",
    authDomain: "dbms-f6217.firebaseapp.com",
    databaseURL: "https://dbms-f6217.firebaseio.com",
    projectId: "dbms-f6217",
    storageBucket: "dbms-f6217.appspot.com",
    messagingSenderId: "815776464470"
  };
  firebase.initializeApp(config);

 const auth = firebase.auth();
auth.createUserWithEmailAndPassword('yuvi666666@gmail.com','yuvraj12').then((data) => {
    console.log(data.user);
});
