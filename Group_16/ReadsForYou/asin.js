// var util = require('util'),
// OperationHelper = require('apac').OperationHelper;

// var opHelper = new OperationHelper({
//     awsId:     '[YOUR ACCESS KEY ID HERE]',
//     awsSecret: '[YOUR SECRET ACCESS KEY HERE]',
//     assocId:   '[YOUR ASSOCIATE TAG HERE]', 
// });


// opHelper.execute('ItemSearch', {
//     'SearchIndex': 'Books',
//     'Keywords': 'harry potter',
//     'ResponseGroup': 'ItemAttributes,Offers'
// }, function(error, results) {
//     if (error) { console.log('Error: ' + error + "\n"); }
//     console.log("Results:\n" + util.inspect(results) + "\n");
// });



// opHelper.execute('ItemLookup', {
//     'ItemId': '[ASIN GOES HERE]',
//     'MechantId': 'All',
//     'Condition': 'All',
//     'ResponseGroup': 'Medium'
// }, function(error, results) {
//     if (error) { console.log('Error: ' + error + "\n"); }
//     console.log("Results:\n" + util.inspect(results) + "\n");
// });

// var express = require('express'); 
// var app = express(); 
  
// app.listen(3000, () => { 
//     console.log('server running on port 3000'); 
// } ) 
  
// // Function callName() is executed whenever  
// // url is of the form localhost:3000/name 
// app.get('/name', callName); 
  
// function callName(req, res) { 
      
//     // Use child_process.spawn method from  
//     // child_process module and assign it 
//     // to variable spawn 
//     var spawn = require("child_process").spawn; 
      
//     // Parameters passed in spawn - 
//     // 1. type_of_script 
//     // 2. list containing Path of the script 
//     //    and arguments for the script  
      
//     // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
//     // so, first name = Mike and last name = Will 
//     var process = spawn('python',["./hello.py", req.query.ASIN]); 
//     console.log(process);
  
//     // Takes stdout data from script which executed 
//     // with arguments and send this data to res object 
//     process.stdout.on('data', function(data) { 
//         res.send(data.toString()); 
//     } ) 
// } 

// function run(cmd, callback) {
//     var spawn = require('child_process').spawn;
//     var command = spawn(cmd);
//     var result = '';
//     command.stdout.on('data', function(data) {
//          result += data.toString();
//     });
//     command.on('close', function(code) {
//         return callback(result);
//     });
// }

// run("ls", function(result) { console.log(result) });


function scrapDetails(param){
    return new Promise(resolve => {
        var spawn = require("child_process").spawn;
        var process = spawn('python',["scrap.py", param]);
        var result = '';
        process.stdout.on('data', function(data) { 
            result += data.toString();
            resolve(result);
            
        });
    });    
}


async function f1()
{
    var x = await scrapDetails(1632361736);
    // console.log(typeof(x))
    // y = JSON.parse(x);
    
    console.log(x.slice(13, -4));
};

f1();



