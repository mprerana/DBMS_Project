import 'dart:async';
import 'package:flutter/material.dart';
import 'package:dbms_final/farmer/screens/setalarm.dart';
import 'package:dbms_final/farmer/models/clock.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/datbasefiles/clockcrud.dart';
class MyAppmain extends StatefulWidget {

	@override
  State<StatefulWidget> createState() {

    return MyAppmainstate();
  }
}

    
    class MyAppmainstate extends State<MyAppmain>{
      DatabaseHelper databaseHelper=DatabaseHelper();
      List<Clockset> clocklist;
      int count=0;
      @override
      Widget build(BuildContext context){
        if(clocklist==null){
          clocklist=List<Clockset>();
          updatelistview();
        }
      
    return Scaffold(
      appBar:new AppBar(title: new Text('alarms'),
      backgroundColor: Color.fromRGBO(40, 80, 40, 0.8)),
      body:getclocklistview(),
      floatingActionButton: FloatingActionButton(
        onPressed: (){
         navigatetodetail(context,Clockset(null,null,'','',''), 'add alarm');
        },
        child: Icon(Icons.add),
        tooltip: 'Add one more alarm',

      ),
     
      
    );
    
      } 
      ListView getclocklistview(){
        return ListView.builder(
       itemCount: count,
       itemBuilder:(BuildContext context,int position) {
         return Card(
           child:ListTile(
              title: new Text(this.clocklist[position].reason),
              
          trailing: GestureDetector(child:Icon(Icons.delete),
          onTap: (){
            _delete(context, clocklist[position]);
          },
          ),
           onTap:(){
              navigatetodetail(context,this.clocklist[position], 'edit alarm');
             },
           )
         );
       }
            
      );
      }

      void _delete(BuildContext context,Clockset clockset) async{
        int result=await Clockcrudoperations().deleteTime(clockset.idf);
        if(result!=0){
          _showSnackBar(context,'alarm deleted succesful');
          updatelistview();
        }
      }
      void _showSnackBar(BuildContext context,String message){
        final snackBar=SnackBar(content:Text(message));
        Scaffold.of(context).showSnackBar(snackBar);
      }
void navigatetodetail(BuildContext context,Clockset clockset,String title) async{
        bool result=await Navigator.push(context,MaterialPageRoute(builder: (context){
          return MyApp1(clockset,title);
        }));
        if(result==true){
          updatelistview();
        }
      }
      void updatelistview(){
        final Future<Database> dbFuture=databaseHelper.initializeDatabase();
        dbFuture.then((database){
          Future<List<Clockset>>clocklistFuture=Clockcrudoperations().getclocklist();
          clocklistFuture.then((clocklist){
            
            setState(() {
				  this.clocklist = clocklist;
				  this.count = clocklist.length;
				});
          });
        });
      }
      
}