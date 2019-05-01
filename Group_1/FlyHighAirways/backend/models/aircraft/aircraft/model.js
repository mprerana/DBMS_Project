const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class Aircraft extends Sequelize.Model {
}

Aircraft.init({
    modelId: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    noOfAircrafts:{
        type: Sequelize.INTEGER,
        allowNull: false
    },
    dateOfPurchase:{
        type: Sequelize.DATE
    }
}, {sequelize, underscored:true, tableName:'aircrafts', timestamps:false});

// Associations

//export


module.exports = Aircraft;

