const express = require('express');
const jwt = require('jsonwebtoken');
const passport = require('passport');
const router = express.Router();
const fs = require('fs');
const path = require('path');
const nodemailer = require('nodemailer');
const crypto = require('crypto');

require('../config/passport')(passport);
const db = require('../models/database');




router.get('/', passport.authenticate('jwt', { session: false}), function(req, res) {
  var token = getToken(req.headers);
  if (token) {
      db.getUserProfile(req.user.username)
      .then(resolve => {
          if(resolve.pictureurl){
              fs.readFile(resolve.pictureurl, function read(err, data) {
                  if (err) {
                      return res.status(403).send({success: false, msg: 'Unauthorized.'})
                  }
                  resolve.picture = data.toString();
                  delete resolve["pictureurl"]
                  return res.status(200).send(resolve)
              });
          } else {
          return res.status(200).send(resolve)
          }
      })
      .catch(e => {
          console.log(e)
          return res.status(403).send({success: false, msg: 'Unauthorized.'})
      })
  } else {
      return res.status(403).send({success: false, msg: 'Unauthorized.'});
  }
});

router.post('/', passport.authenticate('jwt', { session: false}), function(req, res) {
  var token = getToken(req.headers);
  if (token) {
      if(req.body.options.hasOwnProperty('picture')){
          const pictureurl = __dirname + "/../models/pictures/" + crypto.createHash('md5').update(req.user.id.toString()).digest('hex');
          fs.writeFile(pictureurl, req.body.options.picture, function(err) {
              if(err) {
                  return res.status(403).send({success: false, msg: 'Unauthorized.'})
              }
              req.body.options.pictureurl = pictureurl;
              db.getUserProfile(req.user.username)
              .then(resolve => {
                  if(resolve.hasOwnProperty("username")){
                      db.updateUserProfile(req.user.username,req.body.options)
                      .then(resolve => {
                          return res.status(200).send({success: true, msg: 'Updated.'});
                      })
                      .catch(e => {
                          console.log(e)
                          return res.status(403).send({success: false, msg: 'Unauthorized.'})
                      })
                  } else {
                      db.insertUserProfile(req.user.username,req.body.options)
                      .then(resolve => {
                          return res.status(200).send({success: true, msg: 'Updated.'});
                      })
                      .catch(e => {
                          console.log(e)
                          return res.status(403).send({success: false, msg: 'Unauthorized.'})
                      })
                  }
              })
          }); 
      } else {
          db.getUserProfile(req.user.username)
          .then(resolve => {
              if(resolve.hasOwnProperty("username")){
                  db.updateUserProfile(req.user.username,req.body.options)
                  .then(resolve => {
                      return res.status(200).send({success: true, msg: 'Updated.'});
                  })
                  .catch(e => {
                      console.log(e)
                      return res.status(403).send({success: false, msg: 'Unauthorized.'})
                  })
              } else {
                  db.insertUserProfile(req.user.username,req.body.options)
                  .then(resolve => {
                      return res.status(200).send({success: true, msg: 'Updated.'});
                  })
                  .catch(e => {
                      console.log(e)
                      return res.status(403).send({success: false, msg: 'Unauthorized.'})
                  })
              }
          })
      }
  } else {
      return res.status(403).send({success: false, msg: 'Unauthorized.'});
  }
});

router.post('/changePassword', passport.authenticate('jwt', { session: false}), function(req, res) {
  var token = getToken(req.headers);
  if (token) {
      jwt.verify(token, 'nodeauthsecret', function(err, data){
          if(!err){
              db.changePassword(data.username,req.body.password)
              .then(resolve => {
                  return res.status(200).send({success: true, msg: 'Updated.'});
              })
              .catch(e => {
                  console.log(e)
                  return res.status(403).send({success: false, msg: 'Unauthorized.'})
              })
          }
      })
  } else {
      return res.status(403).send({success: false, msg: 'Unauthorized.'});
  }
});


router.post('/picture', passport.authenticate('jwt', { session: false}), function(req, res) {
  var token = getToken(req.headers);
  if (token) {
      db.getUserProfile(req.user.username)
      .then(resolve => {
          if(resolve.hasOwnProperty("pictureurl")){
              fs.readFile(resolve.pictureurl, function read(err, data) {
                  if (err) {
                      return res.status(404).send({picture: "Not found"})
                  }
                  resolve.picture = data.toString();
                  return res.status(200).send(resolve.picture)
              });
          }
          else{
              return res.status(404).send({picture: "Not found"})
          }
      })
      .catch(e => {
          console.log(e)
          return res.status(404).send({picture: "Not found"})
      })
  } else {
  return res.status(403).send({success: false, msg: 'Unauthorized.'});
  }
});

router.get('/landing', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token) {
        db.getRestaurantProfiles()
        .then(resolve => {
            for(var element in resolve){
                if(resolve[element].logourl){
                    var data = fs.readFileSync(resolve[element].logourl)
                    resolve[element].logo = data.toString();
                    delete resolve[element]["logourl"];
                }
            };
            return res.status(200).send(resolve);
        })
        .catch(e => {
            console.log(e);
            return res.status(403).send({success: false, msg: 'Unauthorized.'})
        })
    } else {
        return res.status(403).send({success: false, msg: 'Unauthorized.'});
    }
});

router.get('/restaurant/:id', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if(token) {
        console.log(req.params.id);
        db.getRestaurantItems(req.params.id)
        .then(resolve => {
            for(var element in resolve){
                if(resolve[element].photourl){
                    var data = fs.readFileSync(resolve[element].photourl)
                    resolve[element].photo = data.toString();
                    delete resolve[element]["photourl"];
                }
            };
            return res.status(200).send(resolve);
        })
        .catch(e => {
            console.log(e);
            return res.status(403).send({success: false, msg: 'Unauthorized.'})
        })
    }
    else {
        return res.status(403).send({success: false, msg: 'Unauthorized.'});
    }
});

router.post('/order', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if(token) {
        db.addOrderItem(req.body.orderid,req.body.itemid,req.body.quantity)
        .then(resolve => {
            return res.status(200).send({success: true, msg: 'Added to order.'});
        })
        .catch(e => {
            console.log(e)
            return res.status(403).send({success: false, msg: 'Unauthorized.'})
        })
    }
    else {
        return res.status(403).send({success: false, msg: 'Unauthorized.'});
    }
});

router.post('/createorder', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if(token) {
        db.createOrder(req.body.orderid, req.user.username, req.body.restname, req.body.lat, req.body.lon, req.body.deliveryname)
        .then(resolve => {
            return res.status(200).send({success: true, msg: 'Created.'});
        })
        .catch(e => {
            console.log(e)
            return res.status(403).send({success: false, msg: 'Unauthorized.'})
        })
    }
    else {
        return res.status(403).send({success: false, msg: 'Unauthorized.'});
    }
});

router.get('/lastorder', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if(token){
        db.getLastOrder()
        .then( resolve => {
            return res.status(200).send(resolve);
        })
        .catch( e => {
            console.log(e);
            return res.status(403).send({success: false, msg: 'Unauthorized.'});
        })
    }
    else {
        return res.status(403).send({success: false, msg: 'Unauthorized.'});
    }
});

getToken = function (headers) {
  if (headers && headers.authorization) {
      var parted = headers.authorization.split(' ');
      if (parted.length === 2) {
          return parted[1];
      } else {
          return null;
      }
  } else {
      return null;
  }
};

module.exports = router;
