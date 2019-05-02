import 'dart:async';
import 'package:http/http.dart' as http;
import 'package:splash_tokenauth/common/apifunctions/requestData.dart';

Future<String> createCourse(context, token, courseName)async{
  final url = "http://10.0.36.104:8000/course/createcourse";

  Map<String, String> body = {
    'cname': courseName,
  };

  final response = await http.post(url, body: body, headers: {"Accept": "application/json", "x-access-token": token});
  print(response);

  getJsonData(token, context);

  return "Success";
}