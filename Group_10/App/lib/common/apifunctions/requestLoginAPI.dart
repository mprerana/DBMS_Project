import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:splash_tokenauth/common/apifunctions/requestData.dart';
import 'package:splash_tokenauth/model/json/loginModel.dart';

Future<LoginModel> requestLoginAPI(BuildContext context, String username, String password) async {
  final url = "http://10.0.36.104:8000/api/auth/login";

  Map<String, String> body = {
    'email': username,
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

