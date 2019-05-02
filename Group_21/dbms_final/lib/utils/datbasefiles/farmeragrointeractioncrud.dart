import 'dart:async';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/utils/datbasefiles/databasetables.dart';
import 'package:dbms_final/login/models/interaction.dart';
class Farmeragrointeraction {
  DatabaseHelper databaseHelper = DatabaseHelper();


  Future<List<Map<String, dynamic>>> getinterMapList() async {
    Database db = await databaseHelper.database;

    var result =
        db.rawQuery('SELECT * FROM ${FarmerAgriInteraction.interactiontable}');
    return result;
  }

  // insert into table
  Future<int> insertinteraction(Interaction inter1) async {
    print("inserting");
    Database db = await databaseHelper.database;
    print("inserting");
    int result =
        await db.insert(FarmerAgriInteraction.interactiontable, inter1.toMap());
  
    return result;
  }

  // update into table
  Future<int> updatestatus(int fid,int aid) async {
    Database db = await databaseHelper.database;
    String status ="filled";
    int result = await db.rawUpdate('UPDATE ${FarmerAgriInteraction.interactiontable} SET ${FarmerAgriInteraction.colstatus} AS $status  WHERE ${FarmerAgriInteraction.colfid}=$fid AND ${FarmerAgriInteraction.colaid}=$aid');
    return result;
  }

  Future<List<Map<String,dynamic>>> getinterList(int dummyid,String status) async {
    var intermaplist = await getinterMapList();
    int count = intermaplist.length;
    print('intercount');
    print(count);
    Database db = await databaseHelper.database;
    List<Map<String,dynamic>> interlist = await db.rawQuery('SELECT * FROM ${FarmerAgriInteraction.interactiontable} WHERE ${FarmerAgriInteraction.colaid} = $dummyid ');
    return interlist;
  }
  

}
