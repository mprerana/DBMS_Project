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

router.post('/addCategory', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token) {
        if (req.user.role === '3'){
            db.getRestaurantCategory(req.user.username, req.body.catName)
            .then(resolve => {
                if(resolve === undefined){
                    db.addRestaurantCategory(req.user.username, req.body.catName)
                    .then(() => {
                        return res.status(200).send({success: true, msg: 'Updated.'})
                    })
                    .catch(e => {
                        console.log(e)
                        return res.status(403).send({success: false, msg: e})
                    })
                }
                else{
                    return res.status(200).send(false)
                }
            })
        }
    } else{
        return res.status(200).send({success: false, msg: 'Unauthorized'})
    }
        
});

router.get('/categories', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token) {
        if (req.user.role === '3'){
            db.getRestaurantCategories(req.user.username)
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

router.post('/addItem', passport.authenticate('jwt', { session: false}), function(req, res) {
    var token = getToken(req.headers);
    if (token) {
        if (req.user.role === '3'){
            db.getRestaurantItem(req.user.username, req.body.itemName)
            .then(resolve => {
                if(resolve === undefined){
                    const pictureurl = __dirname + "/../models/items/" + crypto.createHash('md5').update(req.user.id.toString() + req.body.itemName).digest('hex');
                    fs.writeFile(pictureurl, req.body.photo, function(err) {
                        if(err) {
                            return res.status(403).send({success: false, msg: 'Unauthorized.'})
                        }
                    });
                    db.addRestaurantItem(req.user.username, req.body.itemName, req.body.price, req.body.desc, req.body.categoryID,pictureurl)
                    .then(() => {
                        return res.status(200).send({success: true, msg: 'Updated.'})
                    })
                    .catch(e => {
                        console.log(e)
                        return res.status(403).send({success: false, msg: e})
                    })
                }
                else{
                    return res.status(200).send(false)
                }
            })
        }
    } else{
        return res.status(200).send({success: false, msg: 'Unauthorized'})
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
