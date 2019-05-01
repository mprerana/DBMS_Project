import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/songBy.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class SongByCRUD {

  static SongByCRUD _songByCRUD = SongByCRUD._createInstance();

  SongByCRUD._createInstance();

  factory SongByCRUD() => _songByCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all playlist
  Future<List<Map<String, dynamic>>> getSongByMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${SongByTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertSongBy(SongBy songby) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(SongByTable.tableName, songby.toMap());
    return result;
  }

  // update
  Future<int> updateSongBy(SongBy songby) async {
    Database db = await databaseHelper.database;

    int result = await db.update(SongByTable.tableName, songby.toMap(),
        where: '${SongByTable.colSongId} = ?', whereArgs: [songby.songId]);
    // int result = await db.rawUpdate('UPDATE ${playlistsTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteSongBy(int artistId) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${SongByTable.tableName} WHERE ${SongByTable.colArtistId} = $artistId');
    return result;
  }

  // get number of records
  Future<int> getTotalSongByCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${SongByTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<SongBy>> getSongByList() async {
    List<Map<String, dynamic>> mapList = await getSongByMapList();
    int count = mapList.length;

    List<SongBy> songbyList = List<SongBy>();
    for (int i = 0; i < count; i++) {
      songbyList.add(SongBy.fromMaptoSongBy(mapList[i]));
    }
    return songbyList;
  }

  // fetch playlist by id
  Future<List<Map<String, dynamic>>> getSongByMapById(int artistId) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${SongByTable.tableName} WHERE ${SongByTable.colArtistId} = $artistId');
    return result;
  }
}
