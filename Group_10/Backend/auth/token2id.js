var config = require('../config/secret');
var jwt = require('jsonwebtoken');

module.exports = function (token) {
  return new Promise((resolve, reject) => {
    jwt.verify(token, config.secret, (err, decoded) => {
      if (err)
        reject(err);
      //console.log("Token = " + token + "\nID = "+ decoded.id);
      resolve(decoded.id);
    })
  })

}
