var express    = require('express')
var app        = express()
var passport   = require('passport')
var session    = require('express-session')
var bodyParser = require('body-parser')
var env        = require('dotenv')
var exphbs     = require('express-handlebars')
var flash      = require('connect-flash')
const path     = require('path');


// For Passport
app.use(session({ secret: 'keyboard cat',resave: true, saveUninitialized:true})); // session secret
app.use(passport.initialize());
app.use(passport.session()); // persistent login sessions
app.use(flash());
app.use('/assets',express.static('assets'));


const errorController = require('./controllers/error');

const db = require('./util/database');
const Entity = require('./models/book');


// Entity.Users.create_table();
Entity.Category.create_table();
Entity.Books.create_table();
Entity.Favourites.create_table();


//Books.fetchAllFromFavorites().then(result => console.log(result[0][0]['UserId']));


app.set('view engine', 'ejs');
app.set('views', 'views');

const adminRoutes = require('./routes/admin');
const userRoutes = require('./routes/user');

const profileRoutes = require('./routes/profile');

app.use(bodyParser.urlencoded({ extended:false }));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function(req, res){
    res.render('home')
});

app.use(userRoutes);
app.use(profileRoutes);
app.use('/admin', adminRoutes);




//Models
var models = require("./authenticate/app/models");
//Routes
var authRoute = require('./authenticate/app/routes/auth.js')(app,passport);

//load passport strategies
require('./authenticate/app/config/passport/passport.js')(passport,models.user);

//Sync Database
models.sequelize.sync().then(function(){
console.log('Nice! Database looks fine')

}).catch(function(err){
console.log(err,"Something went wrong with the Database Update!")
});


app.use(errorController.get404);

app.listen(8080);





