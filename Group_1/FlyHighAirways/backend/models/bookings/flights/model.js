const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class FlightBooking extends Sequelize.Model {
}

FlightBooking.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    booker:{
      type:Sequelize.STRING,
    },
    pnrNo:{
      type: Sequelize.INTEGER,
      // autoIncrement:true,
      allowNull:false
    },
    flightNo:{
        type:Sequelize.INTEGER
    },
    passengers:{
        type:Sequelize.JSON
        /* json is array of objects of type:
        *   {
        *       fullname, gender, age, status, seat:{row,number}
        * */
    },
    amount:{
        type:Sequelize.INTEGER
    },
    status:{
        type:Sequelize.STRING
    },
    bookedOn:{
        type:Sequelize.DATE
    },
}, {sequelize, underscored:true, timestamps:false});

// Associations

//export


module.exports = FlightBooking;

