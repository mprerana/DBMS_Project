import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';

import '../scoped_models/main.dart';
import '../models/events.dart';

class EventCard extends StatelessWidget {
  final Event single_event;
  final int index;

  EventCard(this.single_event, this.index);

  showlink(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('a different page'),
          content: Text('a webpage'),
          actions: <Widget>[
            FlatButton(
              child: Text('discard'),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
            FlatButton(
              child: Text('delete'),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
          ],
        );
      },
    );
  }


  @override
  Widget build(BuildContext context) {
    return Container(

      child: Card(
        margin: EdgeInsets.all(15.0),
        child: Column(
          children: <Widget>[
            Container(
                decoration: BoxDecoration(

                  boxShadow: [
                    new BoxShadow(
                      color: Colors.black26,
                      blurRadius: 0.0,
                    ),
                  ],
                  // Box decoration takes a gradient
                  gradient: LinearGradient(
                    // Where the linear gradient begins and ends
                    begin: Alignment.topRight,
                    end: Alignment.bottomLeft,
                    // Add one stop for each color. Stops should increase from 0 to 1
                    stops: [0.1, 0.5, 0.7, 0.9],
                    colors: [
                      // Colors are easy thanks to Flutter's Colors class.
                      Colors.indigo[800],
                      Colors.indigo[700],
                      Colors.indigo[600],
                      Colors.indigo[400],
                    ],
                  ),
                ),
                padding: EdgeInsets.all(20.0),
                child: Column(
                  textDirection: TextDirection.ltr,
                  children: <Widget>[
                    Row(
                      children: <Widget>[
                        Expanded(
                          child: Text(
                            'Title : ',
                            style: TextStyle(
                              fontSize: 25.0,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Oswald',
                            ),
                          ),
                        ),
                        Expanded(
                          child: Text(
                            single_event.title,
                            style: TextStyle(
                              fontSize: 25.0,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Oswald',
                            ),
                          ),
                        ),
                      ],
                    ),
                    SizedBox(
                      height: 10.0,
                    ),
                    Row(
                      children: <Widget>[
                        Expanded(
                          child: Text(
                            'Group : ',
                            style: TextStyle(
                              fontSize: 25.0,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Oswald',
                            ),
                          ),
                        ),
                        Expanded(
                          child: Text(
                            single_event.group,
                            style: TextStyle(
                              fontSize: 25.0,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Oswald',
                            ),
                          ),
                        ),
                      ],
                    ),
                    SizedBox(
                      height: 10.0,
                    ),
                    Row(
                      children: <Widget>[
                        Expanded(
                          child: Text(
                            'Party : ',
                            style: TextStyle(
                              fontSize: 25.0,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Oswald',
                            ),
                          ),
                        ),
                        Expanded(
                          child: Text(
                            single_event.party,
                            style: TextStyle(
                              fontSize: 25.0,
                              fontWeight: FontWeight.bold,
                              fontFamily: 'Oswald',
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                )),
          ],
        ),
      ),
    );
  }
}
