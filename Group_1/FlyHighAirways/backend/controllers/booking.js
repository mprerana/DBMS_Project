const sequelize = require('../utils/database/connect');
const queryWrappers = require('../utils/query-wrappers');
const sequelizeErrors = require('../utils/sequelize-errors');
const parseError = require('../utils/parse-error');
const moment = require('moment');
const {validationResult} = require('express-validator/check');
const models = require('../models');


const validatePassengerDetails = async passenger => {
    const err = new Error("Validation Failed for passenger");
    err.statusCode = 422;

    if (typeof (passenger) != "object") {
        err.data = {"passenger": `Expected a passenger object but received ${typeof (passenger)}`};
        throw err
    }
    if (!(
        'fullName' in passenger &&
        'gender' in passenger &&
        'age' in passenger
    )) {
        err.data = {"passenger": "Insufficient details provided for some passenger"};
        throw err
    }


    passenger['age'] = parseInt(passenger['age']);

    if (isNaN(passenger['age']) || passenger['age'] < 0) {
        console.log(passenger['age']);
        err.data = {"age": "age not an integer or age less than 0"};
        throw err
    }

    if (['M', 'm', 'F', 'f', 'N', 'n'].indexOf(passenger['gender']) === -1) {
        console.log(passenger['gender']);
        err.data = {"passenger": "Only choices for gender are M, F, N"};
        throw err
    }
};

const validateAllPassengerDetails = async (passengers, next) => {
    console.log("validating!");
    if (passengers.length <= 0) {
        const err = new Error("Validation Failed!");
        err.statusCode = 422;
        err.data = {"passengers": "passenger list is empty!"};
        throw err
    }
    const promises = passengers.map(pass => validatePassengerDetails(pass));
    try {
        await Promise.all(promises)
    } catch (err) {
        throw err;
    }
};

exports.bookSeats = async (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        const err = new Error("Validation Failed!");
        err.statusCode = 422;
        err.data = errors.array();
        return next(err);
    }

    const {bookingNumber, passengerName, seat} = req.body;

    const booking = await models.bookings.FlightBooking.findOne({where: {id: bookingNumber}});
    if (!booking) {
        const err = new Error("Booking does not exist");
        err.statusCode = 422;
        return next(err);
    }
    // console.log(booking);
    for (let pass_in in booking.passengers) {

        if (booking.passengers[pass_in].fullName === passengerName) {
            console.log(booking.passengers[pass_in]);

            booking.passengers[pass_in].seat = seat;
            console.log(booking.passengers[pass_in]);
            console.log(booking.passengers)
            await models.bookings.FlightBooking.update({passengers: booking.passengers}, {where: {id: booking.id}});
            query = `insert into booked_seats(booking_id, seat_no, flight_no) values (${booking.id}, ${queryWrappers.wrapValue(seat)}, ${booking.flightNo})`;
            await sequelize.query(query);
            break
        }
    }

    return res.status(201).json({"booked": "Seat booked"})
};

exports.makePayment = async (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        const err = new Error("Validation Failed!");
        err.statusCode = 422;
        err.data = errors.array();
        return next(err);
    }

    const {referenceString, amount, remarks} = req.body;

    try {
        const paymentInstance = await models.others.Payment.create({
            referenceString: referenceString,
            amount: amount,
            remarks: remarks,
            userId: req.user.id
        })
    } catch (err) {
        err.statusCode = 422;
        return next(err)
    }

    return res.status(201).json({"status": "Payment made successfully"})

};

exports.bookFlight = async (req, res, next) => {

    const errors = validationResult(req);

    if (!errors.isEmpty()) {
        const err = new Error("Validation Failed!");
        err.statusCode = 422;
        err.data = errors.array();
        return next(err);
    }

    const {flightNumber, passengers, paymentReferenceKey, date} = req.body;

    try {
        await validateAllPassengerDetails(passengers, next);
    } catch (err) {
        return next(err)
    }

    const paymentInstance = await models.others.Payment.findOne({
        where: {
            referenceString: paymentReferenceKey.toString(),
            checked: false,
            refunded: false
        }
    })
    if (paymentInstance == null) {
        const err = new Error("No payment for for the booking. Booking cancelled!")
        err.statusCode = 422;
        return next(err);
    }
    const schedule = await models.schedule.Schedule.findByPk(flightNumber);
    console.log(schedule);
    if (schedule == null) {
        let err = new Error("No schedules found with given ID")
        err.statusCode = 422;
        return next(err)
    }

    // console.log(schedule.id);
    let flight = await models.schedule.UpcomingFlight.findOne({where: {schedule_id: schedule.id, start_date: date}});

    if (flight == null) {
        console.log(schedule.aircraft_id);
        flight = await models.schedule.UpcomingFlight.create({
            scheduleId: schedule.id,
            aircraftId: schedule.aircraftId,
            source: schedule.source,
            destination: schedule.destination,
            startDate: date,
            endDate: date,
            startTime: schedule.departure,
            endTime: schedule.arrival,
        });
        // console.log("flight null")
    }

    //passenger details
    const noOfPassengers = passengers.length;
    const modifiedPassengers = passengers.map(pass => {
        return {
            ...pass,
            "status": "confirmed",
            "seat": null
        }
    });

    const booking = await models.bookings.FlightBooking.create({
        booker: req.user.id,
        flightNo: flight.flightNo,
        amount: paymentInstance.amount,
        status: 'confirmed',
        passengers: modifiedPassengers,
        pnrNo: 'FH' + flight.flightNo.toString() + parseInt(new Date() * 1).toString()
    });
    // console.log(flight);

    paymentInstance.checked = true;
    await paymentInstance.save();
    return res.status(201).json({"status": "booking_confirmed", "passengers": booking.passengers})

};