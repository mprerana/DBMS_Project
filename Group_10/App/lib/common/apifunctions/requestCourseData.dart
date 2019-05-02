import 'package:http/http.dart' as http;
import 'package:splash_tokenauth/ui/courseScreen.dart';
import 'dart:async';

List data;

Future<String> getCourseJsonData(token, context, cid) async{

String url = "http://10.0.36.104:8000/quiz/listquizzes/"+cid.toString();
var response = await http.get(Uri.encodeFull(url), headers: {"Accept": "application/json", "x-access-token": token});

if (response.statusCode == 200) {
  courseInitializer(token, response.body, context);
  }

  return "Success";
}
