var crypto = require('crypto');

let functions={}

functions.genRandomString = function(length){
    return crypto.randomBytes(Math.ceil(length))
	    .toString('hex')
	    .slice(0,length);
};

functions.sha512 = function(password, salt){
    var hash = crypto.createHmac('sha512', password);
    return {
	salt:salt,
	passwordHash:functions.digestHmac(hash,salt)	//will be digested later
    };
};

functions.digestHmac = (hash,salt)=>{	//salted Hash
	hash.update(salt);
	return hash.digest('hex')
}


functions.saltHashPassword= (userpassword) =>{
    var salt = functions.genRandomString(8);
    return functions.sha512(userpassword, salt);
}

module.exports = functions;
