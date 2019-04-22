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

router.get('/restaurant-applications', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token) {
        if (req.user.role === '2'){
            db.getRestaurantApplications()
                .then(resolve => {
                    return res.status(200).send(resolve)
                })
                .catch(e => {
                    console.log(e)
                    return res.status(403).send({success: false, msg: e})
                })
        }
    } else{
        return res.status(200).send({success: false, msg: 'Unauthorized'})
    }
        
});

router.get('/restaurant-application/:id', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token) {
        if (req.user.role === '2'){
            db.getRestaurantApplicationByID(req.params.id)
                .then(resolve => {
                    fs.readFile(resolve.logourl, function read(err, data) {
                        if (err) {
                            return res.status(403).send({success: false, msg: 'Unauthorized.'})
                        }
                        resolve.logo = data.toString();
                        delete resolve["logourl"]
                        return res.status(200).send(resolve)
                    });
                })
                .catch(e => {
                    console.log(e)
                    return res.status(403).send({success: false, msg: e})
                })
        }
    } else{
        return res.status(200).send({success: false, msg: 'Unauthorized'})
    }
        
});

router.get('/users', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token && req.user.role === '2') {
        db.getUsers()
        .then(resolve => {
            return res.status(200).send(resolve)
        })
        .catch(e => {
            console.log(e)
            return res.status(403).send({success: false, msg: 'Unauthorized.'})
        })
    } else {
        return res.status(403).send({success: false, msg: 'Unauthorized.'});
    }
});

router.post('/restaurantApplication', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token && req.user.role === '2') {
        db.updateRestaurantApplication(req.body.email, req.body.status)
        .then(resolve => {
            var token = crypto.createHash('md5').update('restaurant' + resolve.id).digest('hex')
            db.insertNewToken('restaurant' + resolve.id,token,'a')
            .then( () => {
                if(req.body.status = 'A'){
                    var transporter = nodemailer.createTransport({
                        host: "smtp.gmail.com",
                        port: 587,
                        secure: false, // true for 465, false for other ports
                        auth: {
                            user: 'thewatercomp@gmail.com', // generated ethereal user
                            pass: 'wat3r123' // generated ethereal password
                            }
                    });
                    var mailOptions = { from: 'no-reply@yourwebapplication.com', to: req.body.email, subject: 'Account Verification Token', text: 'Hello,\n\n' + 'Please verify your restaurant\'s account by clicking the link: ' + req.headers.origin + '\/confirmation\/' + token + '.\n' };
                    transporter.sendMail(mailOptions, function (err) {
                        if (err) { return res.status(500).send({ msg: err.message }); }
                    });
                }
                return res.json(JSON.parse('{"success": true}'));
            })
            .catch((error) => {
                console.log(error);
                return res.status(400).send(error);
            });
        })
        .catch(e => {
            console.log(e)
            return res.status(403).send({success: false, msg: 'Unauthorized.'})
        })
    } else {
        return res.status(404).send({success: false, msg: 'Unauthorized.'});
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
