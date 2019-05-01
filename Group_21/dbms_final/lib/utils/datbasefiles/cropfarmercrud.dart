import 'dart:async';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/utils/datbasefiles/databasetables.dart';
import 'package:dbms_final/farmer/models/cropfarmer.dart';
class Farmercropinteraction {
  DatabaseHelper databaseHelper = DatabaseHelper();


  Future<List<Map<String, dynamic>>> getcropMapList() async {
    Database db = await databaseHelper.database;

    var result =
        db.rawQuery('SELECT * FROM ${Farmercrop.farmercrop}');
    return result;
  }

  // insert into table
  Future<int> insertcrop(Cropfarmer cropfarmer) async {
    print("inserting");
    Database db = await databaseHelper.database;
    print("inserting");
    int result =
        await db.insert(Farmercrop.farmercrop, cropfarmer.toMap());
  print(result);
    return result;
  }

  // update into table
  Future<int> updatecropfarmer(Cropfarmer cropfarmer) async {
    Database db = await databaseHelper.database;
    int result = await db.update(Farmercrop.farmercrop, cropfarmer.toMap(), where: '${cropfarmer.fid}=?', whereArgs: [cropfarmer.fid]);

    return result;
  }
Future<Map<String,dynamic>>getcropList(int dummyid) async {
     Database db = await databaseHelper.database;
  List<Map<String,dynamic>> croplist = await db.rawQuery('SELECT * FROM ${Farmercrop.farmercrop} WHERE ${Farmercrop.colfid} = $dummyid');
    print("croplist1");
    print(croplist);
    return croplist[0];
  }
  
 


}
