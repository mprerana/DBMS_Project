var mongoose = require('mongoose');
var {Theatre} = require('./theatre.js');

var Bookings = mongoose.model('Bookings',{
    booked_date:{
        type:Date,
        default:Date.now()
    },
    user:{
        type:String,
        required:true
    },
    movie_name:{
        type:String,
        required:true
    },
    theatre_name:{
        type:String
    },
    seats:{
        type:Array
    },
    Amount:{
        type:Number
    },
    movie_date:{
        type:String
    },
    screen:{
        type:String
    },
    showtime:{
        type:String
    }
});

module.exports = {Bookings};
