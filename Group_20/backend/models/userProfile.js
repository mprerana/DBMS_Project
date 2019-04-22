var self = this;
const fs = require('fs');



self.insertUserProfile = function(username, options){
    client = this;
    return new Promise(function(resolve,reject){
        var i = 2;
        var temp = 'VALUES ((SELECT username FROM users WHERE username=$1)';
        var query = {
            text:   'INSERT INTO userProfile (username',
            values: [username],
        }
        if (options.hasOwnProperty("firstname")){
            query.text += ', firstname';
            temp += ',$' + i;
            query.values[i++ - 1] = options.firstname ;
        }
        if (options.hasOwnProperty("lastname")){
            query.text += ', lastname';
            temp += ',$' + i;
            query.values[i++ - 1] = options.lastname; 
        }
        if (options.hasOwnProperty("phone")){
            query.text += ', phone';
            temp += ',$' + i;
            query.values[i++ - 1] = options.phone; 
        }
        if (options.hasOwnProperty("address")){
            query.text += ', address';
            temp += ',$' + i;
            query.values[i++ - 1] = options.address; 
        }
        if (options.hasOwnProperty("pictureurl")){
            query.text += ', pictureurl';
            temp += ',$' + i;
            query.values[i++ - 1] = options.pictureurl;
        }
        temp += ')'
        query.text += ') ' + temp;
        console.log(query)
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.getUserProfile = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `select * from userProfile
                    where username = $1`,
            values: [username],
        }
        client.query(query)
        .then(res => {
            if (res.rows.length !== 0){
                resolve(res.rows[0]);
            } else {
                resolve({});
            }
        })
        .catch(e => reject(e))
    });
}

self.updateUserProfile = function(username,options){
    client = this;
    return new Promise(function(resolve,reject){
        var i = 2;
        var query = {
            text:   'update userProfile set ',
            values: [username],
        }
        if (options.hasOwnProperty("firstname")){
            query.text += ' firstname = $' + i;
            query.values[i++ - 1] = options.firstname ;
        }
        if (options.hasOwnProperty("lastname")){
            if(i>2){
                query.text += ','
            }
            query.text += ' lastname = $' + i;
            query.values[i++ - 1] = options.lastname; 
        }
        if (options.hasOwnProperty("phone")){
            if(i>2){
                query.text += ','
            }
            query.text += ' phone = $' + i;
            query.values[i++ - 1] = options.phone; 
        }
        if (options.hasOwnProperty("address")){
            if(i>2){
                query.text += ','
            }
            query.text += ' address = $' + i;
            query.values[i++ - 1] = options.address; 
        }
        if (options.hasOwnProperty("pictureurl")){
            if(i>2){
                query.text += ','
            }
            query.text += ' pictureurl = $' + i;
            query.values[i++ - 1] = options.pictureurl;
        }
        query.text += ' where username = $1';
        console.log(query)
        client.query(query)
        .then(res => {
            resolve(res.rows[0])
        })
        .catch(e => reject(e))
    });
}

self.deleteUserProfile = function(username){
    client = this;
    return new Promise(function(resolve,reject){
        const query = {
            text:   `delete from userProfile
                    where username = $1
                    returning *`,
            values: [username],
        }
        client.query(query)
        .then(res => {
            if (res.rows[0].hasOwnProperty("pictureurl")){
                console.log(res.rows[0].pictureurl)
                fs.unlink(res.rows[0].pictureurl, (err) => {
                    if (err) {
                      console.error(err)
                      return
                    }
                  
                    //file removed
                    resolve(res.rows[0])
                })
            } else {
                resolve(res.rows[0])
            }
        })
        .catch(e => reject(e))
    });
}

module.exports = self;