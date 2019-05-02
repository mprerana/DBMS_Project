var {mongoose} = require('./db/mongoose');
var {Theatre} = require('./models/theatre.js');
var {ShowTime} = require('./models/showtime.js');
var {Movie} = require('./models/movie.js');
var {User} = require('./models/users.js');
var {News} = require('./models/news.js');
var {Bookings} = require('./models/bookings.js');


// var movie = new ShowTime({
//     movie_name: "About Time",
//     date: "23-10-19",
//     show_time: "10:45",
//     screen_no: 2,
//     theatre_id:"5ca48d965676c74a8e2eed9e"
// });
//
// movie.save().then((doc) => {
//     console.log(doc);
// });

var newMovie = new Movie({
    name:'AboutTime',
    title: 'AboutTime',
    country: 'India',
    year: '2019',
    genre: 'Action',
    director: 'Abhishek',
    cast: ['Yuvraj','Dhoni'],
    boxoffice: '350 Cr',
    ageres: 'R',
    reldate: '23-10-19',
    plot:'Cricket',
    trailers:["oiXdPolca5w"],
    cover:"/uploads/theusualsuspects.jpg",
    duration: '187 min',
    comments:[{user : 'Yuvraj',cmnt : 'dvbdvbjkvsdbjdvskjjk'}],
    images:["usualsupects1.jpg"]
});

newMovie.save().then((doc) => {
    console.log(doc);
});






// var newUser = new User({
//     user_name:'Yuvraj',
//     watchlist:['AboutTime'],
//     dob:'12-12-1981',
//     profilephoto:'/uploads/xyz.jpg',
//     mobilenumber:'8976801234',
//     gender:'M'
// });
//
// newUser.save().then((doc) => {
//     console.log(doc);
// })

// var newArticle = new News({
//     tags:['bdkjdj','mdlkklkd'],
//     article:'jdanklc klcklklczcc',
//     source:'kjsdvdvnjndsn'
// });
//
// newArticle.save().then((doc) => {
//     console.log(doc);
// })

// var newBooking = new Bookings({
//     user:'hemanth',
//     movie_name:'AboutTime',
//     theatre_name:'Empire',
//     seats:['A8','A9'],
//     Amount:'360',
//     movie_date:'23-10-19',
//     screen:2
// });
//
// newBooking.save().then((doc) => {
//     console.log(doc);
// })
