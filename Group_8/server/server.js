var {mongoose} = require('./db/mongoose');
var {Theatre} = require('./models/theatre.js');
var {ShowTime} = require('./models/showtime.js');
const express = require('express');
const hbs = require('hbs');

var helpers = require('handlebars-helpers')();

var app = express();
app.set('view engine','hbs');
app.use(express.static('public'));

const bodyParser = require('body-parser')

var urlencodedParser = bodyParser.urlencoded({extended:false});

const middlewares = [
  // ...
  bodyParser.urlencoded()
]

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

app.post('/seat_confirm',urlencodedParser,(req, res,) => {
    // var Kitten = req.Kitten;
     // PROBLEM: it returns empty, while I expect req.body
     console.log('name' ,req.body);
    
    Theatre.findOne({name: req.body.cinema}).then((theatres) => {
        console.log(theatres._id);
    ShowTime.findOne({movie_name:req.body.movie, theatre_id:String(theatres._id), show_time: req.body.time}).then((details) =>{
        var seats = details.seats.split(" ");
        res.render('book2.hbs',{data : seats});
    })
    })
});

app.post('/confirm_seats',urlencodedParser,(req, res,) => {
    // var Kitten = req.Kitten;
     // PROBLEM: it returns empty, while I expect req.body
     console.log('name' ,req.body);
    res.render('book3-buy.hbs',{data : req.body.cost});
});


// movie.save((doc) => {
//     console.log(doc);
// });

ShowTime.find({
    movie_name:'About Time',
    date: '23-10-19',
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
    Theatre.find({
        city: 'Vijayawada'
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
        app.get('/',(req,res) => {
            res.render('test.hbs',{
                key : test,
                X : output
            })
        })

    })
    app.listen(3000,() => {
        console.log('Server is upon port 3000')
    })
})
