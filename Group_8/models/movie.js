const mongoose=require('mongoose');
const {Schema} = require('mongoose');

const comment= new Schema({
    user:{
        type:String
    },
    date:{
        type:Date,
        default:Date.now()
    },
    cmnt:{
        type:String
    }
},{_id:false});

const movieSchema = new Schema({
    name: {
        type: String,
        required: true,
    },
    title:{
        type:String
    },
    country:{
        type:String
    },
    year:{
        type:String
    },
    genre:{
        type:String
    },
    director:{
        type:String
    },
    cast:{
        type:Array,"default":[]
    },
    boxoffice:{
        type:String
    },
    ageres:{
        type:String
    },
    reldate:{
        type:String
    },
    plot:{
        type:String
    },
    trailers:{
        type:Array,"default":[]
    },
    cover:{
        type:String
    },
    duration:{
        type:String
    },
    comments:[comment],
    images:{
        type:Array,
        "default":[]
    },
    inthe:{
        type:Boolean
    }
});


const Movie = mongoose.model('movie', movieSchema);
module.exports={Movie};
