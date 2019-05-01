import 'dart:async';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/utils/datbasefiles/databasetables.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'package:dbms_final/farmer/models/clock.dart';
import 'package:dbms_final/servies/authentication.dart';
import 'package:firebase_auth/firebase_auth.dart';
class Clockcrudoperations{
  DatabaseHelper databaseHelper=DatabaseHelper();
  Future<List<Map<String,dynamic>>>getclockMaplist() async{
  Database db = await databaseHelper.database;
print("what");
FirebaseUser user = await BaseAuth().getCurrentUser();
    //print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);
    String currentuserid=userrecord['id'].toString();
var result = db.rawQuery('SELECT * FROM ${ClockTable.clockTable} WHERE ${ClockTable.colId}=$currentuserid ');
print(result);
print("happened");
return result;
}
Future<int> insertTime(Clockset clock) async{
  Database db = await databaseHelper.database;
  var result=await db.insert(ClockTable.clockTable,clock.toMap());
  var users = await Usercrudoperations().getUserMapList();
  print("users");
  print(users);
  return result;
}
Future<int> updateTime(Clockset clock) async{
  print('hello');
  Database db=await databaseHelper.database;
  //int result=await db.update(${ClockTable.clockTable}, clock.toMap(), where:'${ClockTable.colId}:?,$colclockId:?', whereArgs: [clock.id,clock.idf]);
 int result = await db.update(ClockTable.clockTable, clock.toMap(), where: '${ClockTable.colclockId}=?', whereArgs: [clock.idf]);
 print('result');
  print(result);
  return result;
}
Future<int> deleteTime(int idf) async{
  var db=await databaseHelper.database;
  
  int result=await db.rawDelete('DELETE FROM ${ClockTable.clockTable} WHERE  ${ClockTable.colclockId}=$idf');
  
  return result;
}
Future<int> getCount() async{
  Database db = await databaseHelper.database;
  FirebaseUser user = await BaseAuth().getCurrentUser();
    //print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);
    String currentuserid=userrecord['id'].toString();
  List<Map<String,dynamic>> x=await db.rawQuery('SELECT COUNT(*) from ${ClockTable.clockTable}  WHERE ${ClockTable.colId}=$currentuserid ');
  int result=Sqflite.firstIntValue(x);
  return result;
}
Future<List<Clockset>>getclocklist() async{
  var clockMaplist=await getclockMaplist();
  int count=clockMaplist.length;
  List<Clockset>clocklist=List<Clockset>();
  for(int i=0;i<count;i++){
    clocklist.add(Clockset.fromMapObject(clockMaplist[i]));
  }
  print(clockMaplist);
  return clocklist;
}





}