import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:flutter_webview_plugin/flutter_webview_plugin.dart';

import '../scoped_models/main.dart';
import '../models/news.dart';

class NewsDetailPage extends StatefulWidget {
  final MainModel model;

  NewsDetailPage(this.model);

  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _NewsDetailPageState();
  }
}

  Future _launchURL(String url) async {
    if(await canLaunch(url)){
      launch(url, forceSafariVC: true, forceWebView: true);
    }else{
      print('cant launch ${url}');
    }
  }

class _NewsDetailPageState extends State<NewsDetailPage> {
  void _opennewpage() {
    Navigator.pushNamed(context, '/webview');
  }

//  final webView = FlutterWebviewPlugin();
//  TextEditingController controller = TextEditingController(text: widget.model.selectedUrl);
//
//  @override
//  void initState() {
//    super.initState();
//
//    webView.close();
//    controller.addListener(() {
//      url = controller.text;
//    });
//  }
//
//  @override
//  void dispose() {
//    webView.dispose();
//    controller.dispose();
//    super.dispose();
//  }
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return WillPopScope(
          onWillPop: () {
            print('back button presses');
            Navigator.pop(context, false);
            return Future.value(false);
          },
          child: ScopedModelDescendant<MainModel>(
              builder: (BuildContext context, Widget child, MainModel model) {
            final News news = model.allnews[model.selectedIndex];
            print('news details main');
            print(news);
            return Scaffold(
              appBar: AppBar(
                title: Text(news.title),
              ),
              body: Column(
                children: <Widget>[
                  Container(
                    padding: EdgeInsets.all(20.0),
                    child: Text(
                      news.description,
                      style: TextStyle(
                        fontSize: 20.0,
                      ),
                    ),
                  ),
                  Center(
                    child: FlatButton(
                      onPressed: () {
                        model.setUrl(news.url);
                        _launchURL(news.url);
                        //_opennewpage();

                      },
                      child: Text('further details'),
                    ),
                  ),
                ],
              ),
            );
          }),
        );

  }
}

//true, true closes the app
//true, false goes back but deletes the product.
//false, true closes the app
//false, false goes back, product saved.
//remove navigator.pop statement(false), no back allowed
//remove navigator.pop statement(true), back allowed, but null returned
//remove return (false), back allowed, but null returned
//remove return (true), back allowed, product deleted.
