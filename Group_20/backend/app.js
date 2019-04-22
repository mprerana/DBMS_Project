var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors')

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/user');
var apiRouter = require('./routes/api');
var adminRouter = require('./routes/admin');
var restoRouter = require('./routes/restaurant');

var app = express();



const db = require('./models/database');
db.setup()
//db.insertUserProfile('hanimo','email@','firstname','lastname','phone','address');
//db.deleteUser('hanimo')
// db.insertUser('hani','password','hani.mohammed.3@gmail.com','2')
// db.getUsers()
//   .then(resolve => {
//     console.log(resolve)
//   })
//   .catch(e => console.log(e));

// db.updateUserProfile('email',{
//   lastname:'mohammed',
//   firstname:'hani',
//   phone: '+919840794287'
// })
// db.deleteUserProfile('hani')

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(cors({credentials: true, origin: true}))
app.use(logger('dev'));
app.use(express.json({limit: '50mb'}));
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/user', usersRouter);
app.use('/admin', adminRouter);
app.use('/restaurant', restoRouter);
app.use('/api', apiRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
