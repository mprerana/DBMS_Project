import 'dart:async';

import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';

import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/login/models/user.dart';

import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';

class ViewUsers extends StatefulWidget {

  @override
  State<StatefulWidget> createState() {
    return _ViewUsersState();
  }
}

class _ViewUsersState extends State<ViewUsers> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  List<User> userList;
  int count = 0;

  @override
  Widget build(BuildContext context) {

    if(userList == null) {
      userList = List<User>();
      updateUserListView();
    }
    
    

    return Scaffold(
      appBar: AppBar(
        title: Text('All Users'),
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
            title: Text(this.userList[position].email, style: textStyle),
            
            
            
          ),
        );
      },
    );
  }

  

  

  void updateUserListView() {
    final Future<Database> dbFuture = databaseHelper.database;
    dbFuture.then((database) {
      Future<List<User>> userlistfuture = Usercrudoperations().getUserList();
      userlistfuture.then((userlistfuture) {
        setState(() {
        this.userList = userlistfuture;
        this.count = userlistfuture.length; 
        });
      });
    });
  }
  
}