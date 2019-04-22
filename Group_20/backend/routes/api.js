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


router.post('/signup', function(req, res) {
    if (!req.body.username || !req.body.password || !req.body.email) {
      return res.status(400).send({msg: 'Incomplete details.'})
    } else {
        db.insertUser(req.body.username,req.body.password,req.body.email)
            .then((user) =>{
                var token = crypto.createHash('md5').update(req.body.username).digest('hex')
                db.insertNewToken(req.body.username,token,'a')
                .then( () => {
                    var transporter = nodemailer.createTransport({
                        host: "smtp.gmail.com",
                        port: 587,
                        secure: false, // true for 465, false for other ports
                        auth: {
                            user: 'thewatercomp@gmail.com', // generated ethereal user
                            pass: 'wat3r123' // generated ethereal password
                            }
                    });
                    var mailOptions = { from: 'no-reply@yourwebapplication.com', to: req.body.email, subject: 'Account Verification Token', text: 'Hello,\n\n' + 'Please verify your account by clicking the link: ' + req.headers.origin + '\/confirmation\/' + token + '.\n' };
                    // transporter.sendMail(mailOptions, function (err) {
                    //     if (err) { return res.status(500).send({ msg: err.message }); }
                    // });
                    return res.json(JSON.parse('{"success": true}'));
                })
                .catch((error) => {
                    console.log(error);
                    return res.status(400).send(error);
                });
                
            })
            .catch((error) => {
                console.log(error);
                 return res.status(400).send(error);
            });
    }
});

router.post('/iforgot', function(req, res) {
    if (!req.body.email) {
      res.status(400).send({msg: 'Incomplete details.'})
    } else {
        db.getUserByEmail(req.body.email)
        .then( (user) => {
            if(user){
                var token = crypto.createHash('md5').update(user.username).digest('hex')
                db.insertNewToken(user.username,token,'p')
                .then( () => {
                    var transporter = nodemailer.createTransport({
                        host: "smtp.gmail.com",
                        port: 587,
                        secure: false, // true for 465, false for other ports
                        auth: {
                            user: 'thewatercomp@gmail.com', // generated ethereal user
                            pass: 'wat3r123' // generated ethereal password
                            }
                    });
                    var mailOptions = { from: 'no-reply@yourwebapplication.com', to: req.body.email, subject: 'Forgot Password Token', text: 'Hello,\n\n' + 'Please log in and change your password by clicking the link: ' + req.headers.origin + '\/confirmation\/' + token + '.\n' };
                    transporter.sendMail(mailOptions, function (err) {
                        if (err) { return res.status(500).send({ msg: err.message }); }
                    });
                    res.json(JSON.parse('{"success": true}'));
                    setTimeout( () => db.deleteToken(user.username), 60000)
                })
                .catch((error) => {
                    console.log(error);
                    return res.status(400).send(error);
                });
            } else {
                return res.json(JSON.parse('{"success": true}'));
            }
        })
    }
});

router.post('/confirm', function(req, res) {
    db.verifyToken(req.body.token)
        .then((newUser) => {
            if (!newUser) {
                return res.status(401).send({
                message: 'Authentication failed. User not found.',
                });
            }
            db.getUser(newUser.username)
            .then((user) => {
                if (!user) {
                    return res.status(401).send({
                    message: 'Authentication failed. User not found.',
                    });
                }
                db.setActive(newUser.username)
                    .catch((error) => res.status(400).send(error));
                db.deleteToken(newUser.username)
                    .catch((error) => res.status(400).send(error));
                var token = jwt.sign(JSON.parse(JSON.stringify(user)), 'nodeauthsecret', {expiresIn: 86400 * 30});
                jwt.verify(token, 'nodeauthsecret', function(err, data){
                    //console.log(err, data);
                })
                return res.json(JSON.parse('{"success": true, "token": "JWT ' + token + '", ' + JSON.stringify(user).slice(1)));
            })
            .catch((error) =>{
                console.log(error)
                return res.status(400).send(error)
            });      
        })
        .catch((error) =>{
            console.log(error)
            return res.status(400).send(error)
        });      
});

router.post('/signin', function(req, res) {
    db.getVerifiedUser(req.body.username)
        .then((user) => {
            if (!user) {
                return res.status(401).send({
                message: 'Authentication failed. User not found.',
                });
            }
            db.comparePassword(user,req.body.password, (err, isMatch) => {
                if(isMatch && !err) {
                    var token = jwt.sign(JSON.parse(JSON.stringify(user)), 'nodeauthsecret', {expiresIn: 86400 * 30});
                    jwt.verify(token, 'nodeauthsecret', function(err, data){
                        //console.log(err, data);
                    })
                    return res.json(JSON.parse('{"success": true, "token": "JWT ' + token + '", ' + JSON.stringify(user).slice(1)));
                } else {
                    return res.status(401).send({success: false, msg: 'Authentication failed. Wrong password.'});
                }
            })
        })
        .catch((error) => res.status(400).send(error));
});

router.post('/username', function(req, res) {
    db.getUser(req.body.username)
    .then(resolve => {
        return res.status(200).send(resolve === undefined)
    })
    .catch(e => {
        console.log(e)
        return res.status(404).send({message: "Server down."})
    })
});

router.post('/email', function(req, res) {
    db.getUserByEmail(req.body.email)
    .then((resolve1) => {
        db.getRestaurantApplicationByEmail(req.body.email)
        .then(resolve => {
            return res.status(200).send(resolve1 === undefined && resolve === undefined)
        })
        .catch(e => {
            console.log(e)
            return res.status(404).send({message: "Server down."})
        })
    })
    .catch(e => {
        console.log(e)
        return res.status(404).send({message: "Server down."})
    })
});

router.post('/restaurant/signup', function(req, res) {
    if (!req.body.name || !req.body.email || !req.body.lon || !req.body.lat || !req.body.address || !req.body.zipcode || !req.body.phone || !req.body.openingHrs || !req.body.closingHrs || !req.body.logo) {
      return res.status(400).send({msg: 'Incomplete details.'})
    } else {
        var logourl = __dirname + "/../models/logos/" + crypto.createHash('md5').update(req.body.email).digest('hex');
        fs.writeFile(logourl, req.body.logo, function(err) {
            if(err) {
                return res.status(403).send({success: false, msg: 'Unauthorized.'})
            }
        });
        db.restaurantApply(req.body.name, req.body.email, req.body.lon, req.body.lat, req.body.address, req.body.zipcode, req.body.phone, req.body.openingHrs, req.body.closingHrs, logourl)
        .then( (done) => {
            if(done){
                return res.json(JSON.parse('{"success": true}'));
            }
            else{
                console.log(done)
                return res.status(400).send(done);
            }
        })
        .catch((error) => {
            console.log(error);
            return res.status(400).send(error);
        });
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