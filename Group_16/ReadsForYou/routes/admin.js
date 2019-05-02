const path = require('path');
const express = require('express');

const { check, body } = require('express-validator/check');
const { sanitize } = require('express-validator/filter');

const adminController = require('../controllers/admin');

const router = express.Router();

router.get('/add-book',
[
    body('ASIN')
        .isISBN()
        .isLength({min: 10, max: 10}),
    body('FileName')
        .isString().trim(),
    sanitize('.*jpg || png || jpeg'),
    
    body('ImageURL')
        .isURL(),
    body('Title')
        .isAlphanumeric()
        .isLength({min: 3})
        .trim(), 
    //  body('Price')
    //     .isFloat()
    //     .isLength({min:0}),
     body('Description')
        .isLength({min:5, max: 400})
        .trim(),
], adminController.getAddBook);

// router.get('/books', adminController.getBooks);

router.post('/add-book', adminController.postAddBook);

router.get('/edit-book/', adminController.getEditBook);

router.post('/edit-book', 
[
    body('ASIN')
        .isISBN()
        .isLength({min: 10, max: 10}),
    body('FileName')
        .isString()
        .trim(),
    sanitize('.*jpg || png || jpeg'),
    
    body('ImageURL')
        .isURL(),
    body('Title')
        .isAlphanumeric()
        .isLength({min: 3})
        .trim(), 
    // body('Price')
    //     .isFloat()
    //         .isLength({min:0}),
    body('Description')
        .isLength({min:5, max: 400})
        .trim(),
], adminController.postEditBook);

// router.post('/delete-book', adminController.postDeleteBook);

module.exports = router;
