import 'package:dbms_final/customer/models/newsdata.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';


class Newsview extends StatelessWidget {
  final NewsData news;
  Newsview({Key key, @required this.news}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text(news.description.toString(),  style: new TextStyle(color: Colors.green, fontSize: 30.0)),
        
        Text(news.content.toString(),  style: new TextStyle(color: Colors.green, fontSize: 10.0)),
              ],
    );
  }
}