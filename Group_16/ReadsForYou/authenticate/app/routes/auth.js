var authController = require('../controllers/authcontroller.js');
var session = require('express-session');
// var connect = require('../config/passport/passport.js')
module.exports = function(app,passport){
app.get('/', function(req, res){
  res.render('index.ejs');
 });

var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root",
  database: "project"
});

con.connect(function(err){
  if(err){
    throw err;
  }
  console.log('Mysql Connected...');
});
app.get('/signup', authController.signup);


app.get('/signin', authController.signin);


app.post('/signup', passport.authenticate('local-signup',  { successRedirect: '/usercategory',
                                                    failureRedirect: '/signup',failureFlash:true}
                                                    ));


app.get('/dashboard',isLoggedIn, authController.dashboard);


app.get('/logout',authController.logout);


app.post('/signin', passport.authenticate('local-signin',  { successRedirect: '/dashboard',
                                                    failureRedirect: '/signin',failureFlash:true}
                                                    ));

app.get('/userinfo', function(req, res){
	var ssn = req.session
	console.log("Current isLoggedIn user:");
	console.log(req.session);
	console.log("***********");
  console.log(req.session.passport.user);
 });

app.get('/usercategory', authController.usercategory);

app.post('/usercategory', function(req,res){
    console.log(req.body);
    var items = req.body;
    console.log(typeof items);
    console.log(items);
    var UserId = req.session.passport.user;
    console.log(UserId);
    var xt = 0;
    for (var i in items) {
      for(var j in items[i]){
     console.log(items[i]);
    let data  = {
    UserId:UserId,
    CategoryId:items[i][j]
  };
  xt = xt+1;
  console.log("*********");
  console.log(data);

  

  var sql = "INSERT INTO Preferences set ?";
  con.query(sql,data, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });
      }}
    res.redirect('/dashboard');
});

function isLoggedIn(req, res, next) {
    if (req.isAuthenticated())
        return next();

    res.redirect('/signin');
}



}






