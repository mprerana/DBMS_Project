const express = require('express')
const md5 = require('md5')
const kmeans = require('node-kmeans')

const token2id = require("../auth/token2id")

module.exports = (models, client) => {

  // how_to_import
  const _getters = require("../lib/getters")(models, client)

  const router = express.Router()

  router.get('/listgroups', async (req, res) => {
    try {
      let id = await token2id(req.get('x-access-token'))

      let isTeacher = await models.sequelize.query(`SELECT "isTeacher" from "Users" where userid = ?`, {
        replacements: [id],
      })

      isTeacher = isTeacher[0][0].isTeacher

      let sql;

      if (isTeacher) {
        sql = `SELECT * FROM "Courses" WHERE "TeacherTid" = ?`
        console.log("hi")
      } else {
        sql = `SELECT cid,cname,"joinKey","startDate","endDate","TeacherTid","name" FROM "Courses","Users" WHERE cid IN (SELECT "CourseCid" as cid FROM "StudentCourse" WHERE "StudentSid" = ?) AND "Users"."userid"="Courses"."TeacherTid"`
      }

      console.log(sql)

      let result = await models.sequelize.query(sql, {
        replacements: [id]
      })

      console.log(result[0])
      res.json(result[0])

    } catch (e) {
      res.json(e)
    }
  })

  router.get("/courseinfo/:cid", async (req, res) => {
    try {
      sql = `SELECT cid,cname,"TeacherTid",username,name,email,"joinKey" FROM "Courses","Users" WHERE "Courses"."cid" = ? AND "Courses"."TeacherTid"="Users"."userid" `
      let result = await models.sequelize.query(sql, {
        replacements: [req.params.cid]
      })
      res.json(result[0])
    } catch (e) {
      console.log(e)
      res.json(e)
    }

  })


  router.post("/createcourse", async (req, res) => {

    try {

      let id = await token2id(req.get('x-access-token'))

      let isTeacher = await _getters.isTeacher(id)

      if (!isTeacher) throw ("ID is not a teacher")

      let oldCid = await models.sequelize.query(`SELECT cid from "Courses" ORDER BY cid DESC LIMIT 1`)
      oldCid = oldCid[0]

      let currCid;
      if (oldCid.length == 0) {
        currCid = 0
      } else {
        currCid = oldCid[0] + 1
      }

      let hash = md5(req.body.cname + currCid.toString())

      let date = new Date()
      date = date.toJSON()


      /* to create a new teacher
      // let sql = `INSERT INTO "Teachers" VALUES (?, ?, ?) RETURNING *`
      // let teacher = await models.sequelize.query(sql, {
      //   replacements: [id, date, date]
      // })
      */

      let sql = `INSERT INTO "Courses"("cname", "joinKey", "TeacherTid", "createdAt", "updatedAt", "startDate") VALUES(?,?,?,?,?,?) RETURNING *`
      let course = await models.sequelize.query(sql, {
        replacements: [req.body.cname, hash, id, date, date, date]
      })

      /* how_to_use
      let newCid = course[0][0].cid
      let newTid = await _getters.getTidFromCourse(newCid) //or use "then"
      */

      res.json(course[0][0])
    } catch (e) {
      res.json(e)
    }
  })

  router.post("/joincourse", async (req, res) => {
    try {

      let id = await token2id(req.get('x-access-token'))
      let isStudent = !(await _getters.isTeacher(id))

      if (!isStudent) throw ("id is not a student")

      let sql = `SELECT cid FROM "Courses" WHERE "joinKey" = '${req.body.joinKey}'`

      console.log(sql)

      let course = await models.sequelize.query(sql, {
        replacements: []
      })

      console.log(course)

      let date = new Date()
      date = date.toJSON()


      sql = `INSERT INTO "StudentCourse"("CourseCid", "StudentSid", "createdAt", "updatedAt") VALUES(?,?,?,?) RETURNING *`

      let result = await models.sequelize.query(sql, {
        replacements: [course[0][0].cid, id, date, date]
      })

      res.json(result[0][0])

    } catch (e) {
      console.log("noo....", e)
      res.status(403).json("error")
    }

  })

  router.get("/getCSV/:courseid", async (req, res) => {

    let id, coursetid

    try {
      id = await token2id(req.get('x-access-token'))
      coursetid = await _getters.getTidFromCourse(req.params.courseid)
    } catch (e) {
      res.json(e)
    }

    if (id != coursetid) {
      res.status(403).send("Forbidden")
    }

    let sql = `SELECT "StudentSid", marks, "quizQuizid" from "Responses" WHERE "quizQuizid" IN `
      + `(SELECT quizid from quizzes WHERE "CourseCid"=${req.params.courseid})`;


    try {
      let result = await models.sequelize.query(sql)
      result = result[0]
      console.log(result)

      let rows = {}
      let quizzes = {}
      let students = {}

      for (const idx in result) {
        console.log(idx)
        let student = result[idx]['StudentSid']
        if (!(student in students)) {
          students[student] = 1
        }

        let quiz = result[idx]['quizQuizid']
        if (!(quiz in quizzes)) {
          quizzes[quiz] = 1
        }

        console.log(student, quiz)
        if (student in rows) {
          rows[student][quiz] = result[idx]['marks']
        } else {
          rows[student] = {}
          rows[student][quiz] = result[idx]['marks']
        }
      }

      console.log(rows)
      console.log(quizzes)
      console.log(students)

      sql = `SELECT userid, name from "Users" WHERE userid IN (${Object.keys(students).join(',')}) ORDER BY userid`
      result = await models.sequelize.query(sql)
      let studentNames = result[0].map(obj => obj['name'])
      console.log(studentNames)

      sql = `SELECT quizname from "quizzes" WHERE quizid IN (${Object.keys(quizzes).join(',')}) ORDER BY quizid`
      result = await models.sequelize.query(sql)
      let quizNames = result[0].map(obj => `"${obj['quizname']}"`)
      console.log(quizNames)

      let csv = `"studentID","name",${quizNames.join(",")}\n`

      Object.keys(students).sort().forEach((student) => {
        let row = ""
        row += `"${student}","${studentNames.shift()},"`
        console.log(row)
        row += Object.keys(quizzes).sort().map(quiz => {
          console.log(quiz)
          if (quiz in rows[student])
            return `"${rows[student][quiz]}"`
          else
            return `""`
        }).join(",")
        row += `\n`
        console.log(row);
        csv += row
      })

      res.setHeader('Content-disposition', `attachment; filename=marks_${req.params.courseid}.csv`);
      res.setHeader('Content-type', 'application/octet-stream');
      res.send(csv);

    } catch (e) {
      res.status(400).send(e)
    }

  })

  router.post("/getclusters", async (req, res) => {
    let id, coursetid, result

    try {
      id = await token2id(req.get('x-access-token'))
      coursetid = await _getters.getTidFromCourse(req.body.courseid)
    } catch (e) {
      res.json(e)
    }

    if (id != coursetid) {
      res.status(403).send("Forbidden")
    }

    let sql = `SELECT "StudentSid", SUM(marks) from "Responses" WHERE  "quizQuizid" IN `
      + `(SELECT quizid from quizzes WHERE "CourseCid"=${req.body.courseid})  GROUP BY "StudentSid"`;

    try {
      result = await models.sequelize.query(sql)
      result = result[0]

      console.log(JSON.stringify(result))

    } catch (e) {
      console.log(e)
      res.json(e)
    }

    let vectors = result.map((entry) => [parseInt(entry.sum)])

    console.log(vectors)

    kmeans.clusterize(vectors, { k: 5 }, (err, clusters) => {
      if (err)
        console.error(err)
      else {
        clusters = clusters.sort((a, b) => {
          console.log(a.centroid[0] - b.centroid[0])
          return a.centroid[0] - b.centroid[0]
        })
        console.log('%o', clusters)

        let sendJSON = {}

        let grades = ['S', 'A', 'B', 'C', 'D']
        for (let i = 0; i < 5; i++) {
          clusters[i].clusterInd.forEach(entry => {
            console.log(entry)
            sendJSON[result[entry].StudentSid] = {
              "grade": grades[4-i],
              "marks": result[entry].sum
            }
          })
        }

        console.log(sendJSON)
        res.json(sendJSON)

      }
    });

  })
  return router
}
