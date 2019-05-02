import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/genre.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class GenreCRUD {

  static GenreCRUD _genreCRUD = GenreCRUD._createInstance();

  GenreCRUD._createInstance();

  factory GenreCRUD() => _genreCRUD;

  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all genres
  Future<List<Map<String, dynamic>>> getGenreMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${GenreTable.tableName}');
    return result;
  }

  // insert
  Future<int> insertGenre(Genre genre) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(GenreTable.tableName, genre.toMap());
    return result;
  }

  // update
  Future<int> updateGenre(Genre genre) async {
    Database db = await databaseHelper.database;

    int result = await db.update(GenreTable.tableName, genre.toMap(),
        where: '${GenreTable.colGenreId} = ?', whereArgs: [genre.genreId]);
    // int result = await db.rawUpdate('UPDATE ${UsersTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteGenre(String name) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = \'$name\'');
    return result;
  }

  // get number of records
  Future<int> getTotalGenreCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${GenreTable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<Genre>> getGenreList() async {
    List<Map<String, dynamic>> mapList = await getGenreMapList();
    int count = mapList.length;

    List<Genre> genreList = List<Genre>();
    for (int i = 0; i < count; i++) {
      genreList.add(Genre.fromMaptoGenre(mapList[i]));
    }
    return genreList;
  }

  // fetch geenre by id
  Future<List<Map<String, dynamic>>> getGenreMapById(String name) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${GenreTable.tableName} WHERE ${GenreTable.colName} = $name');
    return result;
  }
}
