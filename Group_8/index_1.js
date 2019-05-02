const _ = require('lodash');
const express = require('express');
const bodyParser = require('body-parser');
const {ObjectID} = require('mongodb');
const mongoose = require('mongoose');
const hbs=require('hbs');
var firebase = require('firebase');
var helpers = require('handlebars-helpers')();


hbs.registerPartials(__dirname+'/partials')

hbs.registerHelper('ifIn',function(elem,list,options){
  if(list.indexOf(elem) > -1){
      return options.fn(this);
  }
  return options.inverse(this);
});


//const {appRoutes} = require('./routes/routes');
var {Movie} = require('./models/movie');
var {Theatre} = require('./models/theatre.js');
var {ShowTime} = require('./models/showtime.js');
var {Movie} = require('./models/movie.js')
var {User} = require('./models/users.js');
var {News} = require('./models/news.js');
var {Bookings} = require('./models/bookings.js');

var app = express();


const port = process.env.PORT || 3000;

mongoose.Promise=global.Promise;

mongoose.connect('mongodb://localhost:27017/MovieReview', {useNewUrlParser: true});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(__dirname + '/public'));

var config = {
  apiKey: "AIzaSyBgPWlk5PDTXzbgeQ1IBwzc4eiez52SlKk",
  authDomain: "dbms-f6217.firebaseapp.com",
  databaseURL: "https://dbms-f6217.firebaseio.com",
  projectId: "dbms-f6217",
  storageBucket: "dbms-f6217.appspot.com",
  messagingSenderId: "815776464470"
};
firebase.initializeApp(config);

app.set('view engine','hbs');

const auth = firebase.auth();

var cinema,movie_name,date,show_time;

var seats = [];
var final_seats = []
var price;



