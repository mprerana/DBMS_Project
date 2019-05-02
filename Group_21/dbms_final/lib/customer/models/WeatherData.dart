class WeatherData {
  final DateTime date;
  final String name;
  final double temp;
  final double humd;
  final double press;
  final String main;
  final String icon;

  WeatherData({this.date, this.name, this.temp,this.humd ,this.press, this.main, this.icon});

  factory WeatherData.fromJson(Map<String, dynamic> json) {
    return WeatherData(
      date: new DateTime.fromMillisecondsSinceEpoch(json['dt'] * 1000, isUtc: false),
      name: json['name'],
      temp: json['main']['temp'].toDouble(),
      humd: json['main']['humidity'].toDouble(),
      press: json['main']['pressure'].toDouble(),
      main: json['weather'][0]['main'],
      icon: json['weather'][0]['icon'],
    );
  }

  Map<String, dynamic> toMap(){
    var map = Map<String, dynamic>();
    map['date'] = date;
    map['name'] = name;
    map['temp'] = temp;
    map['humd'] = humd;
    map['press'] = press;
    map['main'] = main;
    map['icon'] = icon;
    return map;
  }
}