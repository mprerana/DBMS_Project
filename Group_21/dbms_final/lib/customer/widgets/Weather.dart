import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:dbms_final/customer/models/WeatherData.dart';

class Weather extends StatelessWidget {
  final WeatherData weather;

  Weather({Key key, @required this.weather}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Text(weather.name, style: new TextStyle(color: Colors.white,fontSize: 30.0)),
        Text(weather.main, style: new TextStyle(color: Colors.white, fontSize: 42.0)),
        Image.network('https://openweathermap.org/img/w/${weather.icon}.png'),
        Text('${weather.temp.toString()}°C',  style: new TextStyle(color: Colors.white, fontSize: 70.0)),
        Text(weather.humd.toString(),  style: new TextStyle(color: Colors.white, fontSize: 50.0)),
        Text(weather.press.toString(),  style: new TextStyle(color: Colors.white, fontSize: 50.0)),
        Text(new DateFormat.yMMMd().format(weather.date), style: new TextStyle(color: Colors.white,fontSize: 20.0)),
        Text(new DateFormat.Hm().format(weather.date), style: new TextStyle(color: Colors.white, fontSize: 20.0)),
      ],
    );
  }
}