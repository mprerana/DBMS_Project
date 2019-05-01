import 'package:flutter/material.dart';
import 'package:dbms_final/homepage.dart';
import 'package:dbms_final/agricultureexpert/agriculture.dart';
import 'package:dbms_final/customer/weather.dart';
import 'package:dbms_final/farmer/screens/farmerinterface.dart';
import 'package:dbms_final/servies/authentication.dart';
import 'package:dbms_final/login/screens/login.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:path/path.dart';
import 'package:dbms_final/login/models/user.dart';


class Customer extends StatelessWidget{
  String search;
  int count=0;
  Future<List<Map<String, dynamic>>>usersList;

 String _search;
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar:new AppBar(title:new Directionality(
          textDirection: TextDirection.ltr,
          child: new Text('Customerinterface')
          ),
          backgroundColor:Color.fromRGBO(40, 80, 40, 0.8)
    ),
    
    drawer: new Drawer(
      child:new ListView(
        padding: new EdgeInsets.only(top: 30.0,left:10.0),
          children: <Widget>
          [
            ListTile
           (
              leading: Editimage(),
              title: const Text('Edit Profile'),
              onTap:(){Navigator.push(context,MaterialPageRoute(builder: (context)=>Customer()));},
           ),
           ListTile
           (
              leading: Logoutimage(),
              title: const Text('Logout'),
              onTap:()async{
                await BaseAuth().signOut();
                   Navigator.of(context)
                .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new LoginPage();
            
                }
                )
                );},
           ),
          ],
    ),
    ),
    body: Padding(
        padding: EdgeInsets.all(20.0),
         child:TextFormField(
                decoration: InputDecoration(labelText: 'search', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
                
                onFieldSubmitted: (value) {
                 _search= value ;
                 print('hii');
                  getlistView(value);
                },
              )
            ),
           
        
    );
    

    
    
  }
 ListView getlistView(String value) {
    usersList=Usercrudoperations().getfarmerswithcity(value);
    print(usersList);
    if (usersList==null){
      usersList=Usercrudoperations().getfarmerswithcrop(value);
    }
        return ListView.builder(
      itemCount: count,
      itemBuilder: (BuildContext context,int position) {
        return Card(
          color: Colors.white,
          elevation: 2.0,
          child:new Column(
              children: <Widget>[
                Text(this.usersList.toString()),
              
              ],
            
            
            
          ),
        );
      },
    );
  }
}


