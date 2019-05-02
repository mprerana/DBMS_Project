const cassandra = require('cassandra-driver');

let f={}
f.executeQuery=(keyspace,query,err_string,success_string)=>{
	return new Promise((resolve,reject)=>{
		const client = new cassandra.Client({ contactPoints: ['192.168.56.100', '192.168.56.101','192.168.56.202'],localDataCenter: 'datacenter1' , keyspace: keyspace });
		client.connect()
		.then(function () {
		  return client.execute(query);
		})
		.then(function (result) {
		  client.shutdown();
		  if(success_string!==undefined){
			console.log(success_string);
			}
			resolve(result.rows)
		})
		.catch(function (err) {
			console.error(err)
			if(err_string!==undefined){
				console.log(err_string);
			}
		  return client.shutdown();
	  });
	  
	})
	
}
module.exports = f
