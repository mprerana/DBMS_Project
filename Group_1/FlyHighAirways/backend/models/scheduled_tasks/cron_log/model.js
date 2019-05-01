const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');


class CronLog extends Sequelize.Model {
}

CronLog.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    started_on: {
        type: Sequelize.DATE,
        allowNull: false
    },
    total: {
        type: Sequelize.INTEGER,
        allowNull: false,
        defaultValue: 0
    },
    errored: {
        type: Sequelize.INTEGER,
        allowNull: false,
        defaultValue: 0
    }
}, { sequelize, underscored: true });

// Associations

//export


module.exports = CronLog;

