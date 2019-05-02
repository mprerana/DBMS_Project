import 'package:http/http.dart' as http;
import 'package:splash_tokenauth/ui/quizScreen.dart';
import 'dart:async';

List data;

Future<String> getQuizJsonData(token, context, quizid) async{
  String url = "http://10.0.36.104:8000/quiz/quizresults/"+quizid.toString();
  var response = await http.get(Uri.encodeFull(url), headers: {"Accept": "application/json", "x-access-token": token});
  
  if (response.statusCode == 200) {
  quizInitializer(token, response.body, context);
  }
  
  return "Success";
}

