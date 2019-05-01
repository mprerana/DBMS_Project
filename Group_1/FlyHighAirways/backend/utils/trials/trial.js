const user = require('../../models/auth/user');
const sequelize = require('../database/connect');
//
sequelize.query(user.sqlCommands.constraints.index.email).then(([results, metadata])=>{
    console.log(user.sqlCommands.constraints.index.email);
    console.log("Results!", results);
    console.log("Meta-Data", metadata);

}).catch(err=>{
    console.log("Error!", err);
});

// sequelize.query(user.sqlCommands.table.exists, {type:sequelize.QueryTypes.SELECT}).then(tables=>{
//     // console.log("Results!", results);
//     // console.log("Meta-Data", metadata);
//     console.log(tables);
//     if (tables.length >0){
//         return Promise.reject("Table exists. Use force to drop and create a new one");
//     }
//     else{
//         console.log("creating...");
//         return sequelize.query(user.sqlCommands.table.create);
//     }
// }).then(([result,meta])=>{
//         console.log("Results!", result);
//         console.log("Meta-Data", meta);
// }).catch(err=>{
//     console.log("Error!", err);
// });