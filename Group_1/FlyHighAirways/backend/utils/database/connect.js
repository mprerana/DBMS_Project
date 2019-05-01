const Sequelize = require('sequelize');
const sequelize = new Sequelize('flyhigh', 'admin', 'minda', {
    host: 'localhost',
    dialect: 'postgres',
    port: 15000,
    logging: false
});

module.exports = sequelize;
