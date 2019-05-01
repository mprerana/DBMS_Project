const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class Payment extends Sequelize.Model {
}

Payment.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    referenceString: {
        type: Sequelize.STRING
    },
    userId: {
        type: Sequelize.INTEGER
    },
    amount:{
        type:Sequelize.DOUBLE
    },
    checked:{
        type:Sequelize.BOOLEAN
    },
    refunded:{
        type:Sequelize.BOOLEAN
    },
    timestamp:{
        type:Sequelize.DATE
    },
    remarks:{
        type:Sequelize.STRING
    }
}, {sequelize, underscored: true, timestamps:false});

// Associations

//export


module.exports = Payment;

