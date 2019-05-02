
module.exports = (models) => {

  let calculateMarks = async (quizid) => {
    console.log("finishing test", quizid)
    let sql = `SELECT id, response from "Responses" WHERE "quizQuizid"=${quizid}`
    let results = await models.sequelize.query(sql)
    results = results[0]

    sql = `SELECT answers from quizzes WHERE quizid=${quizid}`
    let answers = await models.sequelize.query(sql)

    answers = answers[0][0]['answers']
    console.log(answers)
    for (const responseIdx in results) {
      let attempts = results[responseIdx]['response']
      console.log(attempts)
      let marks = 0;

      for (const index in attempts) {
        if (attempts[index] == answers[index]) {
          marks++
        }
      }

      sql = `UPDATE "Responses" SET marks=${marks} WHERE id=${results[responseIdx]['id']} RETURNING *`
      await models.sequelize.query(sql)
    }
  }

  let testEndTimer = async (quizid) => {
    let sql = `SELECT endtime from "quizzes" where quizid=${quizid}`
    let endtime = await models.sequelize.query(sql)
    endtime = endtime[0][0]['endtime']

    endtime = new Date(endtime)
    let remainingTime = endtime.getTime() - Date.now()

    console.log(remainingTime)

    if (remainingTime > 2147483647) {
      setTimeout(async () => {
        await testEndTimer(quizid)
      }, 2147483630)
    } else {
      setTimeout(() => {
        console.log("ending test...")
        calculateMarks(quizid)
      }, remainingTime)
    }
  }

  let restartTimers = async () => {
    let sql = `SELECT quizid from "quizzes" where current_timestamp < endtime`
    let quizzes = await models.sequelize.query(sql)

    for (const idx in quizzes[0]) {
      await testEndTimer(quizzes[0][idx]['quizid'])
    }

    console.log(quizzes[0])
  }

  return {
    'restartTimers': restartTimers,
    'testEndTimer': testEndTimer,
    'testCM': calculateMarks,
  }
}