import 'package:flutter/material.dart';


class Seeds extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar:new AppBar(title:new Directionality(
          textDirection: TextDirection.ltr,
          child: new Text('Farmerinterface')
          ),
          backgroundColor:Colors.lightGreenAccent
    ),
    
    );
  }
}