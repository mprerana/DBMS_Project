const express = require('express');
const {body: bodyValidator} = require('express-validator/check');
const authMiddleWare = require('../middlewares/auth');
const router = express.Router();
const {auth: authControllers} = require('../controllers');

// POST /auth/register
router.post(
    '/register',
    [
        bodyValidator('email').isEmail().withMessage('Not A valid email').normalizeEmail(),
        bodyValidator('password').isLength({min: 8}).withMessage('Password must be at least 8 characters long'),
    ],
    authControllers.register
);

router.post(
    '/login',
    [
      bodyValidator('email').not().isEmpty(),
      bodyValidator('password').not().isEmpty()
    ],
    authControllers.login);

router.post(
    '/refresh',
    [
      bodyValidator('token').not().isEmpty()
    ],
    authControllers.refresh);
module.exports = router;