var {mongoose} = require('./db/mongoose');
var {Theatre} = require('./models/theatre.js');
var {ShowTime} = require('./models/showtime.js');
var {Movie} = require('./models/movie.js')
var {User} = require('./models/users.js');
var {News} = require('./models/news.js');
var {Bookings} = require('./models/bookings.js');

const express = require('express');
const hbs = require('hbs');
var firebase = require('firebase');
var helpers = require('handlebars-helpers')();

//const {appRoutes} = require('./routes/routes');

var app = express();
app.set('view engine','hbs');
app.use(express.static(__dirname+'/public'));
//appRoutes(app);
const bodyParser = require('body-parser')

var urlencodedParser = bodyParser.urlencoded({extended:false});

const middlewares = [
  // ...
  bodyParser.urlencoded()
]

hbs.registerHelper('ifIn',function(elem,list,options){
    if(list.indexOf(elem) > -1){
        return options.fn(this);
    }
    return options.inverse(this);
});
// var movie = new ShowTime({
//     movie_name: "Bahubali",
//     date: "23-10-19",
//     show_time: "15:15",
//     screen_no: 3,
//     theatre_id: "5c9b603ba6e6cf02c7fd6a73"
// });

// app.get('/seat_confirm', function(req, res) {
//     // var Kitten = req.Kitten;
//  // PROBLEM: it returns empty, while I expect req.body
//     res.render('book2.hbs');
// });

var config = {
  apiKey: "AIzaSyBgPWlk5PDTXzbgeQ1IBwzc4eiez52SlKk",
  authDomain: "dbms-f6217.firebaseapp.com",
  databaseURL: "https://dbms-f6217.firebaseio.com",
  projectId: "dbms-f6217",
  storageBucket: "dbms-f6217.appspot.com",
  messagingSenderId: "815776464470"
};
firebase.initializeApp(config);


app.get('/register',(req,res) => {
    res.render('../register.hbs');
});
var actionCodeSettings = {
  // URL you want to redirect back to. The domain (www.example.com) for this
  // URL must be whitelisted in the Firebase Console.
  url: 'https://www.example.com/finishSignUp?cartId=1234',//change this url to something.
  // This must be true.
  handleCodeInApp: true,
  dynamicLinkDomain: 'example.page.link'
};



app.post('/register_complete',urlencodedParser,(req,res)=>{
    console.log(req.body);
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
          res.render('../register.hbs');
          var user = firebase.auth().currentUser;
          if(user != null){
              uid =user.uid;
              console.log(uid);
          }


      });


  });
}

    // res.render('../login.hbs');
});


app.get('/signin',(req,res) => {
    res.render('../login.hbs');
});
const auth = firebase.auth();


app.post('/signin_complete',urlencodedParser,(req,res)=>{
    console.log(req.body);
    auth.signInWithEmailAndPassword(req.body.email,req.body.pass)
    .catch(function(error){

        console.log(error);
        res.render('../login.hbs',{message:'Invalid credentials'});
    })
    .then((doc) => {
        var user = firebase.auth().currentUser;
        email = user.email
        res.render('../index-2.hbs',{val:false,username:email});

    });

});


var cinema,movie_name,date,show_time;
app.post('/seat_confirm',urlencodedParser,(req, res,) => {
    // var Kitten = req.Kitten;
     // PROBLEM: it returns empty, while I expect req.body
      console.log(req.body);
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
});

app.get('/start',(req,res)=>{
    Movie.find().then((movies)=>{
        console.log(movies);
        res.render('../movie-list-full.hbs',{movie:movies});
    })

});

app.post('/booking',urlencodedParser,(req,res)=>{
    console.log(req.body);
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

})




})

var seats = [];
var final_seats = []
var price;
app.post('/confirm_seats',urlencodedParser,(req, res) => {
    // var Kitten = req.Kitten;
     // PROBLEM: it returns empty, while I expect req.body
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
});

app.post('/confirm_tickets',urlencodedParser,(req,res) => {
    console.log(req.body);
    console.log('seats',final_seats);
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
})

app.listen(3000,() => {
        console.log('Server is upon port 3000')
    })
