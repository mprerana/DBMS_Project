var self = this;
var bcrypt = require('bcrypt-nodejs');



self.insertUser = function(username,password,email,role='1'){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `insert into users(username,password,email,role)
                    values ($1,$2,$3,$4) returning *`,
            values: [username,bcrypt.hashSync(password, bcrypt.genSaltSync(10), null),email,role],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getVerifiedUser = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from users
                    where username = $1 and isactive = true`,
            values: [username],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0]);
        })
        .catch(e => reject(e))
    });
}

self.getUser = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from users
                    where username = $1`,
            values: [username],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0]);
        })
        .catch(e => reject(e))
    });
}

self.setActive = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `update users
                    set isactive = true
                    where username = $1`,
            values: [username],
        }
        client.query(query)
        .then(resolve())
        .catch(e => reject(e))
    });
}

self.getUserByEmail = function(email){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from users
                    where email = $1`,
            values: [email],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0]);
        })
        .catch(e => reject(e))
    });
}

self.getUsers = function(){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from users`
        }
        client.query(query)
        .then(res => {
            resolve(res.rows);
        })
        .catch(e => reject(e))
    });
}

self.updateUser = function(username,newusername,password=''){
    client = this;
    return new Promise(function(resolve,reject){
        var query;
        if (!password){
            query = {
                text:   `update users
                        set username = $1, password = $2
                        where username = $3`,
                values: [newusername,bcrypt.hashSync(password, bcrypt.genSaltSync(10), null),username],
            }
        } else {
            query = {
                text:   `update users
                        set username = $1
                        where username = $2`,
                values: [newusername,username],
            }
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.changePassword = function(username,password){
    client = this;
    return new Promise(function(resolve,reject){
        var query;
        query = {
            text:   `update users
                    set password = $2
                    where username = $1 returning *`,
            values: [username,bcrypt.hashSync(password, bcrypt.genSaltSync(10), null)],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.deleteUser = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `delete from users
                    where username = $1`,
            values: [username],
        }
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.comparePassword = function(user,password,callback){
    bcrypt.compare(password,user.password, (err, isMatch) => {
        return callback (err, isMatch);
    })
}
module.exports = self;