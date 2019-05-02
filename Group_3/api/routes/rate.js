const express = require('express');
const Router = express.Router();
const query = require('../utilities/query');
const checkAuth = require('../utilities/checkAuth');

Router.get('/listall', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listallquery = `SELECT * FROM rates WHERE uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listallquery);

  res.status(200);
  res.send(rows)
});

Router.get('/listbyfat', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listbyfat = `SELECT * FROM rates WHERE fat=${req.query.fat} AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listbyfat);

  res.status(200);   
  res.send(rows)

});

Router.get('/listbyclr', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listbyclr = `SELECT * FROM rates WHERE clr=${req.query.clr} AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listbyclr);

res.status(200);   res.send(rows)

});

module.exports = Router;
