const express = require('express');
const {body: bodyValidator} = require('express-validator/check');
const router = express.Router();
const authMiddleWare = require('../middlewares/auth');
const {booking: bookingControllers} = require('../controllers');

// POST /booking/make-payment
router.post(
  '/make-payment',
  [
      bodyValidator('referenceString').not().isEmpty().isString(),
      bodyValidator('amount').not().isEmpty().isFloat(),

  ],
  authMiddleWare, bookingControllers.makePayment
);
// POST /booking/book-flight
router.post(
    '/book-flight',
    [
        bodyValidator('flightNumber').not().isEmpty().withMessage("Missing parameter flightNumber"),
        bodyValidator('passengers').not().isEmpty().withMessage("Missing parameter passengers").isArray().withMessage('Expected an array of passenger detail objects'),
        bodyValidator('paymentReferenceKey').not().isEmpty().withMessage("Missing parameter paymentReferenceKey"),
        bodyValidator('date').not().isEmpty().withMessage("Missing parameter date (js date object)")
    ],
    authMiddleWare,bookingControllers.bookFlight
);

router.post(
    '/book-seat',
    [
        bodyValidator('bookingNumber').not().isEmpty(),
        bodyValidator('passengerName').not().isEmpty().isString(),
        bodyValidator('seat').not().isEmpty().isString()
    ],
    authMiddleWare, bookingControllers.bookSeats
);
module.exports = router;

