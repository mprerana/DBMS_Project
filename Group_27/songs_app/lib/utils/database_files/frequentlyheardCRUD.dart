import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/frequentlyHeard.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class FrequentlyHeardCRUD {
  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all playlist
  Future<List<Map<String, dynamic>>> getFrequentlyHeardMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${FrequentlyHeardTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertFrequentlyHeard(FrequentlyHeard frequentlyheard) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(
        FrequentlyHeardTable.tableName, frequentlyheard.toMap());
    return result;
  }

  // update
  Future<int> updateFrequentlyHeard(FrequentlyHeard frequentlyheard) async {
    Database db = await databaseHelper.database;

    int result = await db.update(
        FrequentlyHeardTable.tableName, frequentlyheard.toMap(),
        where: '${FrequentlyHeardTable.colSongId} = ?',
        whereArgs: [frequentlyheard.songId]);
    // int result = await db.rawUpdate('UPDATE ${playlistsTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteFrequentlyHeard(int songid) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${FrequentlyHeardTable.tableName} WHERE ${FrequentlyHeardTable.colSongId} = \'$songid\'');
    return result;
  }

  // get number of records
  Future<int> getTotalFrequentlyHeardCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap = await db
        .rawQuery('SELECT COUNT (*) FROM ${FrequentlyHeardTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<FrequentlyHeard>> getFrequentlyHeardList() async {
    List<Map<String, dynamic>> mapList = await getFrequentlyHeardMapList();
    int count = mapList.length;

    List<FrequentlyHeard> frequentlyheardList = List<FrequentlyHeard>();
    for (int i = 0; i < count; i++) {
      frequentlyheardList
          .add(FrequentlyHeard.fromMaptoFrequentlyHeard(mapList[i]));
    }
    return frequentlyheardList;
  }

  // fetch playlist by id
  Future<List<Map<String, dynamic>>> getFrequentlyHeardById(int songid) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${FrequentlyHeardTable.tableName} WHERE ${FrequentlyHeardTable.colSongId} = $songid');
    return result;
  }
}
