module.exports = function (sequelize, DataTypes) {

  var quiz = sequelize.define("quiz", {
    quizid: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },
    quizname:{type: DataTypes.STRING},
    accesskey: { type: DataTypes.STRING, allowNull:false },
    qdata: { type: DataTypes.JSONB },
    answers:{ type: DataTypes.JSONB },
    starttime: { type: DataTypes.DATE, validate: { isDate: true } },
    endtime: { type: DataTypes.DATE, validate: { isDate: true } },
  });

  quiz.associate = function (models) {
    models.quiz.hasMany(models.Response)
    models.quiz.belongsTo(models.Course)
  };

  return quiz;
}
