import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:splash_tokenauth/common/apifunctions/requestLogoutAPI.dart';
import 'package:splash_tokenauth/common/apifunctions/requestQuizData.dart';

var data;
var json1;
var json2;
var token;

void courseInitializer(intoken, inJson, context){
  json1 = inJson;
  json2 = json.decode(inJson);
  token = intoken;
  Navigator.of(context).pushReplacementNamed('/CourseScreen');
}

class CourseScreen extends StatefulWidget {
  @override
  _CourseScreenState createState() =>  _CourseScreenState();
}

class _CourseScreenState extends State<CourseScreen> {
    
  final String url = "http://10.0.36.104:8000/quiz/listquizzes/course_id";

  @override
  void initState() {
    super.initState();
    _saveCurrentRoute("/CourseScreen");
  }

  _saveCurrentRoute(String lastRoute) async {
    SharedPreferences preferences = await SharedPreferences.getInstance();
    await preferences.setString('LastScreenRoute', lastRoute);
  }

void back(){
  Navigator.of(context).pushReplacementNamed('/HomeScreen');
}

@override
Widget build(BuildContext context){
  if(json2 == null)
  return new Scaffold(body: Text("No Data"),);
  
  return new Scaffold(
    appBar: new AppBar(
      title: new Text("Quizzes", style: TextStyle(fontSize: 25.0, color: Colors.white),),
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
                      onPressed: (){getQuizJsonData(token, context, json2[index]["quizid"]);},
                      color: Colors.white,
                    padding: const EdgeInsets.all(30.0),
                    child: new Container(
                    child: new RichText(
                      text: TextSpan(text: "", style: DefaultTextStyle.of(context).style,
                      children: <TextSpan>[
                        TextSpan(text: "Quiz Name: "+json2[index]["quizname"].toString(), style: TextStyle(fontWeight: FontWeight.bold)),                
                        TextSpan(text: "\nQuiz ID: "+json2[index]["quizid"].toString(), style: TextStyle(fontStyle: FontStyle.italic)),
                        TextSpan(text: "\nStarted on: "+json2[index]["starttime"].toString(), style: TextStyle(fontStyle: FontStyle.italic)),
                        TextSpan(text: "\nEnding on: "+json2[index]["endtime"].toString(), style: TextStyle(fontStyle: FontStyle.italic)),
                        json2[index]["name"]!=null?
                        TextSpan(text: "\nFaculty Name: "+json2[index]["name"].toString(), style: TextStyle(fontStyle: FontStyle.italic)):
                        TextSpan(text: ""),
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