const sequelize = require('../utils/database/connect');
const queryWrappers = require('../utils/query-wrappers');
const sequelizeErrors = require('../utils/sequelize-errors');
const parseError = require('../utils/parse-error');
const {validationResult} = require('express-validator/check');
const Schedule = require("../models/schedule/schedule")
const City = require("../models/others/city/model.js")
const models = require('../models');


exports.getAllFlights = (req, res, next) => {
    Schedule.findAll().then(flights => {
            newFlights = flights.map(obj => {
                return {
                    id: obj.id,
                    start_time: obj.departure,
                    end_time: obj.end_time,
                    source: obj.source,
                    destination: obj.destination,
                    economy: {
                        fare: obj.price,
                        seats_remaining: 15
                    }
                }
            });
            return res.status(200).json({flights: newFlights});
        }
    )
        .catch(err => {
                // console.log(err);
                return next(err)
            }
        );
}

exports.getFlightsBySourceAndDestination = (req, res, next) => {
    const source = req.bodyValidator.source;
    const destination = req.bodyValidator.destination;
    Schedule.findAll({where: {source: source, destination: destination}})
        .then(flights => {
            return res.status(200).json({flights: flights})
        })
        .catch(err => {
                // console.log(err);
                return next(err)
            }
        );
}

exports.getAllCities = (req, res, next) => {
    City.findAll()
        .then(cities => {
            return res.status(200).json({cities: cities})
        })
        .catch(err => {
                // console.log(err);
                return next(err)
            }
        );
}

exports.getBookingsByUser = (req, res, next) => {
    const userID = req.user.id;
    BookedFlights = models.bookings.FlightBooking
    BookedFlights.findAll({where: {id: userID}})
        .then(bookedFlights => {
            return res.status(200).json({bookedFlights: bookedFlights})
        })
        .catch(err => {
                // console.log(err);
                return next(err)
            }
        );
};
exports.getSeats = async (req, res, next) => {
    const errors = validationResult(req);

    if (!errors.isEmpty()) {
        const err = new Error("Validation Failed!");
        err.statusCode = 422;
        err.data = errors.array();
        return next(err);
    }

    const {flightNo} = req.body;

    query = `select * from booked_seats where flight_no=${flightNo}`;
    const seats = await sequelize.query(query);
    let onlySeats = seats[0].map(obj => obj.seat_no);
    console.log(onlySeats)

    const retSeatList = [];
    for (let row of ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) {
        for (let no of [1, 2, 3, 4, 5, 6]) {
            let curSeat = row.toString() + no.toString()
            if (onlySeats.indexOf(curSeat) !== -1) {
                retSeatList.push({seat_no: curSeat, is_booked: true, special:(no===1 || no===6)})
            } else {
                retSeatList.push({seat_no: curSeat, is_booked: false, special:(no===1 || no===6)})

            }
        }
    }

    return res.status(200).json({"seats": retSeatList});
};
