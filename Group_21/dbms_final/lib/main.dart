import 'package:flutter/material.dart';
import 'package:dbms_final/login/screens/login.dart';
void main()=>runApp(AgricultureApp());
class AgricultureApp extends StatelessWidget{
  @override
  Widget build(BuildContext conntext){
    return MaterialApp(
      title:'AgricultureApp',
     debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: LoginPage(),
    );
  }
}