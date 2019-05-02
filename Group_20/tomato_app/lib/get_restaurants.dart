import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'package:tomato_app/homePage.dart';

List data;

Future<String> getJsonData(token, context) async {
  final String url = "http://10.0.34.149:3000/user/landing";

  var response = await http.get(Uri.encodeFull(url),
      headers: {"Accept": "application/json", "Authorization": token});
  if (response.statusCode == 200) {
    final inJson = json.decode(response.body);
    initializer(inJson, context, token);
  } else {
    final inJson = json.decode(response.body);
    print(inJson);
  }
  return "Success";
}
