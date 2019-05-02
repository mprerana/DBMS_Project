module.exports = function (sequalize, DataTypes) {

  let Student = sequalize.define("Student", {
    sid: {
      type: DataTypes.INTEGER,
      primaryKey: true,
    }
  })

  Student.associate = function (models) {
    models.Student.belongsToMany(models.Course, { through: 'StudentCourse' })
    models.Student.belongsTo(models.User, { foreignKey: 'sid' })
    models.Student.hasMany(models.Response)

  }

  return Student
}
