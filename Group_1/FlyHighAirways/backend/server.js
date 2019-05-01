/* package imports */
const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

/* constants */
const port = 5000;
const app = express();
const routes = require('./routes');
/* Middleware */
app.use(bodyParser.json());

app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET, POST, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

/* Routes */

app.use((req, res, next) => {
    console.log(req.path);
    next();
});

app.use('/auth', routes.auth);

app.use('/flights',routes.flights);
app.use('/book', routes.booking);

/* error Route */
app.use((error, req, res, next) => {
    console.log(error);
    let {statusCode, message, data} = error;
    if (!statusCode) statusCode = 500;

    if (statusCode === 500) {
        message = "Internal Error! Please try again later!";
        data = {};
    }
    res.status(statusCode).json({message: message, data: data});
});

/* start server */
console.log("listning on port", port);
app.listen(port);
