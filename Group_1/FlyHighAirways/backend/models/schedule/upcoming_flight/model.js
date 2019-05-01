const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class UpcomingFlight extends Sequelize.Model {
}

UpcomingFlight.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    scheduleId:{
        type:Sequelize.INTEGER
    },
    flightNo:{
        type:Sequelize.INTEGER
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
    },
    price:{
        type:Sequelize.INTEGER
    },
    pilot:{
        type:Sequelize.ARRAY(Sequelize.INTEGER)
    },
    crew:{
        type:Sequelize.ARRAY(Sequelize.INTEGER)
    }
}, {sequelize, underscored:true, timestamps:false});

// Associations

//export


module.exports = UpcomingFlight;

