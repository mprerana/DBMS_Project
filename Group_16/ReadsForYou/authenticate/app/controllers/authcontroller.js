var exports = module.exports = {}


exports.signup = function(req,res){

	res.render('signup',{message:req.flash('signupMessage')}); 

}

exports.signin = function(req,res){

	res.render('signin',{message:req.flash('loginMessage')}); 

}

exports.dashboard = function(req,res){

	res.render('dashboard'); 

}

exports.logout = function(req,res){

  req.session.destroy(function(err) {
  res.redirect('/');
  });

}
exports.usercategory = function(req,res){

	res.render('usercategory'); 

}