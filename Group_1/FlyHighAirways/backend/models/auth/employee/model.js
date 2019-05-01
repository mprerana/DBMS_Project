const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class Employee extends Sequelize.Model {
}

Employee.init({
    employeeId: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    occupation:{
        type: Sequelize.STRING,
        allowNull:true
    },

}, {sequelize, underscored:true, timestamps:false});

// Associations
Employee.belongsTo(Employee, {foreignKey:'supervisor'});
Employee.hasMany(Employee, {foreignKey:'supervisor'});
//export


module.exports = Employee;

