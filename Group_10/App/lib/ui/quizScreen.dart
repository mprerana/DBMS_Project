import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:async';
import 'package:splash_tokenauth/common/apifunctions/requestLogoutAPI.dart';
import 'package:http/http.dart' as http;

bool _isTeacher = false;
Future<String> teacherInitializer(intoken, indata, context)async{
  final String url = "http://10.0.36.104:8000/api/auth/me";
  var response = await http.get(Uri.encodeFull(url), headers: {"Accept": "application/json", "x-access-token": intoken});
  var responseJson = json.decode(response.body);
  _isTeacher = (responseJson != null && !responseJson.isEmpty) ? responseJson[0]["isTeacher"] : false;
  return "Success";
}


var data;
var json1;
var json2;

void quizInitializer(token, inJson, context){
  json1 = inJson;
  json2 = json.decode(inJson);
  teacherInitializer(token, inJson, context);
  Navigator.of(context).pushReplacementNamed('/QuizScreen');
}


class QuizScreen extends StatefulWidget {
  @override
  _QuizScreenState createState() =>  _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {

  @override
  void initState() {
    super.initState();
    _saveCurrentRoute("/QuizScreen");
  }

  _saveCurrentRoute(String lastRoute) async {
    SharedPreferences preferences = await SharedPreferences.getInstance();
    await preferences.setString('LastScreenRoute', lastRoute);
  }


void back(){
  Navigator.of(context).pushReplacementNamed('/CourseScreen');
}

void doNothing(){}

@override
Widget build(BuildContext context){
  return new Scaffold(
    appBar: new AppBar(
      title: new Text("Quiz Result", style: TextStyle(fontSize: 25.0, color: Colors.white),),
      actions: <Widget>[MaterialButton(
        onPressed:(){ requestLogout(context);},
        color: Colors.blue,
        child: Text("Logout", style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),),
      ),
    ],
    leading: IconButton(icon: Icon(Icons.arrow_back), onPressed:(){ back();}),
    ),
    body: new ListView.builder(
       itemCount: json2 == null ? 0 : json2.length,
      itemBuilder: (BuildContext context , int index){
        return new Container(
          child: new Center(
            child: new Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                new Card(
                  child: new Container(
                    child: RaisedButton(
                      onPressed: (){doNothing();},
                      color: Colors.white,
                    padding: const EdgeInsets.all(30.0),
                    child: new Container(
                    child: new RichText(
                      text: TextSpan(text: "", style: DefaultTextStyle.of(context).style,
                      children: <TextSpan>[
                        TextSpan(text: "Quiz Name: "+json2[index]["quizname"].toString(), style: TextStyle(fontWeight: FontWeight.bold)),                      
                        _isTeacher==true? TextSpan(text: "\nStudent UserID: "+json2[index]["username"].toString(), style: TextStyle(fontStyle: FontStyle.italic)):TextSpan(text:""),
                                          TextSpan(text: "\nMarks: "+json2[index]["marks"].toString(), style: TextStyle(fontStyle: FontStyle.italic)),
                      ],
                    ),
                  )
                    )
                  )
                  ),
                ),
              ],
            ),
          ),
        );
      }
    )
  );
}
}

void doNothing() {
}