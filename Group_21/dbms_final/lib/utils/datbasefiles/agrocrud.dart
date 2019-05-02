import 'dart:async';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/utils/datbasefiles/databasetables.dart';
import 'package:dbms_final/login/models/agro.dart';
import 'package:dbms_final/servies/authentication.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'package:firebase_auth/firebase_auth.dart';
class Agrocrudoperations{
  DatabaseHelper databaseHelper=DatabaseHelper();
  
  Future<List<Map<String,dynamic>>> getagroMapList() async {
    Database db = await databaseHelper.database;
    
    var result = db.rawQuery('SELECT * FROM ${AgroTable.agroexperttable}');
    return result;
  }

  // insert into table
  Future<int> insertagro(Agro expert1) async {
     Database db = await databaseHelper.database;

    int result = await db.insert(AgroTable.agroexperttable, expert1.toMap());
    return result; 
  }
  //
  Future<List<Agro>> getagroList() async {
    var agromaplist = await getagroMapList();
    int count = agromaplist.length;
    print('agriculturesscount');
    print(count);
    List<Agro> agrolist = List<Agro>();
    for(int i = 0;i<count ;++i) {
      agrolist.add(Agro.fromMapObject(agromaplist[i]));
    }
    print("agricultureexpertlist");
    print(agromaplist);
    //print(agrolist);
    return agrolist;
  }

  Future<List<Map<String,dynamic>>>getcity( )async{

FirebaseUser user = await BaseAuth().getCurrentUser();
    print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);
    print(userrecord);
    print(userrecord['City']);
    var city1=userrecord['City'];

    Database db = await databaseHelper.database;

    List<Map<String,dynamic>> resultList = await db.rawQuery('SELECT * FROM ${UserTable.userTable} WHERE ${UserTable.colCity} = "$city1" AND ${UserTable.colusertype}= "AgricultureExpert"');
   print(resultList);

    return resultList;

  }

}