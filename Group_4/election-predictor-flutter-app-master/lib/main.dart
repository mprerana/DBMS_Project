import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:flutter_webview_plugin/flutter_webview_plugin.dart';
import 'package:location/location.dart';
import 'package:flutter/services.dart';
import 'dart:async';




import './pages/auth.dart';
import './pages/eventlist.dart';

import './pages/home.dart';
import './pages/news.dart';
import './pages/analysis.dart';

import './scoped_models/main.dart';
import './widgets/newsdetail.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _MyAppState();
  }
}

class _MyAppState extends State<MyApp> {
  final MainModel _model = MainModel();
  bool _isAuthenticated = false;
  Map<String, double> currentLocation = Map();
  StreamSubscription<Map<String, double>> locationSubscription;
  Location location = Location();
  String error;

  @override
  initState() {
    super.initState();
    _model.autoAuthenticate();
    _model.userSubject.listen((bool isAuthenticated) {
      setState(() {
        _isAuthenticated = isAuthenticated;
      });
    });

    currentLocation['latitude'] = 0.0;
    currentLocation['longitude'] = 0.0;

    void initPlatformState() async {
      Future<Map<String, double>> my_location;
      try {
        var my_loc = await location.getLocation;
        error = "";
        print(my_location.runtimeType);
      } on PlatformException catch (e) {
        if (e.code == 'PERMISSION_DENIED')
          error = 'permission denied';
        else if (e.code == 'PERMISSION_DENIED_NEVER_ASK')
          error = 'permission denied - please ask the blah';
        my_location = null;
        print('this is location${my_location}');
      }
    }

    initPlatformState();
    locationSubscription =
        location.onLocationChanged().listen((Map<String, double> result) {
          currentLocation = result;
          _model.setLocation(currentLocation['latitude'], currentLocation['longitude']);

        });


  }

  @override
  Widget build(BuildContext context) {
    print('build');
    print(_isAuthenticated);

    return ScopedModel<MainModel>(
      model: _model,
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        theme: ThemeData(
          primarySwatch: Colors.lightBlue,
          accentColor: Colors.black,
        ),
        home: !_isAuthenticated ? AuthPage() : HomePage(_model),
        routes: {
          '/analysis': (BuildContext context) => AnalysisPage(_model),
          '/signup-through-website': (_) => WebviewScaffold(
                resizeToAvoidBottomInset: true,
                url: 'http://127.0.0.1:8000/auth/register_user/',
                appBar: new AppBar(
                  title: const Text('Widget Webview'),
                ),
                withZoom: false,
                withLocalStorage: true,
              ),
          '/news': (BuildContext context) =>
              !_isAuthenticated ? AuthPage() : NewsPage(_model),
          '/events': (BuildContext context) =>
          !_isAuthenticated ? AuthPage() : EventsPage(_model),
          "/webview": (_) => WebviewScaffold(
                resizeToAvoidBottomInset: true,
                url: _model.selectedUrl,
                appBar: new AppBar(
                  title: const Text('Widget Webview'),
                ),
                withZoom: false,
                withLocalStorage: true,
              ),
        },
        onGenerateRoute: (RouteSettings settings) {
          final List<String> pathElements = settings.name.split('/');
          if (pathElements[0] != '') {
            return null;
          }
          if (pathElements[1] == 'news_detail') {
            final String newsid = pathElements[2];
            _model.selectNews(newsid);
            return MaterialPageRoute(
                builder: (BuildContext context) =>
                    !_isAuthenticated ? AuthPage() : NewsDetailPage(_model));
          }
          return null;
        },
        onUnknownRoute: (RouteSettings settings) {
          return MaterialPageRoute(
            builder: (BuildContext context) =>
                !_isAuthenticated ? AuthPage() : HomePage(_model),
          );
        },
      ),
    );
  }
}
