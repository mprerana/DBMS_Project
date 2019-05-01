import 'package:scoped_model/scoped_model.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:rxdart/subjects.dart';

import '../models/user.dart';
import '../models/auth.dart';
import '../models/news.dart';
import '../models/events.dart';
import '../models/task.dart';


class ConnectedModel extends Model {
  bool _isloading = false;
  List<News> _news = [];
  User _authenticatedUser;
  String _selectedUrl = null;
  int _index;
  double _latitude = 13.5567943;
  double _longitude = 80.025118;
  String user_location = 'Chennai';
  List<Event> _events;
}

class NewsModel extends ConnectedModel {
  int no_of_news = 0;
  News selectednews;
  String selectedId;

  void selectNews(String id) {
    print('selectNews main');

    selectedId = id;
    print(id);
  }

  void setUrl(String url) {
    _selectedUrl = url;
  }

  String get selectedUrl {
    return _selectedUrl;
  }

  List<News> get allnews {
    return List.from(_news);
  }

  List<News> get displayNews {
    return List.from(_news);
  }

  void selectIndex(int index) {
    _index = index;
  }

  int get selectedIndex {
    return _index;
  }

  Future<Null> fetchNews() async {
    _isloading = true;
    notifyListeners();
    print('fetch ho raha hai');
    String link = 'http://127.0.0.1:8000/api/v1/articles';
    http.Response response;
    response = await http.get(
      link,
      //body: json.encode('Bearer '+ _authenticatedUser.access),
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + _authenticatedUser.access
      },
    );
    print('this is the status ${response.statusCode}');
    print('print/fetch ho gaya!!');
    final List<News> fetchedProductList = [];
    final List productListData = json.decode(response.body);
    print('decode  ${productListData.length}');

    if (productListData == null) {
      print('fnull hai');

      _isloading = false;
      notifyListeners();
      return;
    }
    for (int i = 0; i < productListData.length; i++) {
      String old_desc = productListData[i]['description'];
      List<String> split_desc = old_desc.split('>');
      List<String> desc = split_desc[1].split('<');

      final News news = News(
        title: productListData[i]['title'],
        description: desc[0],
        url: productListData[i]['url'],
      );

      fetchedProductList.add(news);
    }

    _news = fetchedProductList;
    _isloading = false;
    notifyListeners();
  }
}

class UserModel extends ConnectedModel {

  User get authenticatedUser {
    return _authenticatedUser;
  }
  Timer _authtimer;
  PublishSubject<bool> _userSubject = PublishSubject();

  PublishSubject<bool> get userSubject {
    return _userSubject;
  }

  User get user {
    return _authenticatedUser;
  }

  Future<Map<String, dynamic>> authenticate(String email, String password,
      int phone, String username, String number_plate,
      [AuthMode _authmode = AuthMode.login]) async {
    _isloading = true;
    notifyListeners();

    String ip_address = 'http://127.0.0.1:8000/api/token/';
    final Map<String, dynamic> authdata_signup = {
      'email': email,
      'password': password,
      'phone_number': phone,
      'username': username,
      'number_plate': number_plate,
      'returnSecureToken': true,
    };

    final Map<String, dynamic> authdata_login = {
      'username': username,
      'password': password,
    };

    bool haserror = true;
    String message = 'incorrect data entered';
    print(authdata_signup);
    http.Response response;

    if (_authmode == AuthMode.login) {
      String link = ip_address;
      print('ye hai link ${link}');

      response = await http.post(
        link,
        body: json.encode(authdata_login),
        headers: {'Content-Type': 'application/json'},
      );
    }
//    else {
//      String link = ip_address + '/auth/user/create/';
//
//      response = await http.post(
//        link,
//        body: json.encode(authdata_signup),
//        headers: {'Content-Type': 'application/json'},
//      );
//
//      if (response.statusCode != 400 || response.statusCode != 401) {
//        String link = ip_address + '/auth/token/obtain/';
//        response = await http.post(
//          link,
//          body: json.encode(authdata_login),
//          headers: {'Content-Type': 'application/json'},
//        );
//      }
//    }
    print('ye hai response ${json.decode(response.body)}');
    final Map<String, dynamic> responsedata = json.decode(response.body);
    print('ye hai status code ${response.statusCode}');

    if (response.statusCode != 400 && response.statusCode != 401) {
      haserror = false;
      _authenticatedUser = User(
        refresh: responsedata['refresh'],
        access: responsedata['access'],
        username: username,
      );

      setAuthTimeout(1 * 3600 * 24); //1day timeout in seconds
      final DateTime now = DateTime.now();
      final DateTime expiryTime =
          now.add(Duration(seconds: 1 * 3600 * 24)); //1 day in seconds

      final SharedPreferences prefs = await SharedPreferences.getInstance();
      prefs.setString('refresh', responsedata['refresh']);
      prefs.setString('username', username);
      prefs.setString('access', responsedata['access']);
      prefs.setString('expiryTime', expiryTime.toIso8601String());
      _userSubject.add(true);
    }

    _isloading = false;
    notifyListeners();
    return {'success': !haserror, 'message': message};
  }

