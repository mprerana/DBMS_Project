const path = require('path');

const express = require('express');

// destrustured syntax of validator 
const { check, body } = require('express-validator/check');

const profileController = require('../controllers/profile');

const router = express.Router();

router.get('/profile/:UserId/:alert', profileController.getProfileerr);
router.get('/profile', profileController.getProfile);
router.post('/profile/:UserId', profileController.getEditProfile);
// router.post('/edit-profile', profileController.postEditProfile);


router.post('/edit-profile', 
           [
            check('Email')
            .isEmail()
            .withMessage('Please enter a valid Email!')
               .normalizeEmail()               
            //We Can make own custom validator for specific task
            .custom((value, {req}) => {
                if(value === 'test@gmail.com') {
                    throw new Error('This email address is Forbidden!');
                 }
                 return true;
             }),
             body('FirstName', 'Please enter a string').isString().trim(),
             body('LastName', 'Please enter a string').isString().trim(),
            
            

            ], 
        profileController.postEditProfile);

module.exports = router;
