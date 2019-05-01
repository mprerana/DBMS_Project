import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/albums.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class AlbumCRUD {

  static AlbumCRUD _albumCRUD = AlbumCRUD._createInstance();

  AlbumCRUD._createInstance();

  factory AlbumCRUD() => _albumCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all playlist
  Future<List<Map<String, dynamic>>> getAlbumMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${AlbumsTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertAlbum(Album album) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(AlbumsTable.tableName, album.toMap());
    return result;
  }

  // update
  Future<int> updateAlbum(Album album) async {
    Database db = await databaseHelper.database;

    int result = await db.update(AlbumsTable.tableName, album.toMap(),
        where: '${AlbumsTable.colAlbumId} = ?', whereArgs: [album.albumId]);
    // int result = await db.rawUpdate('UPDATE ${playlistsTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteAlbum(String albumName) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${AlbumsTable.tableName} WHERE ${AlbumsTable.colAlbumName} = \'$albumName\'');
    return result;
  }

  // get number of records
  Future<int> getTotalAlbumCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${AlbumsTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  /// returns list of all albums
  Future<List<Album>> getAlbumList() async {
    List<Map<String, dynamic>> mapList = await getAlbumMapList();
    int count = mapList.length;

    List<Album> albumList = List<Album>();
    for (int i = 0; i < count; i++) {
      albumList.add(Album.fromMaptoAlbum(mapList[i]));
    }
    return albumList;
  }

  // fetch playlist by id
  Future<List<Map<String, dynamic>>> getAlbumMapByName(String name) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${AlbumsTable.tableName} WHERE ${AlbumsTable.colAlbumName} = $name');
    return result;
  }

  Future<Album> getAlbumByName(String name) async {
    Map<String,dynamic> map = (await getAlbumMapByName(name)).first;
    return Album.fromMaptoAlbum(map);
  }

  Future<List<Map<String, dynamic>>> getAlbumMapById(String albumId) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${AlbumsTable.tableName} WHERE ${AlbumsTable.colAlbumId} = \'$albumId\'');
    return result;
  }

  Future<Album> getAlbumById(String albumId) async {
    Map<String,dynamic> map = (await getAlbumMapById(albumId)).first;
    return Album.fromMaptoAlbum(map);
  }
}
