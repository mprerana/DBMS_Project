module.exports = function (sequalize, DataTypes) {

  let Teacher = sequalize.define("Teacher", {
    tid: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    }
  })

  Teacher.associate = function (models) {
    models.Teacher.hasMany(models.Course)
    models.Teacher.belongsTo(models.User, { foreignKey: 'tid' })
  }

  return Teacher
}
