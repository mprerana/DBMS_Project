const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const sequelize = require('../utils/database/connect');
const queryWrappers = require('../utils/query-wrappers');
const sequelizeErrors = require('../utils/sequelize-errors');
const parseError = require('../utils/parse-error');
const {validationResult} = require('express-validator/check');

const {auth: {User, OutstandingToken}} = require('../models');

const serverSecret = require('../utils/server-secret');

exports.register = async (req, res, next) => {
    console.log("here");
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        const err = new Error("Validation Failed!");
        err.statusCode = 422;
        err.data = errors.array();
        next(err);
    }

    const {email, password, first_name, last_name} = req.body;
    const tableName = User.getTableName();

    let hashedPassword;

    try {
        hashedPassword = await bcrypt.hash(password, 9);
    } catch (err) {
        next(err);
    }

    const wrappedValues = queryWrappers.wrapAllValues({
        email: email, password: hashedPassword, first_name: first_name,
        last_name: last_name
    });

    const query = `INSERT INTO ${tableName} ("email","password","first_name","last_name")
                    VALUES (${wrappedValues.email} , 
                            ${wrappedValues.password} , 
                            ${wrappedValues.first_name} , 
                            ${wrappedValues.last_name}
                            )
                   `;

    console.log(query);

    sequelize.query(query).then(([result, metaData]) => {
        res.status(201).json({message: "User Created"});
    }).catch(err => {

        const data = sequelizeErrors(err);
        const message = "Invalid Data!";
        const error = new Error();
        error.statusCode = 422;
        error.message = message;
        error.data = parseError(data);
        next(error);
    });


};

exports.login = async (req, res, next) => {
    try {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            const err = new Error("Validation Failed!");
            err.statusCode = 422;
            err.data = errors.array();
            throw err;
        }
        const {email, password} = req.body;

        let query = `select * from ${User.getTableName()} where "email"=${queryWrappers.wrapValue(email)}`;

        const users = await sequelize.query(query, {type: sequelize.QueryTypes.SELECT, model: User});

        if (users.length <= 0) {
            const error = new Error("The given email does not exist!");
            error.statusCode = 401;
            throw error;
        }
        const user = users[0];

        console.log(password, user.password);
        const isPasswordEqual = await bcrypt.compare(password, user.password);
        console.log(isPasswordEqual);
        if (!isPasswordEqual) {
            const error = new Error("Incorrect Password!");
            error.statusCode = 401;
            throw error;
        }

        const accessToken = jwt.sign({
            email: user.email,
            type: "access",
            keywoard: "Bearer"
        }, serverSecret, {expiresIn: 60 * 60*24*5});


        const outstandingRefreshToken = parseInt(new Date() * user.id / 100000000);

        const refreshToken = jwt.sign({
            email: user.email,
            type: "refresh",
            outstandingToken: outstandingRefreshToken
        }, serverSecret, {expiresIn: 60 * 60 * 24 * 30});

        const refreshTokenExpiryDate = new Date(new Date() * 1 + (1000 * 60 * 60 * 24 * 30));

        // add outstanding token in db
        // keep async to end response faster
        const WrappedExpiryDate = queryWrappers.wrapValue(refreshTokenExpiryDate.toISOString());
        query = `INSERT INTO ${OutstandingToken.getTableName()} 
                ("user_id","token", "expires_on") 
                VALUES (${user.id},${outstandingRefreshToken},${WrappedExpiryDate} )
                `;

        query2 = `
                    UPDATE ${OutstandingToken.getTableName()}
                    SET is_valid = TRUE
                    WHERE "token" = ${outstandingRefreshToken}
                 `;

        sequelize.query(query).then(([result, meta]) => {
            console.log("created new outstanding token");
        }).catch(err => {
            sequelize.query(query2).then(([result,meta])=>{
                console.log("updated existing outstanding token");
            }).catch(err=>{
                console.log(err);
            });
        });
        res.status(200).json({tokens: {access: accessToken, refresh: refreshToken, email:user.email}})
    } catch (err) {
        next(err);
    }
};

exports.refresh = async (req,res,next) => {
    try {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            const err = new Error("Validation Failed!");
            err.statusCode = 422;
            err.data = errors.array();
            throw err;
        }
        const {token} = req.body;

        let decodedToken;
        try {
            decodedToken = jwt.verify(token, serverSecret);
        }catch(err){
            err.statusCode = 401;
            err.data = {"token":"invalid token"};
            throw err;
        }

        const decodedOutstandingToken = decodedToken.outstandingToken;
        const wrapedDecodedEmail = queryWrappers.wrapValue(decodedToken.email);

        const user_table = User.getTableName();
        const ot_table = OutstandingToken.getTableName();
        const query = `
                        SELECT is_valid, "token", user_id FROM ${ot_table}
                        INNER JOIN ${user_table}
                        ON ${user_table}.id = ${ot_table}.user_id
                        WHERE "email"=${wrapedDecodedEmail} AND 
                              "token"=${decodedOutstandingToken} AND
                              "is_valid"=TRUE AND
                              "expires_on" > NOW() 
                    `;

        const ot_instances = await sequelize.query(query, {type:sequelize.QueryTypes.SELECT, model: OutstandingToken});

        if (ot_instances.length <= 0){
            // invalid for refresh token
            const err = new Error("this refresh token is either invalid, expired or revoked!");
            err.statusCode = 422;
            err.data = errors.array();
            throw err;
        }

        // valid to refresh token. generate new access token and send

        let user = await User.findByPk(ot_instances[0].dataValues.user_id);
        const newAccessToken = jwt.sign({
            email: user.email,
            type: "access",
            keywoard: "Bearer"
        }, serverSecret, {expiresIn: 60 * 15});

        res.status(200).json({tokens: {access: newAccessToken}})
    } catch (err) {
        next(err);
    }
};
