const express = require('express');
const {body: bodyValidator} = require('express-validator/check');
const router = express.Router();
const flightControllers = require('../controllers/flights')
const authMiddleWare = require('../middlewares/auth');

router.post(
    '/get_all_flights',
    [
        bodyValidator('flights').not().isEmpty(),
    ],
    flightControllers.getAllFlights
);

router.post(
    '/get_flights_by_source_and_destination',
    [
        bodyValidator('flights').not().isEmpty(),
        bodyValidator('source').not().isEmpty(),
        bodyValidator('destination').not().isEmpty(),
    ],
    flightControllers.getFlightsBySourceAndDestination
);

router.post(
    '/get_all_cities',
    [
        bodyValidator('cities').not().isEmpty(),
    ],
    flightControllers.getAllCities
);

router.post(
    '/get_bookings_by_user',
    [
        bodyValidator('id').not().isEmpty(),
    ],

    authMiddleWare, flightControllers.getBookingsByUser
);


router.post(
    '/get_seats',
    [
        bodyValidator('flightNo').not().isEmpty(),
    ],
    flightControllers.getSeats
);


module.exports = router;