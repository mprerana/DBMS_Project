import 'package:flutter/material.dart';

import 'package:splash_tokenauth/ui/homeScreen.dart';
import 'package:splash_tokenauth/ui/loginScreen.dart';
import 'package:splash_tokenauth/ui/splashScreen.dart';
import 'package:splash_tokenauth/ui/courseScreen.dart';
import 'package:splash_tokenauth/ui/quizScreen.dart';
import 'package:splash_tokenauth/ui/signupScreen.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {

  // var _splashShown = false;

  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: "QuazApp Login",
      routes: <String,WidgetBuilder>{
        "/HomeScreen": (BuildContext context) => HomeScreen(),
        "/LoginScreen": (BuildContext context) => LoginScreen(),
        "/CourseScreen": (BuildContext context) => CourseScreen(),
        "/QuizScreen": (BuildContext context) => QuizScreen(),
        "/SignupScreen": (BuildContext context) => SignupScreen(),
      },
      home: SplashScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
