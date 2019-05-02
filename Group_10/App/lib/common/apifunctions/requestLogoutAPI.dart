import 'dart:async';
import 'package:flutter/material.dart';

Future<void> requestLogout(BuildContext context){
  Navigator.of(context).pushReplacementNamed('/LoginScreen');
  return null;
}