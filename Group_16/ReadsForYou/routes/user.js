const path = require('path');

const express = require('express');

const userController = require('../controllers/user');

const profileController = require('../controllers/profile');
const router = express.Router();


// when the user is not logged in
//router.get('/', userController.getBooks);


// when the user is logged in and is shown recommended books
router.get('/dashboard', userController.getBooks);


// find book by in url by ASIN
router.get('/books/:ASIN', userController.getIndex);

// fetch a particular book
router.get('/book', userController.getBook);
router.post('/book', userController.postBook);

// Profile 
//router.get('/profile', userController.getProfile);


// fetch the favorite book of the user
router.get('/favorites/:UserId', userController.getFavorites);

router.post('/delete/:UserId/:ASIN', userController.postDeleteFavorites);

// get details about a particular book
router.get('/detail/:ASIN', userController.getDetails);

router.post('/detail/:ASIN', userController.postDetails);

// logout
// router.get("/logout", userController.getLogout);

router.post('/favorites', userController.postFavorites);

//router.post('/book-details/:ASIN', userController.getDetails);

// router.post('/cart/delete-book', userController.postCartDeleteBook);


// using profile controller
router.get('profile/:UserId', profileController.getProfile);

module.exports = router;




//select B.ASIN, B.Filename, B.ImageURL, B.Title, B.Author, B.CategoryId, C.CategoryName
//from Books as B, Category as C where B.CategoryId = C.CategoryId and B.CategoryId = param


