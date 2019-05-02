import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;


Future<String> getData(String username, String password) async {
  print("/*-/*-/*-/*-/*-/*-/*-/*-/*-/*-");
  http.Response response = await http.post(
      Uri.encodeFull("http://10.0.34.149:3000/api/signin"),headers: {"accept" : "application/json"},
      body: {"username": username , "password" : password});
  print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq");
  print(response.body);
  var responseJson = json.decode(response.body);
  print("sssssssssssssssssssssssssssss");
  print(response);
  print(responseJson["token"]);
  print(response.statusCode);
    if(response.statusCode == 200){
    return (responseJson["token"]);
  }
  else{
    return (responseJson);
  }
}