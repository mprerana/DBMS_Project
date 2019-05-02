var createError = require('http-errors');
var express = require('express');
var path = require('path');


const cookieParser = require('cookie-parser');
const logger = require('morgan');

const indexRouter = require('./routes/index');
const usersRouter = require('./routes/user');
const accountRouter = require('./routes/account');
const itemRouter = require('./routes/item');
const purchaseRouter = require('./routes/purchase');
const rateRouter = require('./routes/rate');
const receiptRouter = require('./routes/receipt');
const mcollectRouter = require('./routes/mcollect');
const msalesRouter = require('./routes/msales');

const app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/account',accountRouter);
app.use('/item',itemRouter);
app.use('/purchase',purchaseRouter);
app.use('/rate',rateRouter);
app.use('/receipt',receiptRouter);
app.use('/mcollect',mcollectRouter);
app.use('/msales',msalesRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // Check if develpment is on or not
  console.log('Current Environmet is:'+req.app.get('env'));


  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
