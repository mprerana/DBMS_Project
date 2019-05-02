const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const config = require('../config/secret');
const models = require("../models")

module.exports = function (models) {
  const router = express.Router();

  router.post('/register', (req, res) => {
    var hashedPassword = bcrypt.hashSync(req.body.password, 8);
    models.User.create({
      username: req.body.username,
      name: req.body.name,
      email: req.body.email,
      age: req.body.age,
      isTeacher: req.body.isTeacher,
      password: hashedPassword
    }).then((user) => {

      //create a token
      console.log(user);
      var token = jwt.sign({ id: user.userid }, config.secret, {
        expiresIn: 86400 //expired in 24 hours
      });

      res.status(200).send({ auth: true, token: token });
    }).catch((err) => {
      console.log(err);
      return res.status(500).send("There was a problem registering the user");
    });
  });

  router.get('/me', (req, res) => {

    var token = req.get('x-access-token');
    if (!token)
      return res.status(401).send({ auth: false, message: 'No token provided' });

    jwt.verify(token, config.secret, (err, decoded) => {
      if (err) {
        console.log(err);
        return res.status(500).send({ auth: false, message: 'Failed to authenticate token' });
      }


      // User.findById(decoded.id, function (err, user) {
      //     if (err) return res.status(500).send("There was a problem finding the user.");
      //     if (!user) return res.status(404).send("No user found.");

      //     res.status(200).send(user);
      // });
      console.log(decoded);
      models.sequelize.query(`SELECT "userid","username","email","isTeacher" FROM "Users" where "userid" = ${decoded.id}`).then(([result, metadata]) => {
        if (result.length == 0)
          return res.status(404).send("No user found.");
        res.status(200).send(result);
      }).catch((err) => {
        console.log(err);
        return res.status(500).send("There was a problem finding the user.");
      })
    })

  })

  router.post('/login', (req, res) => {
    verifyUser(req.body.email, req.body.password).then((userid) => {
      console.log("RETURNED VALUE =", userid);
      if (!userid)
        return res.status(401).send({ auth: false, token: null });
      var token = jwt.sign({ id: userid }, config.secret, { expiresIn: 86400 });
      res.status(200).send({ auth: true, token: token });
    }).catch((err) => {
      if (err == "No User found") {
        res.status(404).send(err);
      }
      res.status(500).send(err);
    })

  })

  return router
}


function verifyUser(email, password) {
  return new Promise((resolve, reject) => {
    models.sequelize.query(`SELECT * FROM "Users" where "email" = '${email}'`).then(([result, metadata]) => {
      if (result.length == 0)
        reject("No User found");
      var passwordIsValid = bcrypt.compareSync(password, result[0].password);
      if (!passwordIsValid)
        resolve(false);
      resolve(result[0].userid)
    }).catch((err) => {
      reject("There was a problem finding the user.");
    })

  })
}
