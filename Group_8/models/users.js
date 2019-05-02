var mongoose = require('mongoose');

var User = mongoose.model('User',{
    user_name:{
        type:String,
        required: true,
        minlength:1,
        trim:true,
        unique:true
    },
    watchlist:{
        type:Array,
        "default":[],
        required:true,
        minlength:1,
        trim:true
    },
    dob:{
        type:String,
        required:true,
        minlength:1,
        trim:true
    },
    profilephoto:{
        type:String,
        minlength:1,
        trim:true
    },
    mobilenumber:{
        type:String,
        minlength:10,
        maxlength:10,
        required:true,
        trim:true
    },
    favgenre:{
        type:String,
        minlength:1,
        required:true,
        trim:true
    }


});

module.exports = {User};
