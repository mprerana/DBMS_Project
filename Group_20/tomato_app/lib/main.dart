import 'package:flutter/material.dart';
import 'package:tomato_app/LoginSignUpPage.dart';
import 'package:tomato_app/splash.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Tomato App',
      theme: ThemeData(
      primarySwatch: Colors.deepOrange,
      ),
      home: new SplashScreen(),
      routes: <String, WidgetBuilder>{
        '/LoginScreen': (BuildContext context) => new LoginSignUpPage(),
      },
      debugShowCheckedModeBanner: false,
    );
  }
}

