import 'dart:async';

import 'package:sqflite/sqflite.dart';

import 'package:songs_app/models/image.dart';
import 'package:songs_app/utils/database_files/tables.dart';
import 'package:songs_app/utils/database_helper.dart';

class ImagesCRUD {
  DatabaseHelper databaseHelper = DatabaseHelper();

  // fetch all users
  Future<List<Map<String, dynamic>>> getImageMapList() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result =
        await db.rawQuery('SELECT * FROM ${Imagestable.tableName}');
    return result;
  }

  // insert
  Future<int> insertImage(Images image) async {
    Database db = await databaseHelper.database;

    int result = await db.insert(Imagestable.tableName, image.toMap());
    return result;
  }

  // update
  Future<int> updateImage(Images image) async {
    Database db = await databaseHelper.database;

    int result = await db.update(Imagestable.tableName, image.toMap(),
        where: '${Imagestable.colImageId} = ?', whereArgs: [image.imageId]);
    // int result = await db.rawUpdate('UPDATE ${UsersTable.tableName} SET {}')
    return result;
  }

  // delete
  Future<int> deleteImage(String name) async {
    Database db = await databaseHelper.database;

    int result = await db.rawDelete(
        'DELETE FROM ${Imagestable.tableName} WHERE ${Imagestable.colName} = \'$name\'');
    return result;
  }

  // get number of records
  Future<int> getTotalImageCount() async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> countMap =
        await db.rawQuery('SELECT COUNT (*) FROM ${Imagestable.tableName}');
    int result = Sqflite.firstIntValue(countMap);
    return result;
  }

  Future<List<Images>> getImageList() async {
    List<Map<String, dynamic>> mapList = await getImageMapList();
    int count = mapList.length;

    List<Images> imageList = List<Images>();
    for (int i = 0; i < count; i++) {
      imageList.add(Images.fromMaptoImage(mapList[i]));
    }
    return imageList;
  }

  // fetch image by id
  Future<List<Map<String, dynamic>>> getImageMapById(String name) async {
    Database db = await databaseHelper.database;

    List<Map<String, dynamic>> result = await db.rawQuery(
        'SELECT * FROM ${Imagestable.tableName} WHERE ${Imagestable.colName} = $name');
    return result;
  }
}
