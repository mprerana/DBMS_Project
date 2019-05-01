import 'package:flutter/material.dart';
import 'package:dbms_final/agricultureexpert/agriculture.dart';
import 'package:dbms_final/customer/customer.dart';

class Homepage extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar:new AppBar(title:new Directionality(
          textDirection: TextDirection.ltr,
          child: new Text('Agriculture App')
          ),
          backgroundColor:Colors.lightGreenAccent
    ),
    drawer: new Drawer(
      child:new ListView(
        padding: new EdgeInsets.only(top: 30.0,left:10.0),
          children: <Widget>
          [
            
            ListTile
            (
              title: const Text('farmerinterface'),
               leading: Farmerimage(),
              //onTap:(){Navigator.push(context,MaterialPageRoute(builder: (context)=>Farmerinterface()));},
              
            ),
           ListTile
           (
              leading: Customerimage(),
              title: const Text('customer'),
              onTap:(){Navigator.push(context,MaterialPageRoute(builder: (context)=>Customer()));},
           ),
           ListTile
           (
              leading: Agricultureimage(),
              title: const Text('agriculture'),
              onTap:(){Navigator.push(context,MaterialPageRoute(builder: (context)=>Viewagro()));},
           ),
          ],
    ),
    ),
    );
  }

}

class Farmerimage extends StatelessWidget{
    @override
    Widget build(BuildContext context){
      AssetImage assetImage =AssetImage('images/farmericon.jpg');
      Image farmerimage=Image(image:assetImage,width:30,height: 30,);
      return Container(child: farmerimage);
    }
  }
 class Editimage extends StatelessWidget{
    @override
    Widget build(BuildContext context){
      AssetImage assetImage =AssetImage('images/edit.png');
      Image editimage=Image(image:assetImage,width:30,height: 30,);
      return Container(child: editimage);
    }
  }
  class Newsimage extends StatelessWidget{
    @override
    Widget build(BuildContext context){
      AssetImage assetImage =AssetImage('images/news.jpg');
      Image editimage=Image(image:assetImage,width:30,height: 30,);
      return Container(child: editimage);
    }
  }
class Customerimage extends StatelessWidget{
    @override
    Widget build(BuildContext context){
      AssetImage assetImage =AssetImage('images/customericon.png');
      Image customerimage=Image(image:assetImage,width:30,height: 30,);
      return Container(child: customerimage);
    }
  }

 class Logoutimage extends StatelessWidget{
    @override
    Widget build(BuildContext context){
      AssetImage assetImage =AssetImage('images/logout.png');
      Image logoutimage=Image(image:assetImage,width:30,height: 30,);
      return Container(child: logoutimage);
    }
  }
class Agricultureimage extends StatelessWidget{
    @override
    Widget build(BuildContext context){
      AssetImage assetImage =AssetImage('images/agricultureicon.jpg');
      Image agricultureimage=Image(image:assetImage,width:30,height: 30,);
      return Container(child: agricultureimage);
    }
  }

