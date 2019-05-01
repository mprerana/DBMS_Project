const Sequelize = require('sequelize');
const sequelize = require('../../../utils/database/connect');

class User extends Sequelize.Model {
}

User.init({
    id: {
        type: Sequelize.INTEGER,
        autoIncrement: true,
        allowNull: false,
        primaryKey: true
    },
    email: {
        type: Sequelize.STRING,
        allowNull: false,
        validate: {
            isEmail: true
        }
    },
    password:{
        type:Sequelize.STRING,
        allowNull:false,
    },
    first_name:{
        type:Sequelize.STRING,
        allowNull:true
    },
    last_name:{
        type:Sequelize.STRING,
        allowNull:true
    },
    last_login:{
        type:Sequelize.DATE,
        allowNull:false,
    },
    has_password:{
        type:Sequelize.BOOLEAN,
        allowNull:false,
        defaultValue:true
    }
}, {sequelize, underscored:true});

// Associations

//export


module.exports = User;

