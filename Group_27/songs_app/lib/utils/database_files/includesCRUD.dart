import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/includes.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class IncludesCRUD {

  static IncludesCRUD _includesCRUD = IncludesCRUD._createInstance();

  IncludesCRUD._createInstance();

  factory IncludesCRUD() => _includesCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all playlist
  Future<List<Map<String, dynamic>>> getIncludesMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${IncludesTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertIncludes(Includes includes) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(IncludesTable.tableName, includes.toMap());
    return result;
  }

  // update
  Future<int> updateIncludes(Includes includes) async {
    Database db = await databaseHelper.database;

    int result = await db.update(IncludesTable.tableName, includes.toMap(),
        where: '${IncludesTable.colIncludesId} = ?',
        whereArgs: [includes.includesId]);
    // int result = await db.rawUpdate('UPDATE ${playlistsTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteIncludes(int songid) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${IncludesTable.tableName} WHERE ${IncludesTable.colSongId} = $songid');
    return result;
  }

  // get number of records
  Future<int> getTotalIncludesCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${IncludesTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<Includes>> getIncludesList() async {
    List<Map<String, dynamic>> mapList = await getIncludesMapList();
    int count = mapList.length;

    List<Includes> includesList = List<Includes>();
    for (int i = 0; i < count; i++) {
      includesList.add(Includes.fromMaptoIncludes(mapList[i]));
    }
    return includesList;
  }

  // fetch playlist by id
  Future<List<Map<String, dynamic>>> getIncludesMapById(int songid) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${IncludesTable.tableName} WHERE ${IncludesTable.colSongId} = $songid');
    return result;
  }
}
