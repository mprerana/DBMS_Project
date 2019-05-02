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
  const findIdQuery = `SELECT MAX(icode) AS currid FROM item WHERE uid=${req.query.uid};`;

  IdRows = await query.executeQuery('dairy_management',findIdQuery);
  var currid = int(IdRows[0]['currid'])
  if(currid === null){
    currid = 1;
  }
  else{
    currid+=1;
  }

  const insertquery = `INSERT INTO item (uid , icode , available , name , rate) VALUES (${req.query.uid} , ${currid} , ${req.query.available} , '${req.query.name}' , ${req.query.rate});`;

	 await query.executeQuery('dairy_management',insertquery);
   res.status(200).send('Item added successfully')
});


Router.delete('/del',async (req,res)=>{
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }
  const deletequery = `DELETE FROM item WHERE icode=${req.query.icode} AND uid=${req.query.uid};`;

  await query.executeQuery('dairy_management',deletequery);
  res.status(200).send('Item deleted successfully')
});

Router.get('/listall', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listallquery = `SELECT * FROM item WHERE uid=${req.query.uid};`;
  rows = await query.executeQuery('dairy_management',listallquery);

  res.status(200);   res.send(rows)

});

Router.get('/list', async (req, res)=> {
  let authentic = await checkAuth.checkAuth(req.query.uid,req.query.authtoken)
  if (!authentic){
    res.status(403).send('Unauthorized Access')
    return ;
  }

  const listquery = `SELECT * FROM item WHERE uid=${req.query.uid} AND name LIKE '${req.query.name}%';`;
  rows = await query.executeQuery('dairy_management',listquery);

  res.status(200);   res.send(rows)

});


module.exports = Router;
