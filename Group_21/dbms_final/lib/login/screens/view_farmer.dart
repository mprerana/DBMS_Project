import 'dart:async';

import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';

import 'package:dbms_final/utils/dbhelper.dart';

import 'package:dbms_final/login/models/farmer.dart';

import 'package:dbms_final/utils/datbasefiles/farmercrud.dart';
class Viewfarmers extends StatefulWidget {

  @override
  State<StatefulWidget> createState() {
    return _ViewfarmersState();
  }
}

class _ViewfarmersState extends State<Viewfarmers> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  
  List<Farmer>farmersList;
  int count = 0;

  @override
  Widget build(BuildContext context) {

    if(farmersList == null) {
      farmersList = List<Farmer>();
      updatefarmerListView();
    }
    
    

    return Scaffold(
      appBar: AppBar(
        title: Text('land details'),
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
            title: Text(this.farmersList[position].latitude, style: textStyle),
            
            
            
          ),
        );
      },
    );
  }

  

  

  
  void updatefarmerListView() {
    final Future<Database> dbFuture = databaseHelper.database;
    dbFuture.then((database) {
      Future<List<Farmer>> farmerlistfuture = Farmercrudoperations().getfarmerList();
      farmerlistfuture.then((farmerlistfuture) {
        setState(() {
        this.farmersList = farmerlistfuture;
        this.count = farmerlistfuture.length; 
        });
      });
    });
  }
}