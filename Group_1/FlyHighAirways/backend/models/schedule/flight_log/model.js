const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class FlightLog extends Sequelize.Model {
}

FlightLog.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    flightNo:{
        type: Sequelize.INTEGER
    },
    aircraftId:{
        type:Sequelize.INTEGER
    },
    source:{
        type:Sequelize.STRING
    },
    destination:{
        type:Sequelize.STRING
    },
    startDate:{
        type:Sequelize.DATEONLY
    },
    endDate:{
        type:Sequelize.DATEONLY
    },
    startTime:{
        type:Sequelize.TIME
    },
    endTime:{
        type:Sequelize.TIME
    }
}, {sequelize, underscored:true, timestamps:false});

// Associations

//export


module.exports = FlightLog;

