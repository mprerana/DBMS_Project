import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:url_launcher/url_launcher.dart';

import '../scoped_models/main.dart';
import '../models/news.dart';

import '../widgets/logout.dart';
import '../widgets/newscard.dart';
import '../widgets/loaders/loader_1.dart';

class NewsPage extends StatefulWidget {
  final MainModel model;

  NewsPage(this.model);

  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _NewsPageState();
  }
}

class _NewsPageState extends State<NewsPage> {
  List<News> actual_news = List<News>();
  List<News> displayed_news = List<News>();

  Future _launchURL(String url) async {
    if (await canLaunch(url)) {
      launch(url, forceSafariVC: true, forceWebView: true);
    } else {
      print('cant launch ${url}');
    }
  }

  _listItem(int index) {
    return Container(
      child: Card(
        margin: EdgeInsets.all(15.0),
        child: Column(
          children: <Widget>[
            Container(
              padding: EdgeInsets.all(20.0),
              child: Text(
                displayed_news[index].title,
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
                      model.setUrl(displayed_news[index].url);
                      _launchURL(displayed_news[index].url);
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

  _searchbar() {
    return Padding(
        padding: const EdgeInsets.all(8.0),
        child: TextField(
          decoration: InputDecoration(hintText: 'search..'),
          onChanged: (text) {
            text = text.toLowerCase();
            setState(() {
              displayed_news = actual_news.where((news) {
                var title = news.title.toLowerCase();
                return title.contains(text);
              }).toList();
            });
          },
        ));
  }

  Widget _buildNewsList(List<News> news) {
    print(news.length);
    if (news.length > 0) {
      return ListView.builder(
        itemBuilder: (BuildContext context, int index) {
          //return NewsCard(news[index]);
          return index == 0 ? _searchbar() : _listItem(index - 1);
        },
        itemCount: news.length + 1,
      );
    } else {
      return Container(
        child: Center(
          child: Text('no news found'),
        ),
      );
    }
  }

  Widget _news() {
    actual_news = widget.model.displayNews;
    displayed_news = actual_news;
    return ScopedModelDescendant<MainModel>(
      builder: (BuildContext context, Widget child, MainModel model) {
        return model.isLoading
            ? Center(child: ColorLoader2())
            : _buildNewsList(actual_news);
      },
    );
  }

  @override
  void initState() {
    widget.model.fetchNews().then((value) {
      setState(() {
        actual_news.addAll(widget.model.displayNews);
        displayed_news = actual_news;
      });
    });
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return WillPopScope(
        onWillPop: () {
          print('back button presses');
          Navigator.pop(context, false);
          return Future.value(false);
          //true, true closes the app
          //true, false goes back but deletes the product.
          //false, true closes the app
          //false, false goes back, product saved.
          //remove navigator.pop statement(false), no back allowed
          //remove navigator.pop statement(true), back allowed, but null returned
          //remove return (false), back allowed, but null returned
          //remove return (true), back allowed, product deleted.
        },
        child: Scaffold(
          //drawer: drawer(),
          appBar: AppBar(
            title: Text('news page'),
          ),
          body: ScopedModelDescendant<MainModel>(
              builder: (BuildContext context, Widget child, MainModel model) {
            return model.isLoading ? Center(child: ColorLoader2()) : ListView.builder(
              itemBuilder: (BuildContext context, int index) {
                //return NewsCard(news[index]);
                return index == 0 ? _searchbar() : _listItem(index - 1);
              },
              itemCount: displayed_news.length + 1,
            );
          }),
        ));
  }
}
