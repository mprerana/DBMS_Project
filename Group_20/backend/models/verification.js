var self = this;

self.insertNewToken = function(username, token,type){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `insert into verification(username,token,type)
                    values ($1,$2,$3) returning *`,
            values: [username,token,type],
        }
        client.query(query)
        .then(res => {
            resolve()
        })
        .catch(e => reject(e))
    });
}

self.verifyToken = function(token){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from verification
                    where token = $1`,
            values: [token],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}
self.deleteToken = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `delete from verification
                    where username = $1`,
            values: [username],
        }
        client.query(query)
        .then(resolve())
        .catch(e => reject(e))
    });
}
module.exports = self;