import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:splash_tokenauth/common/apifunctions/requestData.dart';
import 'package:splash_tokenauth/model/json/loginModel.dart';

Future<LoginModel> requestSignupAPI(BuildContext context, String username, String name, String email, String age, bool isTeacher, String password) async {
  final url = "http://10.0.36.104:8000/api/auth/register";

  Map<String, String> body = {
    'username': username,
    'name': name,
    'email': email,
    'age': age,
    'isTeacher': isTeacher.toString(),
    'password': password,
  };
  final response = await http.post(url, body: body,);
  
  if (response.statusCode == 200) {
    var responseJson = json.decode(response.body);
    var token = (responseJson != null && !responseJson.isEmpty) ? LoginModel.fromJson(responseJson).token : "";

    getJsonData(token, context);
    
    return LoginModel.fromJson(responseJson);
  }else{
    final responseJson = json.decode(response.body);
    getJsonData(responseJson, context);
    
    return null;
  }
}

