const { promisify } = require('util');


module.exports = (models, client) => {
  const getAsync = promisify(client.get).bind(client);

  let getTidFromCourse = async (cid) => {

    let value = await getAsync(cid)

    if (value !== null)
      return value;

    let sql = `SELECT "TeacherTid" FROM "Courses" WHERE cid = ?`
    let tid = await models.sequelize.query(sql, {
      replacements: [cid]
    })

    client.set(cid, tid[0][0].TeacherTid)

    return tid[0][0].TeacherTid
  }

  let isTeacher = async (id) => {
    let value = await getAsync('a' + id)
    if (value !== null)
      return value != "false";

    let isTeacher = await models.sequelize.query(`SELECT "isTeacher" from "Users" where userid = ?`, {
      replacements: [id],
    })

    client.set('a' + id, isTeacher[0][0].isTeacher)
    console.log("db")
    return isTeacher[0][0].isTeacher
  }

  return {
    "getTidFromCourse": getTidFromCourse,
    "isTeacher": isTeacher
  }
}
