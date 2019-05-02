import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:splash_tokenauth/ui/homeScreen.dart';
import 'dart:async';

final String url = "http://10.0.36.104:8000/course/listgroups";
List data;

Future<String> getJsonData(token, context) async{

  var response = await http.get(Uri.encodeFull(url), headers: {"Accept": "application/json", "x-access-token": token});
  
  if (response.statusCode == 200) {
    final inJson = json.decode(response.body);

  initializer(token, inJson, context);
  }
  
  return "Success";
}
