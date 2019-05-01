import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/songs.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class SongsCRUD {

  static SongsCRUD _songsCRUD = SongsCRUD._createInstance();

  SongsCRUD._createInstance();

  factory SongsCRUD() => _songsCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all songs
  Future<List<Map<String, dynamic>>> getSongMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${SongsTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertSong(Song song) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(SongsTable.tableName, song.toMap());
    return result;
  }

  // update
  Future<int> updateSong(Song song) async {
    Database db = await databaseHelper.database;

    int result = await db.update(SongsTable.tableName, song.toMap(),
        where: '${SongsTable.colSongId} = ?', whereArgs: [song.songId]);
    // int result = await db.rawUpdate('UPDATE ${UsersTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteSong(String songTitle) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${SongsTable.tableName} WHERE ${SongsTable.colTitle} = \'$songTitle\'');
    return result;
  }

  // get number of records
  Future<int> getTotalSongCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${SongsTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  /// returns list of all songs
  Future<List<Song>> getSongList() async {
    List<Map<String, dynamic>> mapList = await getSongMapList();
    int count = mapList.length;

    List<Song> songList = List<Song>();
    for (int i = 0; i < count; i++) {
      songList.add(Song.fromMaptoSong(mapList[i]));
    }
    return songList;
  }

  // fetch user by id
  Future<List<Map<String, dynamic>>> getSongMapById(String title) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${SongsTable.tableName} WHERE ${SongsTable.colTitle} = $title');
    return result;
  }
}