app.post('/:name',(req,res)=>{
    var name=req.params.name;
    if(name=="save_confirm"){
        userName = req.body.user_name;
        dateOfbirth = req.body.user_bday;
        mobileNumber = req.body.user_number;
        genre = req.body.user_genre;
        console.log(userName)
        console.log(dateOfbirth, mobileNumber, genre);
        var new_User = new User({
        watchlist:"",
        user_name:userName,
        dob:dateOfbirth,
        mobilenumber:mobileNumber,
        favgenre:genre
        });
    new_User.save().then((doc) => {
    console.log(doc);
    });
    Movie.find().limit(6).then((movies)=>{
        Movie.find().then((movie)=>{
            // res.render('../index-2.hbs',{val:false,username:name,movies,movie});
            console.log('11111111111111111111111111111111111111111111111111')
            console.log(userName)
            res.render('../index-2.hbs',{val:true,username:userName,movies,movie});
        })
    })
    }
    //res.send(results);

    else if(name=="list"){
        var ser=req.body.ser;
        ser = ser.toLowerCase()
            .split(' ')
            .map((s) => s.charAt(0).toUpperCase() + s.substring(1))
            .join(' ');
        var val=req.body.val;
        var ans;
        //console.log(ser);
        function ans1 (val){
            if(val==1) return {title:ser};
            else if(val ==2)return {year:ser};
            else if(val==3)return {director:ser};
            else if(val==4)return {genre:ser};
        };
        //console.log(ans1(val));
        Movie.find(ans1(val)).then(
            movies => res.render('../movielist.hbs',{data:movies}),
            err => res.send(err)
        );
        //res.send(results);
    }
     else if(name=="register_complete"){
        var email = req.body.email;
        const auth = firebase.auth();
        if(req.body.pass != req.body.re_pass){
            res.render('../register.hbs',{message:'Passwords did not match'})
        }
        else{
        auth.createUserWithEmailAndPassword(req.body.email,req.body.pass).then((data) => {
           console.log(data.user);
           auth.signInWithEmailAndPassword(req.body.email,req.body.pass)
           .catch(function(error){
               console.log(error);
               res.render('../login.hbs',{message:'Invalid credentials'});
           })
           .then((doc) => {
               var user=firebase.auth().currentUser;
               email=user.email;
               name = email.substring(0, email.indexOf('@'));
               Movie.find().limit(6).then((movies)=>{
                   Movie.find().then((movie)=>{
                       // res.render('../index-2.hbs',{val:false,username:name,movies,movie});
                       res.render('../formsite.hbs',{val:true,username:name,movies,movie});
                   })
               })
               //res.render('../');
               //var user = firebase.auth().currentUser;
               if(user != null){
                   uid =user.uid;
                   console.log(uid);
               }


           });


       });
    }

    }
    else if(name=="signin_complete"){
        auth.signInWithEmailAndPassword(req.body.email,req.body.pass)
.catch(function(error){

    console.log(error);
    res.render('../login.hbs',{message:'Invalid credentials'});
})
.then((doc) => {
    var user = firebase.auth().currentUser;
    email = user.email;
    name = email.substring(0, email.indexOf('@'));
    console.log(name)
    Movie.find().limit(6).then((movies)=>{
        Movie.find().then((movie)=>{
        res.render('../index-2.hbs',{val:true,username:name,movies,movie});

    })
})
});

    }
    else if(name=="seat_confirm"){
        //console.log(req.body);
  cinema = req.body.cinema;
  show_time = req.body.time
  console.log(movie_name,date);
Theatre.findOne({name: req.body.cinema}).then((theatres) => {
    // console.log(theatres._id);
ShowTime.findOne({movie_name:movie_name, theatre_id:String(theatres._id), show_time: req.body.time,date:date}).then((details) =>{
    // var seats = details.seats.split(" ");
    // console.log(details.seats[0])
    res.render('../book2.hbs',{data:details.seats});
})
})
    }
    else if(name=="booking"){
        movie_name = req.body.movie;
date = req.body.moviedate;
city = req.body.moviecity;
ShowTime.find({
movie_name: req.body.movie,
date: req.body.moviedate,
}).then((showtimes) => {
var theatres = new Array();
var keys = []
for(var i=0;i<showtimes.length;i++){
    var j;
    var key = showtimes[i].theatre_id;
    var value = showtimes[i].show_time;
    if(keys.length != 0){
        var flag = 0;
        for(j=0;j<keys.length;j++){
            if(key === keys[j]){
                flag = 1;
                break;
            }
        }
    }
    if(flag === 1){
        theatres[key].push(value);
    }
    else{
        keys.push(key);
        theatres[key] = new Array(value);
    }
}
console.log('city:---',req.body.moviecity)
Theatre.find({
    city: req.body.moviecity

}).then((theatre) => {
    var selected_cities = [];
    var theatre_names = []
    for(var city = 0;city < theatre.length;city++){
        selected_cities.push(theatre[city]._id);
        theatre_names.push(theatre[city].name);
    }
    console.log(selected_cities,theatre_names);
    var m,n;
    var final_display = [];
    var final_theatre_names = []
    for(m=0;m<selected_cities.length;m++){
        for(n=0;n<keys.length;n++){
            if(String(selected_cities[m]) === String(keys[n])){
                final_display[keys[n]] = (theatres[keys[n]]);
                final_theatre_names[keys[n]] = theatre_names[m];
            }
        }
    }
    var keys_1 = [];
    for(var k in final_display){
        keys_1.push(String(k));
    }

    test = {1:1,2:2,3:3,4:4}

    var output = {};
    for(var p=0;p<keys_1.length;p++){
        output[final_theatre_names[keys_1[p]]] = final_display[keys_1[p]];
    }
    console.log(output);
    // app.get('/',(req,res) => {
    //     res.render('../test.hbs',{
    //         key : test,
    //         X : output
    //     })
    // })
    res.render('../test.hbs', {key:test, X: output});
})

})}


    else if(name=="confirm_seats"){
        seats = []
 final_seats = []
 console.log('name' ,req.body);
 seats = req.body.sits.split(', ');
 seats = Array.from(new Set(seats));
 price = req.body.cost;
 console.log(seats);

 for(var i=0;i<seats.length-1;i++){
     final_seats.push(seats[i])
 }
 console.log(final_seats);
     res.render('../book3-buy.hbs',{tickets:final_seats.length,cost:req.body.cost});
    }
    else if(name=="confirm_tickets"){
        var user = firebase.auth().currentUser;
var newBooking = new Bookings({
    user:user.email,
    movie_name:movie_name,
    theatre_name:cinema,
    seats:final_seats,
    Amount:price,
    movie_date:date,
    screen:2
});

newBooking.save().then((doc) => {
    console.log(doc);
});
ShowTime.update({movie_name:movie_name,show_time:show_time,date:date},{$addToSet:{seats:final_seats}}).then((doc) => {
    console.log(doc);
})

res.render('../book-final.hbs',{theatre_name:cinema,movie_name:movie_name,date:date,show_time:show_time,seats:final_seats,price:price});
    }
    else{
    Movie.findOneAndUpdate({name:name},{$push:{comments:{user:"VK",cmnt:req.body.cmnt}}}).then(
        movie => res.render('../movie.hbs',movie),
        err => res.send(err)
    );}
});

app.get('/:name', (req, res) => {
    var name=req.params.name;
    //console.log(name);
    // let results = await Movie.find({});
    if(name=="register"){
        res.render('../register.hbs');
    }
    else if(name=="signin"){
        res.render('../login.hbs')
    }
    else if(name=="start"){
        Movie.find().then((movies)=>{
            console.log(movies);
            res.render('../movie-list-full.hbs',{movie:movies});
        })
    }
    else if(name == 'signout'){
        firebase.auth().signOut().then(function(){
            console.log('signed out');
            res.render('../login.hbs')
        },function(error){
            console.error('Sign Out Error',error);
        })
    }

    else
    {
    Movie.findOne({name:name}).then(
        (movie,err) => {
            if(movie==null||err)res.render('../404.hbs')
            else res.render('../movie.hbs',movie)
        })
    }
    //res.send(results);
});



app.listen(port, () => {
  console.log(`Started up at port ${port}`);
});

module.exports = {app};
