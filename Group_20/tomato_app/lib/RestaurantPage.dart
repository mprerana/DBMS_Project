import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:tomato_app/cart.dart';

var data;

class RestaurantPage extends StatefulWidget {
  RestaurantPage({this.data, this.token});
  final String data;
  final String token;

  @override
  State<StatefulWidget> createState() => new _RestrauntPageState();
}

class _RestrauntPageState extends State<RestaurantPage> {
  void initstate() {
    super.initState();
  }

  Map cart = {};

  void nothing(data) {
    if (cart.containsKey(data)) {
      cart[data]++;
    } else {
      cart[data] = 1;
    }
  }

  checkout(context) {
    print(cart);
    var route1 = new MaterialPageRoute(
        builder: (BuildContext context) =>
            new CartPage(data: cart, token: widget.token));
    Navigator.of(context).push(route1);
  }

  @override
  Widget build(BuildContext context) {
    data = widget.data;
    data = json.decode(data);
    if (data == null) {
      return new Scaffold(
        appBar: new AppBar(
          backgroundColor: Colors.deepOrange,
          title: new Text(
            "Dishes",
            style: TextStyle(fontSize: 25.0, color: Colors.white),
          ),
          actions: <Widget>[
            MaterialButton(
              onPressed: () {
                checkout(context);
              },
              color: Colors.deepOrange,
              child: new Icon(Icons.shopping_cart),
            )
          ],
        ),
        body: Text("No Dishes"),
      );
    } else {
      return new Scaffold(
          appBar: new AppBar(
            backgroundColor: Colors.deepOrange,
            title: new Text(
              "Dishes",
              style: TextStyle(fontSize: 25.0, color: Colors.white),
            ),
            actions: <Widget>[
              MaterialButton(
                onPressed: () {
                  checkout(context);
                },
                color: Colors.deepOrange,
                child: new Icon(Icons.shopping_cart, color: Colors.white),
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
                                    nothing(data[index]);
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
                                            text: data[index]["itemname"]
                                                .toString(),
                                            style: TextStyle(
                                                fontWeight: FontWeight.bold)),
                                        TextSpan(
                                            text: "\nRs. " +
                                                data[index]["price"].toString(),
                                            style: TextStyle(
                                                fontStyle: FontStyle.italic)),
                                        TextSpan(
                                            text: "\n" +
                                                data[index]["description"]
                                                    .toString(),
                                            style: TextStyle(
                                                fontStyle: FontStyle.italic)),
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
