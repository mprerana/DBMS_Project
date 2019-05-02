const express = require('express');
const Router = express.Router();
const query = require('../utilities/query');
const checkAuth = require('../utilities/checkAuth');

Router.put('/add',async (req,res)=>{
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const findIdQuery = `SELECT MAX(msno) AS currid FROM msales WHERE uid=${req.query.uid};`;

  IdRows = await query.executeQuery('dairy_management',findIdQuery);
  const currid = int(IdRows[0]['currid'])
  if(currid === null){
    currid = 1;
  }
  else{
    currid+=1;
  }

  const insertquery = `INSERT INTO msales (uid , msno , accountno , amount , clr , date , fat , qty , shift) VALUES (${req.query.uid} , ${currid} , ${req.query.accountno} , ${req.query.amount} , ${req.query.clr} , ${req.query.date} , ${req.query.fat} , ${req.query.qty} , ${req.query.shift}) WHERE uid=${req.query.uid};`;

	 await query.executeQuery('dairy_management',insertquery);
   res.status(200).send('Money sale added successfully')
});

Router.delete('/del',async (req,res)=>{
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }
  const deletequery = `DELETE FROM msales WHERE msno=${req.query.msno} AND uid=${req.query.uid};`;

  await query.executeQuery('dairy_management',deletequery);
  res.status(200).send('Sale deleted successfully')
});

Router.get('/listall', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listallquery = `SELECT * FROM msales WHERE uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listallquery);

  res.status(200);   res.send(rows)

});

Router.get('/listbydate', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listbydate = `SELECT * FROM msales WHERE time BETWEEN ${req.query.time1} AND ${req.query.time2} AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listbydate);

  res.status(200);   res.send(rows)

});

Router.get('/listbyaccount', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listaccount = `SELECT * FROM msales WHERE accountno=${req.query.accountno} AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listaccount);

  res.status(200);   res.send(rows)

});


module.exports = Router;
