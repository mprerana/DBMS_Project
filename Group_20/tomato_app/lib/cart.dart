import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:tomato_app/homePage.dart';
import 'package:http/http.dart' as http;


class CartPage extends StatefulWidget {
  CartPage({this.data, this.token});

  final Map data;
  final String token;

  @override
  State<StatefulWidget> createState() => new _CartPageState();
}

class _CartPageState extends State<CartPage> {
  void initstate() {
    super.initState();
  }

  place_order(dat) async {
     var urrl = "192.0.34.149:3000/user/createorder/";
     var response = await http.post(Uri.encodeFull(urrl),
         headers: {"Accept": "application/json", "Authorization": token},
         body: dat);

    if (response.statusCode == 200) {
    Fluttertoast.showToast(
        msg: "Order Placed Successfully",
        toastLength: Toast.LENGTH_SHORT,
        gravity: ToastGravity.BOTTOM,
        timeInSecForIos: 1,
        textColor: Colors.white,
        backgroundColor: Colors.grey[850],
        fontSize: 16.0);
    redirect();
  }}

  void redirect() {
    var route = new MaterialPageRoute(
      builder: (BuildContext context) => new HomePage(token: widget.token),
    );
    Navigator.of(context).push(route);
  }

  @override
  Widget build(BuildContext context) {
    var items = widget.data;
    print(items);
    List<Map> data = [];
    Map req = {};
    int cost = 0;
    items.forEach((k, v) {
      data.add(k);
      cost = cost + (k["price"] as int) * (v as int);
      data[data.indexOf(k)]["Quantity"] = v.toString();
      req[k["id"]] = v;
    });
    return new Scaffold(
      appBar: new AppBar(
        backgroundColor: Colors.deepOrange,
        title: new Text(
          "Your Cart",
          style: TextStyle(fontSize: 25.0, color: Colors.white),
        ),
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
                              onPressed: () {},
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
                                            data[index]["itemname"].toString(),
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
                                    TextSpan(
                                        text: "\n" +
                                            data[index]["Quantity"].toString(),
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
          }),
      floatingActionButton: new Padding(
        padding: EdgeInsets.all(10),
        child: new RaisedButton(
          elevation: 5.0,
          color: Colors.deepOrange,
          onPressed: place_order(req),
          child: new Text('Pay Rs ' + cost.toString(),
              style: TextStyle(
                  color: Colors.white,
                  fontSize: 15,
                  fontWeight: FontWeight.w700)),
        ),
      ),
    );
  }
}
