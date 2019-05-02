
  //load bcrypt
  var bCrypt = require('bcrypt-nodejs');

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
exports.con = con;
  function fillProfile(data){


  let profile_data  = {
    FirstName:data.firstname,
    LastName:data.lastname,
    Sex:data.sex,
    Email:data.email
  };
  console.log("*********");
  console.log(profile_data);
  var sql = "INSERT INTO Profile set ?";
  con.query(sql,profile_data, function (err, result) {
    if (err) throw err;
    console.log("1 record inserted");
  });
}

  module.exports = function(passport,user, profile){
  var Profile = profile;  
  var User = user;
  var LocalStrategy = require('passport-local').Strategy;


  passport.serializeUser(function(user, done) {
          done(null, user.UserId);
      });


  // used to deserialize the user
  passport.deserializeUser(function(UserId, done) {
      User.findByPk(UserId).then(function(user) {
        if(user){
          done(null, user.get());
        }
        else{
          done(user.errors,null);
        }
      });

  });


  passport.use('local-signup', new LocalStrategy(

    {           
      usernameField : 'email',
      passwordField : 'password',
      passReqToCallback : true // allows us to pass back the entire request to the callback
    },

    function(req, email, password, done){
       

      var generateHash = function(password) {
      return bCrypt.hashSync(password, bCrypt.genSaltSync(8), null);
      };

       User.findOne({where: {email:email}}).then(function(user){

      if(user)
      {
        // console.log('Email already exists');
        // return done(null, false, {message : 'That email is already taken'} );
        return done(null, false,  req.flash('signupMessage','That email is already taken'));
      }

      else
      {
        var userPassword = generateHash(password);
        var data =
        { email:email,
        password:userPassword,
        firstname: req.body.firstname,
        lastname: req.body.lastname,
        dob: req.body.dob,
        sex:req.body.sex
        };
        fillProfile(data);
         User.create(data).then(function(newUser,created){
          if(!newUser){
            return done(null,false);
          }

          if(newUser){
            return done(null,newUser);
            
          }


        });
      }


    }); 



  }



  ));
    
  //LOCAL SIGNIN
  passport.use('local-signin', new LocalStrategy(
    
  {

  // by default, local strategy uses username and password, we will override with email
  usernameField : 'email',
  passwordField : 'password',
  passReqToCallback : true // allows us to pass back the entire request to the callback
  },

  function(req, email, password, done) {

    var User = user;

    var isValidPassword = function(userpass,password){
      return bCrypt.compareSync(password, userpass);
    }

    User.findOne({ where : { email: email}}).then(function (user) {

      if (!user) {
        return done(null, false, req.flash('loginMessage','Email does not exist'));
      }

      if (!isValidPassword(user.password,password)) {

        return done(null, false, req.flash('loginMessage','Incorrect password.'));

      }

      var userinfo = user.get();
      console.log("UserId is...");
      console.log(userinfo.UserId);
      return done(null,userinfo);

    }).catch(function(err){

      console.log("Error:",err);

      return done(null, false, req.flash('loginMessage','Something went wrong with your Signin' ));


    });

  }
  ));

  }

