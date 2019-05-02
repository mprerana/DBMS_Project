import 'package:dbms_final/customer/models/newsdata.dart';
import 'package:dbms_final/customer/widgets/news.dart';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:location/location.dart';
import 'package:flutter/services.dart';



class News extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return new MyAppState();
  }
}

class MyAppState extends State<News> {
  bool isLoading = false;
  NewsData newdata;
  String error;

  @override
  void initState() {
    super.initState();
    print("uu");
    loadWeather();
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Weather',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: Scaffold(
        backgroundColor: Colors.white,
       appBar:new AppBar(title:new Directionality(
          textDirection: TextDirection.ltr,
          child: new Text('news')
          ),
          backgroundColor:Color.fromRGBO(40, 80, 40, 0.8)
    ),
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: newdata != null ? Newsview(news:newdata) : Container(),
                    ),
                  ],
                ),
              ),
            ]
          )
        )
      ),
    );
  }

  loadWeather() async {
    setState(() {
      isLoading = true;
    });  
      final newsfeed = await http.get(
          'https://newsapi.org/v2/top-headlines?q=farmer&from=2019-04-30&sortBy=popularity&apiKey=feeace90995941649c3334f74367cfd4');
      print("oi");
      print(newsfeed.body);
        print("hii");
        return setState(() {
          newdata =
          new NewsData.fromJson(jsonDecode(newsfeed.body));
          isLoading = false;
        });
  }
  
}