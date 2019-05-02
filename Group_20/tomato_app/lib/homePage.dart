import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:http/http.dart' as http;
import 'package:tomato_app/RestaurantPage.dart';

var data;
var token;

void initializer(indata, context, intoken) {
  data = indata;
  token = intoken;
}

class HomePage extends StatefulWidget {
  HomePage({this.token});

  final String token;

  @override
  State<StatefulWidget> createState() => new _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void initState() {
    super.initState();
  }

  final String url = "http://10.0.34.149:3000/user/restaurant/";

  void requestLogout(BuildContext context) {
    Fluttertoast.showToast(
        msg: "Logged out",
        toastLength: Toast.LENGTH_SHORT,
        gravity: ToastGravity.BOTTOM,
        timeInSecForIos: 1,
        textColor: Colors.white,
        fontSize: 16.0);
    Navigator.of(context).pushReplacementNamed('/LoginScreen');
  }

  Future<String> nothing(cid) async {
    var urrl = url + cid;
    var response = await http.get(Uri.encodeFull(urrl),
        headers: {"Accept": "application/json", "Authorization": token});
    var route1 = new MaterialPageRoute(
        builder: (BuildContext context) =>
            new RestaurantPage(data: response.body, token: token));
    Navigator.of(context).push(route1);
    return null;
  }

  @override
  Widget build(BuildContext context) {
    if (data == null) {
      return new Scaffold(
        appBar: new AppBar(
          backgroundColor: Colors.deepOrange,
          title: new Text(
            "Restaurants",
            style: TextStyle(fontSize: 25.0, color: Colors.white),
          ),
          actions: <Widget>[
            MaterialButton(
              onPressed: () {
                requestLogout(context);
              },
              color: Colors.deepOrange,
              child: new Text(
                "Logout",
                style: new TextStyle(
                    fontSize: 15.0,
                    color: Colors.white,
                    fontWeight: FontWeight.w500),
              ),
            )
          ],
        ),
        body: Text("No Restaurants"),
      );
    } else {
      return new Scaffold(
          appBar: new AppBar(
            backgroundColor: Colors.deepOrange,
            title: new Text(
              "Restaurants",
              style: TextStyle(fontSize: 25.0, color: Colors.white),
            ),
            actions: <Widget>[
              MaterialButton(
                onPressed: () {
                  requestLogout(context);
                },
                color: Colors.deepOrange,
                child: new Text(
                  "Logout",
                  style: new TextStyle(
                      fontSize: 15.0,
                      color: Colors.white,
                      fontWeight: FontWeight.w500),
                ),
              )
            ],
          ),
          body: new ListView.builder(
              itemCount: data == null ? 0 : data.length,
              itemBuilder: (BuildContext context, int index) {
                return new Container(
                  child: new Center(
                    child: new Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: <Widget>[
                        new Card(
                          child: new Container(
                              child: RaisedButton(
                                  onPressed: () {
                                    nothing(data[index]["username"].toString());
                                  },
                                  color: Colors.white,
                                  padding: const EdgeInsets.all(30.0),
                                  child: new Container(
                                      child: new RichText(
                                    text: TextSpan(
                                      text: "",
                                      style: DefaultTextStyle.of(context).style,
                                      children: <TextSpan>[
                                        TextSpan(
                                            text:
                                                data[index]["name"].toString(),
                                            style: TextStyle(
                                                fontWeight: FontWeight.bold)),
                                        // TextSpan(text: "\n", style: TextStyle(fontWeight: FontWeight.bold)),
                                        TextSpan(
                                            text: "\n" +
                                                data[index]["address"]
                                                    .toString(),
                                            style: TextStyle(
                                                fontStyle: FontStyle.italic)),
                                        TextSpan(
                                            text: "\n" +
                                                data[index]["openinghrs"]
                                                    .toString() +
                                                " to ",
                                            style: TextStyle(
                                                fontStyle: FontStyle.italic)),
                                        TextSpan(
                                            text: data[index]["closinghrs"]
                                                .toString(),
                                            style: TextStyle(
                                                fontStyle: FontStyle.italic)),
                                        //TextSpan(text: "\nURL" + data[index]["logo"].toString(), style: TextStyle(fontStyle: FontStyle.italic)),
                                        // TextSpan(text: "\n", style: TextStyle(fontWeight: FontWeight.bold)),
                                        data[index]["phone"] != null
                                            ? TextSpan(
                                                text: "\nPhone: " +
                                                    data[index]["phone"]
                                                        .toString(),
                                                style: TextStyle(
                                                    fontStyle:
                                                        FontStyle.italic))
                                            : TextSpan(text: ""),
                                      ],
                                    ),
                                  )))),
                        ),
                      ],
                    ),
                  ),
                );
              }));
    }
  }
}
