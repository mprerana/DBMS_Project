import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/playlist.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class PlaylistCRUD {

  static PlaylistCRUD _playlistCRUD = PlaylistCRUD._createInstance();

  PlaylistCRUD._createInstance();

  factory PlaylistCRUD() => _playlistCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all playlist
  Future<List<Map<String, dynamic>>> getPlaylistMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${PlaylistTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertPlaylist(Playlist playlist) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(PlaylistTable.tableName, playlist.toMap());
    return result;
  }

  // update
  Future<int> updatePlaylist(Playlist playlist) async {
    Database db = await databaseHelper.database;

    int result = await db.update(PlaylistTable.tableName, playlist.toMap(),
        where: '${PlaylistTable.colPlaylistId} = ?',
        whereArgs: [playlist.playlistId]);
    // int result = await db.rawUpdate('UPDATE ${playlistsTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deletePlaylist(String name) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${PlaylistTable.tableName} WHERE ${PlaylistTable.colName} = \'$name\'');
    return result;
  }

  // get number of records
  Future<int> getTotalPlaylistCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${PlaylistTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<Playlist>> getPlaylistList() async {
    List<Map<String, dynamic>> mapList = await getPlaylistMapList();
    int count = mapList.length;

    List<Playlist> playlistList = List<Playlist>();
    for (int i = 0; i < count; i++) {
      playlistList.add(Playlist.fromMaptoPlaylist(mapList[i]));
    }
    return playlistList;
  }

  // fetch playlist by id
  Future<List<Map<String, dynamic>>> getPlaylistMapById(String name) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${PlaylistTable.tableName} WHERE ${PlaylistTable.colName} = $name');
    return result;
  }
}
