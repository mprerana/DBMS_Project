class NewsData {
  final String author;
  final String tittle;
  final String description;
  final String url;
  final String content;
  

  NewsData({this.author, this.tittle, this.description,this.url ,this.content});

  factory NewsData.fromJson(Map<String, dynamic> json) {
    return NewsData(
      author: json['articles'][0]['author'],
      tittle: json['articles'][0]['tittle'],
      description: json['articles'][0]['description'],
      url: json['articles'][0]['url'],
      content: json['articles'][0]['content'],
    );
  }

  Map<String, dynamic> toMap(){
    var map = Map<String, dynamic>();
    map['author'] = author;
    map['tittle'] = tittle;
    map['description'] = description;
    map['url'] = url;
    map['content'] = content;
    return map;
  }
}