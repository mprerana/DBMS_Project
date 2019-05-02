var mongoose = require('mongoose');

var Theatre = require('./theatre.js');

var ShowTime = mongoose.model('ShowTime',{
    movie_name: {
        type : String,
        required: true,
        minlength: 1,
        trim : true
    },
    show_time:{
        type: String,
        required: true,
        minlength : 1,
        trim:true
    },
    date:{
        type: String,
        required: true,
        minlength: 1,
        trim : true
    },
    screen_no: {
        type: Number,
        required: true
    },
    theatre_id:{
        type: Theatre
    },
    seats:{
        type: Array,
        required:true
    }
});

module.exports = {ShowTime};
