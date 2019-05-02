const db = require('../util/database');

exports.Admin = class Admin{
    constructor(username, token_id, password){
        this.username = username;
        this.token_id = token_id;
        this.password = password;
    }

    static verifyByToken(id){
        return db.execute(`select Username from Admin where Token_Id='${id}';`);
    }
};