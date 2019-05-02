module.exports = function (sequelize, DataTypes) {
  var Response = sequelize.define("Response", {
    response: { type: DataTypes.JSONB },
    marks:{type:DataTypes.INTEGER}
  });

  Response.associate = function (models) {
    models.Response.belongsTo(models.Student, {
      onDelete: "CASCADE",
      foreignKey: {
        allowNull: false,
      }
    })

    models.Response.belongsTo(models.quiz, {
      onDelete: "CASCADE",
      foreignKey: {
        allowNull: false,
      }
    });
  };
  return Response
};
