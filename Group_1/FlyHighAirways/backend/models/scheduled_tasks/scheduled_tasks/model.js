const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');


class ScheduledTask extends Sequelize.Model {
}

ScheduledTask.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    name: {
        type: Sequelize.STRING,
        allowNull: false
    },
    active: {
        type: Sequelize.BOOLEAN,
        allowNull: false,
        defaultValue: true
    },
    startsOn: {
        type: Sequelize.DATE
    },
    repeatsIn: {
        type: Sequelize.STRING
    },
    nextRunOn: {
        type: Sequelize.DATE
    },
    procedure: {
        type: Sequelize.STRING
    }
}, { sequelize, underscored: true });

// Associations

//export


module.exports = ScheduledTask;

