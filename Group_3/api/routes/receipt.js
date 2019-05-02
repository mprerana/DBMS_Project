const express = require('express');
const Router = express.Router();
const query = require('../utilities/query.js');
const checkAuth = require('../utilities/checkAuth.js');

Router.put('/add',async (req,res)=>{
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const findIdQuery = `SELECT MAX(rno) AS currid FROM receipt WHERE uid=${req.query.uid};`;

  IdRows = await query.executeQuery('dairy_management',findIdQuery);
  var currid = int(IdRows[0]['currid'])
  if(currid === null){
    currid = 1;
  }
  else{
    currid+=1;
  }

  const insertquery = `INSERT INTO receipt (uid , rno , accountno , amount , mode , remarks , time) VALUES (${req.query.uid} , ${currid} , ${req.query.accountno} , ${req.query.amount} , '${req.query.mode}' , '${req.query.remarks}' , '${req.query.time}');`;
  console.log(insertquery)
	await query.executeQuery('dairy_management',insertquery);
  res.status(200).send('receipt added successfully')
});

Router.delete('/del',async (req,res)=>{
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }
  const deletequery = `DELETE FROM receipt WHERE rno=${req.query.rno} AND uid=${req.query.uid};`;

  await query.executeQuery('dairy_management',deletequery);
  res.status(200).send('Receipt deleted successfully')
});

Router.get('/listall', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listallquery = `SELECT * FROM receipt WHERE uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listallquery);

  res.status(200);
  res.send(rows)

});

Router.get('/listbydate', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;0
  }

  const listbydate = `SELECT * FROM receipt WHERE time BETWEEN ${req.query.time1} AND ${req.query.time2} AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listbydate);

  res.status(200);
  res.send(rows)

});

Router.get('/listbyaccount', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listaccount = `SELECT * FROM receipt WHERE accountno=${req.query.accountno} AND uid=${req.query.uid} ALLOW FILTERING;`;
  rows = await query.executeQuery('dairy_management',listaccount);

  res.status(200);
  res.send(rows)

});

Router.get('/listbyrno', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listrno = `SELECT * FROM receipt WHERE rno=${req.query.rno} AND uid=${req.query.uid} ALLOW FILTERING;`;
  rows = await query.executeQuery('dairy_management',listrno);

  res.status(200);
  res.send(rows)

});


module.exports = Router;
