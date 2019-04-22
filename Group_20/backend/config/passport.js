const db = require('../models/database');
const JwtStrategy = require('passport-jwt').Strategy,
    ExtractJwt = require('passport-jwt').ExtractJwt;
// load up the user model
module.exports = function(passport) {
const opts = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderWithScheme('JWT'),
    secretOrKey: 'nodeauthsecret',
  };
passport.use('jwt', new JwtStrategy(opts, function(jwt_payload, done) {
    db.getUser(jwt_payload.username)
      .then((user) => { return done(null, user); })
      .catch((error) => { return done(error, false); });
  }));
};