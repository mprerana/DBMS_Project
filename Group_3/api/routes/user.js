const express = require('express');
const Router = express.Router();
const query = require('../utilities/query')
const hash = require('../utilities/hash')


Router.post('/login',async (req,res)=>{
  console.log(req.query);
  getInfo = `select * from users where uid = ${req.query.uid};`
  userRes = await query.executeQuery('dairy_management',getInfo);
  if (userRes.length != 1){
    res.status(403).send('Unauthorized Access')
  }
  passhash = hash.sha512(req.query.pass,userRes[0]['salt'])
  console.log(passhash)
  if (passhash.passwordHash == userRes[0]['phash']){
    token =hash.genRandomString(20);
    authquer= `insert into auth (uid,authtoken,time) values (${req.query.uid},'${token}','${(new Date()).toISOString()}')`
    console.log(authquer)
    await query.executeQuery('dairy_management',authquer)
    res.status(200).send(token);
  }
  else{
    res.status(403).send('Unauthorized Access')
  }

})

module.exports = Router;
