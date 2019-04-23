import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/artists.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class ArtistsCRUD {
  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all playlist
  Future<List<Map<String, dynamic>>> getArtistMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${ArtistTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertArtist(Artist artist) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(ArtistTable.tableName, artist.toMap());
    return result;
  }

  // update
  Future<int> updateArtist(Artist artist) async {
    Database db = await databaseHelper.database;

    int result = await db.update(ArtistTable.tableName, artist.toMap(),
        where: '${ArtistTable.colArtistId} = ?', whereArgs: [artist.artistId]);
    // int result = await db.rawUpdate('UPDATE ${playlistsTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteArtist(String name) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${ArtistTable.tableName} WHERE ${ArtistTable.colName} = \'$name\'');
    return result;
  }

  // get number of records
  Future<int> getTotalArtistCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${ArtistTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<Artist>> getArtistList() async {
    List<Map<String, dynamic>> mapList = await getArtistMapList();
    int count = mapList.length;

    List<Artist> artistList = List<Artist>();
    for (int i = 0; i < count; i++) {
      artistList.add(Artist.fromMaptoArtist(mapList[i]));
    }
    return artistList;
  }

  // fetch playlist by id
  Future<List<Map<String, dynamic>>> getArtistMapById(String name) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${ArtistTable.tableName} WHERE ${ArtistTable.colName} = $name');
    return result;
  }
}
