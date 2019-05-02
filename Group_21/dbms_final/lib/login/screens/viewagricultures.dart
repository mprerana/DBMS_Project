import 'dart:async';

import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';

import 'package:dbms_final/utils/dbhelper.dart';

import 'package:dbms_final/login/models/agro.dart';

import 'package:dbms_final/utils/datbasefiles/agrocrud.dart';
class Viewagricultures extends StatefulWidget {

  @override
  State<StatefulWidget> createState() {
    return _ViewagriculturesState();
  }
}

class _ViewagriculturesState extends State<Viewagricultures> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  
  List<Agro>agroList;
  int count = 0;

  @override
  Widget build(BuildContext context) {

    if(agroList == null) {
      agroList = List<Agro>();
      updateagricultureexpertListView();
    }
    
    

    return Scaffold(
      appBar: AppBar(
        title: Text('Agriculture Expert'),
        backgroundColor: Color.fromRGBO(40, 80, 40,0.8),
      ),
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: getlistView(),
      ),
    );
  }

  ListView getlistView() {
    TextStyle textStyle = Theme.of(context).textTheme.subhead;
    return ListView.builder(
      itemCount: count,
      itemBuilder: (BuildContext context,int position) {
        return Card(
          color: Colors.white,
          elevation: 2.0,
          child: ListTile(
            title: Text((this.agroList[position].id).toString(), style: textStyle),
            
            
            
          ),
        );
      },
    );
  }

  

  

  
  void updateagricultureexpertListView(){
    final Future<Database> dbFuture = databaseHelper.database;
    dbFuture.then((database) {
      Future<List<Agro>> agrolistfuture = Agrocrudoperations().getagroList();
      agrolistfuture.then((agrolistfuture) {
        setState(() {
        this.agroList = agrolistfuture;
        this.count = agrolistfuture.length; 
        });
      });
    });
  }
}