module.exports = function (sequelize, DataTypes) {

  var User = sequelize.define("User", {
    userid: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true
    },

    username: { type: DataTypes.STRING, unique: true, allowNull: false },
    password: { type: DataTypes.STRING, allowNull: false },
    name: { type: DataTypes.STRING },
    email: { type:DataTypes.STRING, unique : true},
    age: { type: DataTypes.INTEGER },
    isTeacher: { type: DataTypes.BOOLEAN, allowNull: false }
  });

  User.associate = (models) => {
    models.User.hasOne(models.Student, { foreignKey: 'sid' })
    models.User.hasOne(models.Teacher, { foreignKey: 'tid' })
  }

  return User;
};
