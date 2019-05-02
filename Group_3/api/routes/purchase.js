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
  const findIdQuery = `SELECT MAX(billno) AS currid FROM purchase WHERE uid=${req.query.uid};`;

  IdRows = await query.executeQuery('dairy_management',findIdQuery);
  var currid = int(IdRows[0]['currid'])
  if(currid === null){
    currid = 1;
  }
  else{
    currid+=1;
  }
  const insertquery = `INSERT INTO purchase (uid , billno , accountno , amount , icode , mode , qty , rate , time) VALUES (${req.query.uid} , ${currid} , ${req.query.accountno} , ${req.query.amount} , ${req.query.icode} , '${req.query.mode}' , ${req.query.quantity} , ${req.query.rate} , '${req.query.time}');`;

	 await query.executeQuery('dairy_management',insertquery);
   res.status(200).send('Purchase added successfully')
});

Router.get('/listall', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listallquery = `SELECT * FROM purchase WHERE uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listallquery);

  res.status(200);
  res.send(rows)

});

Router.get('/listbydate', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listbydate = `SELECT * FROM purchase WHERE time BETWEEN ${req.query.time1} AND ${req.query.time2} AND uid=${req.query.uid};`;
 rows =  await query.executeQuery('dairy_management',listbydate);

 res.status(200);
  res.send(rows)

});

Router.get('/listbyaccount', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listaccount = `SELECT * FROM purchase WHERE accountno=${req.query.accountno} AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listaccount);

  res.status(200);
  res.send(rows)
  

});

Router.get('/listbybill', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listbybill = `SELECT * FROM purchase WHERE billno=${req.query.billno} AND uid=${req.query.uid};`;
  arows = await query.executeQuery('dairy_management',listbybill);

  res.status(200);
  res.send(rows)

});

Router.get('/listbymode', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listmode = `SELECT * FROM purchase WHERE mode='${req.query.mode}' AND uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listmode);

  res.status(200);
  res.send(rows)
});


Router.delete('/del',async (req,res)=>{
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }
  const deletequery = `DELETE FROM purchase WHERE billno=${req.query.billno} AND uid=${req.query.uid};`;

  await query.executeQuery('dairy_management',deletequery);
  res.status(200).send('Purchase deleted successfully')
});


module.exports = Router;
