const query = require('./query')

let f={}
f.checkAuth = async (uid,token) => {
	authQuery = `select * from auth where uid = ${uid} and authtoken = '${token}';`
	rows = await query.executeQuery('dairy_management',authQuery);
	console.log(rows);
	if (rows.length >= 1){
		return true;
	}
	return false;
}

module.exports = f
