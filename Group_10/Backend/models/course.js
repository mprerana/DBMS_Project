module.exports = function (sequalize, DataTypes) {
  let Course = sequalize.define("Course", {

    cid: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true
    },

    cname: { type: DataTypes.STRING },

    joinKey: {
      type: DataTypes.STRING,
      unique: true,
      allowNull: false
    },

    startDate: {
      type: DataTypes.DATE,
      validate: { isDate: true },
      defaultValue: sequalize.NOW
    },

    endDate: {
      type: DataTypes.DATE,
      validate: { isDate: true },
      allowNull: true
    },

  })

  Course.associate = function (models) {

    models.Course.hasMany(models.quiz)
    models.Course.belongsTo(models.Teacher)
    models.Course.belongsToMany(models.Student, { through: 'StudentCourse' })
  }

  return Course
}