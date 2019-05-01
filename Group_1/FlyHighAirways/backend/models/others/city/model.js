const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class City extends Sequelize.Model {
}

City.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,

    },
    name: {
        type: Sequelize.STRING,
        primaryKey:true
    },
    short_form: {
        type: Sequelize.STRING
    }
}, {sequelize, underscored: true, timestamps:false});

// Associations

//export


module.exports = City;

