const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class AircraftModel extends Sequelize.Model {
}

AircraftModel.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    manufacturerName:{
        type: Sequelize.STRING,
    },
    modelName:{
        type: Sequelize.STRING,

    },
    noOfSeats:{
        type: Sequelize.INTEGER
    },
    name:{
        type: Sequelize.STRING
    },
    maxWeight:{
        type: Sequelize.FLOAT
    },
    manufacturedDate:{
        type:Sequelize.DATE
    },
    maintenanceDate:{
        type: Sequelize.DATE
    }
}, {sequelize, underscored:true, timestamps:false});

// Associations

//export


module.exports = AircraftModel;

