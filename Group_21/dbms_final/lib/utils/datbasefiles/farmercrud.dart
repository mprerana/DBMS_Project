import 'dart:async';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/utils/datbasefiles/databasetables.dart';
import 'package:dbms_final/login/models/farmer.dart';
class Farmercrudoperations{
  DatabaseHelper databaseHelper=DatabaseHelper();
  Future<List<Map<String,dynamic>>> getfarmerMapList() async {
    Database db = await databaseHelper.database;


    var result = db.rawQuery('SELECT * FROM ${FarmerTable.farmertable} ORDER BY ${FarmerTable.colId} ASC');
    return result;
  }

  // insert into table
  Future<int> insertfarmer(Farmer farmer1) async {
    Database db = await databaseHelper.database;

    

    int result = await db.insert(FarmerTable.farmertable, farmer1.toMap());
    
    return result;
  }
  Future<List<Farmer>> getfarmerList() async {
    var farmermaplist = await getfarmerMapList();
    int count = farmermaplist.length;
    print('farmerscount');
    print(count);
    List<Farmer> farmerslist = List<Farmer>();
    for(int i = 0;i<count ;++i) {
      farmerslist.add(Farmer.fromMapObject(farmermaplist[i]));
    }
    print("farmerlist");
    print(farmermaplist);
    return farmerslist;
  }

}