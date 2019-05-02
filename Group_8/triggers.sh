echo "killing mongod and mongos"
killall mongod
killall mongos
echo "removing data files"
rm -rf /data/config
rm -rf /data/shard*


# start a replica set and tell it that it will be shard0
echo "starting servers for shard 0"
mkdir -p s0_rs0 s0_rs1 s0_rs2
./mongod --replSet s0 --logpath "s0-r0.log" --dbpath s0_rs0 --port 37017 --fork --shardsvr --smallfiles
./mongod --replSet s0 --logpath "s0-r1.log" --dbpath s0_rs1 --port 37018 --fork --shardsvr --smallfiles
./mongod --replSet s0 --logpath "s0-r2.log" --dbpath s0_rs2 --port 37019 --fork --shardsvr --smallfiles

sleep 5
# connect to one server and initiate the set
echo "Configuring s0 replica set"
mongo --port 37017 << 'EOF'
config = { _id: "s0", members:[
          { _id : 0, host : "localhost:37017" },
          { _id : 1, host : "localhost:37018" },
          { _id : 2, host : "localhost:37019" }]};
rs.initiate(config)
EOF

# start a replicate set and tell it that it will be a shard1
echo "starting servers for shard 1"
mkdir -p s1_rs0 s1_rs1 s1_rs2
mongod --replSet s1 --logpath "s1-r0.log" --dbpath s1_rs0 --port 47017 --fork --shardsvr --smallfiles
mongod --replSet s1 --logpath "s1-r1.log" --dbpath s1_rs1 --port 47018 --fork --shardsvr --smallfiles
mongod --replSet s1 --logpath "s1-r2.log" --dbpath s1_rs2 --port 47019 --fork --shardsvr --smallfiles

sleep 5

echo "Configuring s1 replica set"
mongo --port 47017 << 'EOF'
config = { _id: "s1", members:[
          { _id : 0, host : "localhost:47017" },
          { _id : 1, host : "localhost:47018" },
          { _id : 2, host : "localhost:47019" }]};
rs.initiate(config)
EOF

# start a replicate set and tell it that it will be a shard2
echo "starting servers for shard 2"
mkdir -p s2_rs0 s2_rs1 s2_rs2
mongod --replSet s2 --logpath "s2-r0.log" --dbpath s2_rs0 --port 57017 --fork --shardsvr --smallfiles
mongod --replSet s2 --logpath "s2-r1.log" --dbpath s2_rs1 --port 57018 --fork --shardsvr --smallfiles
mongod --replSet s2 --logpath "s2-r2.log" --dbpath s2_rs2 --port 57019 --fork --shardsvr --smallfiles

sleep 5

echo "Configuring s2 replica set"
mongo --port 57017 << 'EOF'
config = { _id: "s2", members:[
          { _id : 0, host : "localhost:57017" },
          { _id : 1, host : "localhost:57018" },
          { _id : 2, host : "localhost:57019" }]};
rs.initiate(config)
EOF


# now start 3 config servers
echo "Starting config servers"
mkdir -p config-a config-b config-c
mongod --logpath "cfg-a.log" --dbpath config/config-a --port 57040 --fork --configsvr --smallfiles
mongod --logpath "cfg-b.log" --dbpath config/config-b --port 57041 --fork --configsvr --smallfiles
mongod --logpath "cfg-c.log" --dbpath config/config-c --port 57042 --fork --configsvr --smallfiles


# now start the mongos on a standard port
mongos --logpath "mongos-1.log" --configdb localhost:57040,localhost:57041,localhost:57042 --fork
echo "Waiting 60 seconds for the replica sets to fully come online"
sleep 60
echo "Connnecting to mongos and enabling sharding"

# add shards and enable sharding on the test db
mongo <<'EOF'
db.adminCommand( { addshard : "s0/"+"localhost:37017" } );
db.adminCommand( { addshard : "s1/"+"localhost:47017" } );
db.adminCommand( { addshard : "s2/"+"localhost:57017" } );
db.adminCommand({enableSharding: "TodoApp"})
db.adminCommand({shardCollection: "school.students", key: {_id:1}});
EOF





























// const mongo = require('mongodb').MongoClient;
// mongo.connect("mongodb://localhost:27017/?replicaSet=rs0").then(client => {
//     console.log("connected");
//     const db = client.db("TodoApp");
//     const collection = db.collection("todos");
//     pipeline = [
//         {
//             $match: {"fullDocument.text" : "Ee sala cup namde"}
//         }
//     ];
//
//     const changeStream = collection.watch(pipeline);
//     changeStream.on("change",function(event){
//         console.log(JSON.stringify(event));
//     });
// });
