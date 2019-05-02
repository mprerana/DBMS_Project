var mongoose = require('mongoose');

var News = mongoose.model('News',{
    tags:{
        type:'Array',
        required:true,
    },
    article:{
        type:String,
        required:true
    },
    date:{
        type:Date,
        default:Date.now()
    },
    source:{
        type:String,
        required:true
    }
});

module.exports = {News};
