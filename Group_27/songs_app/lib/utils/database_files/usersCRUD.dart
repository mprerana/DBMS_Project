import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/users.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class UsersCRUD {
  static UsersCRUD _usersCRUD = UsersCRUD._createInstance();

  UsersCRUD._createInstance();

  factory UsersCRUD() => _usersCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  /// fetch all users
  Future<List<Map<String, dynamic>>> getUserMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${UsersTable.tableName}');
    return result;
  }

  /// inserts the user to table
  Future<int> insertUser(User user) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(UsersTable.tableName, user.toMap());
    return result;
  }

  /// updates the user
  Future<int> updateUser(User user) async {
    Database db = await databaseHelper.database;

    int result = await db.update(UsersTable.tableName, user.toMap(),
        where: '${UsersTable.colUserId} = ?', whereArgs: [user.userId]);
    // int result = await db.rawUpdate('UPDATE ${UsersTable.tableName} SET {}')
    return result;
  }

  /// delete the user
  Future<int> deleteUser(String emailid) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${UsersTable.tableName} WHERE ${UsersTable.colEmail} = \'$emailid\'');
    return result;
  }

  /// get number of records
  Future<int> getTotalUserCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${UsersTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<User>> getUserList() async {
    List<Map<String, dynamic>> mapList = await getUserMapList();
    int count = mapList.length;

    List<User> userList = List<User>();
    for (int i = 0; i < count; i++) {
      userList.add(User.fromMaptoUser(mapList[i]));
    }
    return userList;
  }

  /// fetch user by id
  Future<List<Map<String, dynamic>>> getUserMapById(String emailid) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${UsersTable.tableName} WHERE ${UsersTable.colEmail} = \'$emailid\' ');
    return result;
  }

  Future<Map<String, dynamic>> getUserMapByEmail(String emailid) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${UsersTable.tableName} WHERE ${UsersTable.colEmail} = \'$emailid\' ');
    return result[0];
  }

  Future<User> getUserByID(String emailId) async {
    List<Map<String, dynamic>> userDetails = await getUserMapById(emailId);
    if (userDetails == null || userDetails.isEmpty) {
      print('User with emailId: $emailId does not exist');
      return null;
    }
    return User.fromMaptoUser(userDetails.first);
  }

 
}
