const jwt = require('jsonwebtoken');
const serverSecret = require('../utils/server-secret');
const queryWrappers = require('../utils/query-wrappers');
const {auth:{User}} = require('../models/');
const sequelize = require('../utils/database/connect');

module.exports = async (req,res,next)=>{
    // try {
    //     let authHeader = req.get('Authorization');
    //     if(!authHeader){
    //         const err = new Error("Not Authenticated!");
    //         err.statusCode = 401;
    //         throw err;
    //     }
    //     console.log(authHeader);
    //     authHeader = authHeader.split(' ');
    //
    //     if (authHeader[0] !== "Bearer") {
    //         const err = new Error("Only Bearer tokens are supported. Please included keyword 'Bearer' before token")
    //         err.statusCode = 401;
    //         throw err;
    //     }
    //
    //     const token = authHeader[1];
    //
    //     let decodedToken;
    //     try {
    //         decodedToken = jwt.verify(token, serverSecret);
    //     }catch(err){
    //         err.statusCode = 401;
    //         err.data = {"token":"invalid token"};
    //         throw err;
    //     }
    //
    //     if (decodedToken.type!=="access"){
    //         const err = new Error("Invalid token type!");
    //         err.data = {"token":"Expected access type for token"};
    //         err.statusCode = 401;
    //         throw err;
    //     }
    //
    //     // token is valid. now get and attach user
    //
    //     query = `select * from ${User.getTableName()} where "email"=${queryWrappers.wrapValue(decodedToken.email)}`;
    //
    //
    //     if (users.length <= 0) {
    //         const error = new Error("This user does not exist!");
    //         error.statusCode = 401;
    //         throw error;
    //     }
    //
    //
    // }catch(err){
    //     next(err);
    // }
        query = `select * from ${User.getTableName()}`;

        const users = await sequelize.query(query, {type: sequelize.QueryTypes.SELECT, model: User});
        req.user = users[0];
        next();

};