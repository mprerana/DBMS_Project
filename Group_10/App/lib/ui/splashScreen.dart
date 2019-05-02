import 'dart:async';
import 'package:flutter/material.dart';




class SplashScreen extends StatefulWidget {
  @override
  _SplashScreenState createState() =>  _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  final int splashDuration = 2;

  startTime() async {
    return Timer(
        Duration(seconds: splashDuration),
            () {
          Navigator.of(context).pushReplacementNamed('/LoginScreen');
        }
    );
  }

  Widget _showLogo(){
    return new Hero(
      tag: 'hero' ,
      child: Padding(
        padding: EdgeInsets.fromLTRB(80.0, 0.0, 80.0, 0.0),
        child: Image.asset('assets/quazapp_logo.jpg'),
      ),
    );
  }

  @override
  void initState() {
    super.initState();
    startTime();
  }

  @override
  Widget build(BuildContext context) {
    var drawer = Drawer();

    return Scaffold(drawer: drawer,
        body: Container(
            decoration: BoxDecoration(color: Colors.blue),
            child: Column(
              children: <Widget>[
                 Container(alignment: Alignment.topCenter,
                    child: Padding(padding: EdgeInsets.fromLTRB(0.0, 200.0, 0.0, 30.0),
                      child: Text("QuazApp", style: TextStyle(fontSize: 60.0, color: Colors.white),),
                    )
                ),
                _showLogo(),
              ],
            )
        )
    );
  }
}