  void autoAuthenticate() async {
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    final String access = prefs.getString('access');
    _userSubject.add(false);
    if (access != null) {
      //logged in
      final String expiryTime = prefs.getString('expiryTime');
      print('autoAuthenticate');
      final DateTime now = DateTime.now();
      final parsedExpiryTime = DateTime.parse(expiryTime);
      if (parsedExpiryTime.isBefore(now)) {
        _authenticatedUser = null;
        notifyListeners();
        return;
      }

      _authenticatedUser = User(
        access: prefs.getString('access'),
        refresh: prefs.getString('refresh'),
        username: prefs.getString('username'),
      );
      final int tokenlifespan = parsedExpiryTime.difference(now).inSeconds;
      setAuthTimeout(tokenlifespan);
      _userSubject.add(true);
      notifyListeners();
    }
    //logged out hai
  }

  void logout() async {
    print('logout ho raha hai');
    _authtimer.cancel();
    final SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.remove('access');
    prefs.remove('refresh');
    prefs.remove('username');
    _authenticatedUser = null;
    _userSubject.add(false);
    print('logout ho gaya');
  }

  void setAuthTimeout(int time) {
    _authtimer = Timer(Duration(seconds: time), () {
      logout();
      print('logout, automatic');
    });
  }
}

class Utilitymodel extends ConnectedModel {
  bool get isLoading {
    return _isloading;
  }
}

class Locationmodel extends ConnectedModel {
  void getAddress() async {
    String url =
        'https://maps.googleapis.com/maps/api/geocode/json?latlng=${_latitude},${_longitude}&key=AIzaSyAIJtykBRaxn1aNhQ5SR-k1aglZ65ghY6U';
    http.Response response = await http.get(url);

    Map<String, dynamic> decoded = json.decode(response.body);
    if (decoded['error_message'] != null) {
      print(response.body);
      print(
          'cant fetch your location, api key problem, expired');
      user_location = 'Chennai';
    } else {
      user_location =
          decoded['results'][0]['address_components'][3]['long_name'];
    }
  }

  void setLocation(double latitude, double longitude) {
    //print('setloc function called');
    if (latitude != null && longitude != null) {
      _latitude = latitude;
      _longitude = longitude;
    }
  }
}

class Eventmodel extends ConnectedModel {
  List<Event> get displayEvents {
    return _events;
  }

//  void fetchEvents() async {
//    //get request
////    _events = [];
////    List<Map<String, dynamic>> temp = [
////      {'title': 'event 1', 'party': 'party 1', 'members': 13},
////      {'title': 'event 2', 'party': 'party 2', 'members': 31},
////      {'title': 'event 3', 'party': 'party 3', 'members': 131}
////    ];
//
//    http.Response response = http.get(url)
//    for (int i = 0; i < temp.length; i++) {
//      final Event e = Event(
//        title: temp[i]['title'],
//        party: temp[i]['party'],
//        members: temp[i]['members'],
//      );
//      _events.add(e);
//    }
//  }

  Future<Null> fetchEvents() async {
    _isloading = true;
    notifyListeners();
    String link = 'http://127.0.0.1:8000/api/v1/events';
    http.Response response;
    response = await http.get(
      link,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + _authenticatedUser.access
      },
    );
    print('this is the status ${response.statusCode}\n${response.body}');
    print('print/fetch ho gaya!!');
    final List<Event> fetchedEventsList = [];
    final List eventsListData = json.decode(response.body);
    print('decode  ${eventsListData.length}');

    if (eventsListData == null) {
      print('fnull hai');

      _isloading = false;
      notifyListeners();
      return;
    }
    for (int i = 0; i < eventsListData.length; i++) {

      final Event event = Event(
        title: eventsListData[i]['name'],
        group: eventsListData[i]['group_id']['name'],
        party: eventsListData[i]['group_id']['admin_id']['name'],

      );

      fetchedEventsList.add(event);
    }

    _events = fetchedEventsList;
    _isloading = false;
    notifyListeners();
  }
}

class Analysismodel extends ConnectedModel {
  int _pro_bjp = 5610;
  int _pro_cong = 4765;
  int _anti_bjp = 945;
  int _anti_Cong = 174;


  int get pro_bjp  {
    return _pro_bjp;
  }

  int get pro_cong  {
    return _pro_cong;
  }

  int get anti_cong  {
    return _anti_Cong;
  }
  int get anti_bjp  {
    return _anti_bjp;
  }


}
