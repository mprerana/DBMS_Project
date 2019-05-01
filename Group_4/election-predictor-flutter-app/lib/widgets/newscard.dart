import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:url_launcher/url_launcher.dart';

import '../scoped_models/main.dart';
import '../models/news.dart';

class NewsCard extends StatelessWidget {
  final News single_news;

  NewsCard(this.single_news);

  Future _launchURL(String url) async {
    if (await canLaunch(url)) {
      launch(url, forceSafariVC: true, forceWebView: true);
    } else {
      print('cant launch ${url}');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Card(
        margin: EdgeInsets.all(15.0),
        child: Column(
          children: <Widget>[
            Container(
              padding: EdgeInsets.all(20.0),
              child: Text(
                single_news.title,
                style: TextStyle(
                  fontSize: 25.0,
                  fontWeight: FontWeight.bold,
                  fontFamily: 'Oswald',
                ),
              ),
            ),
            ScopedModelDescendant<MainModel>(
                builder: (BuildContext context, Widget child, MainModel model) {
              return ButtonTheme(
                  minWidth: 250.0,
                  height: 50.0,
                  child: FlatButton(
                    child: Text('details'),
                    color: Colors.greenAccent,
                    onPressed: () {
                      model.setUrl(single_news.url);
                      _launchURL(single_news.url);
                    },
                    shape: new RoundedRectangleBorder(
                        borderRadius: new BorderRadius.circular(5.0)),
                  ));
            }),
            SizedBox(
              height: 15.0,
            ),
          ],
        ),
      ),
      decoration: new BoxDecoration(boxShadow: [
        new BoxShadow(
          color: Colors.black26,
          blurRadius: 0.0,
        ),
      ]),
    );
  }
}
