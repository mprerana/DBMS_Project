import 'package:sqflite/sqflite.dart';
import 'dart:async';  
import 'dart:io';
import 'package:path_provider/path_provider.dart';
import 'package:dbms_final/utils/datbasefiles/triggers.dart';
import 'package:dbms_final/utils/datbasefiles/view.dart';
import 'package:dbms_final/utils/datbasefiles/databasetables.dart';

import 'package:dbms_final/utils/populate_database.dart';
class DatabaseHelper{
static DatabaseHelper _databaseHelper;
static Database _database;
DatabaseHelper._createInstance();
factory DatabaseHelper(){
  if(_databaseHelper==null){
    _databaseHelper=DatabaseHelper._createInstance();
  }

return _databaseHelper;
}
Future<Database>get database async{
  if(_database==null){
    _database=await initializeDatabase();
  }
  return _database;
}
Future<Database>initializeDatabase() async{
  Directory directory=await getApplicationDocumentsDirectory();
  String path=directory.path+'tyuiioop.db';
  deleteDatabase(path);
  Future <Database> projectDatabase=openDatabase(path,version:1,onCreate: _createDb);
  return projectDatabase;
}
void _createDb(Database db,int newVersion) async{
   await db.execute('PRAGMA foreign_keys = ON');
   await db.execute(UserTable.createtable);
   await db.execute(FarmerTable.createtable);
   await db.execute(AgroTable.createtable);
   await db.execute(ClockTable.createtable);
   await db.execute(Trigdelclock.createTable);
   await db.execute(Trigupclock.createtable);
   await db.execute(Trigupfarm.createtable);
   await db.execute(FarmerAgriInteraction.createTable);
   await db.execute(Farmercrop.createtable);
 
   print('tablescreated'); 
  await db.execute(Triggers.triggerdeletealarm);
 await db.execute(Triggers.triggerupdatefarmertable);
 await db.execute(Triggers.triggerupdatealarm);
   print('triggers created succesful');
  await db.execute(Views.getagricultureslist);
   await db.execute(Views.getcustomerslist);
   await db.execute(Views.getfarmerslist);
   print('view succesful');
   await db.execute(UserTable.indexSQL);
   print('index successfull');
   //InitData();
   print('populated database');
}



}