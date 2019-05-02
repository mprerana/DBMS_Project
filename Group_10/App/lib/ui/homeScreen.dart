import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:async';
import 'package:splash_tokenauth/common/apifunctions/requestLogoutAPI.dart';
import 'package:splash_tokenauth/common/apifunctions/requestCourseData.dart';
import 'package:splash_tokenauth/common/functions/createCourse.dart';
import 'package:splash_tokenauth/common/functions/joinCourse.dart';


var data = [];
var token;
var data1;

final TextEditingController _courseName = TextEditingController();

void initializer(intoken, indata, context){
  data = indata;
  token = intoken;
  teacherInitializer(intoken, indata, context);
  Navigator.of(context).pushReplacementNamed('/HomeScreen');
}

bool _isTeacher = false;
Future<String> teacherInitializer(intoken, indata, context)async{
  final String url = "http://10.0.36.104:8000/api/auth/me";
  var response = await http.get(Uri.encodeFull(url), headers: {"Accept": "application/json", "x-access-token": intoken});
  var responseJson = json.decode(response.body);
  _isTeacher = (responseJson != null && !responseJson.isEmpty) ? responseJson[0]["isTeacher"] : false;
  data1 = indata;
  return "Success";
}


class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() =>  _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {

  @override
  void initState() {
    super.initState();
    _saveCurrentRoute("/HomeScreen");
  }

  _saveCurrentRoute(String lastRoute) async {
    SharedPreferences preferences = await SharedPreferences.getInstance();
    await preferences.setString('LastScreenRoute', lastRoute);
  }

@override
Widget build(BuildContext context){
  
  try{
  return new Scaffold(
    appBar: new AppBar(
      title: new Text("Your Courses", style: TextStyle(fontSize: 25.0, color: Colors.white),),
      actions: <Widget>[MaterialButton(
        onPressed:(){ requestLogout(context);},
        color: Colors.blue,
        child: Text("Logout", style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),),
      )],
    ),
    body: new ListView.builder(
      itemCount: data == null ? 0 : data.length,
      itemBuilder: (BuildContext context , int index){
        return new Container(
          child: new Center(
            child: new Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                new Card(
                  child: new Container(
                    child: RaisedButton(
                      onPressed: (){getCourseJsonData(token, context, data[index]["cid"]);},
                      color: Colors.white,
                      padding: const EdgeInsets.all(30.0),
                      child: new Container(
                      child: new RichText(
                      text: TextSpan(text: "", style: DefaultTextStyle.of(context).style,
                      children: <TextSpan>[
                        TextSpan(text: "Course Name: "+data[index]["cname"].toString(), style: TextStyle(fontWeight: FontWeight.bold)),                   
                        TextSpan(text: "\nCourse ID: "+data[index]["cid"].toString(), style: TextStyle(fontStyle: FontStyle.italic)),
                        data[index]["name"]!=null?
                        TextSpan(text: "\nFaculty Name: "+data[index]["name"].toString(), style: TextStyle(fontStyle: FontStyle.italic)):
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
    ),
    floatingActionButton: new FloatingActionButton(
      tooltip: 'Add',
      child: new Icon(Icons.add),
      backgroundColor: Colors.blue,
      onPressed: (){
        showDialog(context: context, child:
      new AlertDialog(
      title: _isTeacher? new Text("Create Course") : new Text("Join Course"),
      content: TextField(
                    controller: _courseName,
                    decoration: InputDecoration(
                      labelText: _isTeacher ? "Course Name" : "Join Key",
                    ),
                    style: TextStyle(fontSize: 22.0, color: Colors.black, fontWeight: FontWeight.bold, ),
                  ),
      actions: <Widget>[
        _isTeacher ? RaisedButton(child:Text("Create", style: TextStyle(color: Colors.white),), onPressed:(){createCourse(context, token, _courseName.text);}):
                     RaisedButton(child:Text("Join", style: TextStyle(color: Colors.white),), onPressed:(){joinCourse(context, token, _courseName.text);})
      ],
    )
    );
      }     
    ),
  );
  }
  catch (e){
    return Scaffold(body: Text("No data"),);
  }
}
}