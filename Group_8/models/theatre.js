var mongoose = require('mongoose');

Schema = mongoose.Schema;

var Theatre = mongoose.model('Theatre',{
    name: {
        type : String,
        required: true,
        minlength: 1,
        trim : true
    },
    location:{
        type: String,
        required: true,
        minlength : 1,
        trim:true
    },
    city: {
        type: String,
        required: true,
        minlength : 1,
        trim:true
    },
    screens: {
        type: Number,
        required: true
    }

});

module.exports = {Theatre};
