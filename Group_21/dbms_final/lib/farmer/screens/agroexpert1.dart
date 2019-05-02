import 'dart:async';

import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';

import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/farmer/screens/indiagro1.dart';
//import 'package:dbms_final/login/models/user.dart';

import 'package:dbms_final/utils/datbasefiles/agrocrud.dart';
class Viewcityagro extends StatefulWidget {
 
  @override
  State<StatefulWidget> createState() {
    return _ViewcityState();
  }
}

class _ViewcityState extends State<Viewcityagro> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  
  List<Map<String,dynamic>>cityagroList;
  int count = 0;

  @override
  Widget build(BuildContext context) {

    if(cityagroList == null) {
      cityagroList = List<Map<String,dynamic>>();
      updatecityagroListView();
    }
    
    

    return Scaffold(
      appBar: AppBar(
        title: Text('All Users'),
         backgroundColor: Color.fromRGBO(40, 80, 40, 0.8),
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
        return 
        Container(
          
          child:Card(
          color: Colors.white,
          elevation: 2.0,
          
          child: ListTile(
            title: Text(this.cityagroList[position]['Firstname'].toString(), style: textStyle),
            subtitle: Text(this.cityagroList[position]['mobileno'].toString()),
             onTap:(){
              Navigator.push(context,MaterialPageRoute(builder: (context)=>Individualexpert(cityagro:cityagroList[position]),
               ),
              );
             },
                
                ),
          ),
         
        decoration: new BoxDecoration(boxShadow:[
            new BoxShadow(
              color:Colors.green[200],
              blurRadius: 20.0,
            ),
        ],
        ),
      
    
     );
      }
            
          );
      
  }

  
void navigatetodetail(BuildContext context, Map<String,dynamic> cityagroList){
     

}
  

  
  void updatecityagroListView() {
    final Future<Database> dbFuture = databaseHelper.database;
    dbFuture.then((database) {
      Future<List<Map<String,dynamic>>> cityagrofuture = Agrocrudoperations().getcity();
      cityagrofuture.then((cityagrofuture) {
        setState(() {
        this.cityagroList = cityagrofuture;
        this.count = cityagrofuture.length; 
        });
      });
    });
  }
}