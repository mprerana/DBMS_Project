import 'package:flutter/material.dart';
import 'package:scoped_model/scoped_model.dart';

import '../scoped_models/main.dart';
import '../models/events.dart';


import '../widgets/eventscard.dart';
import '../widgets/loaders/loader_1.dart';

class EventsPage extends StatefulWidget {
  final MainModel model;

  EventsPage(this.model);

  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _EventsPageState();
  }
}

class _EventsPageState extends State<EventsPage> {



  Widget _buildNewsList(List<Event> events) {
    if (events.length > 0) {
      return ListView.builder(
        itemBuilder: (BuildContext context, int index) =>
            EventCard(events[index], index),
        itemCount: events.length,
      );
    } else {
      return Container(
        child: Center(
          child: Text('no events found'),
        ),
      );
    }
  }

  Widget _events() {
    return ScopedModelDescendant<MainModel>(
      builder: (BuildContext context, Widget child, MainModel model) {
        return model.isLoading
            ? Center(child: ColorLoader2())
            : _buildNewsList(model.displayEvents);
      },
    );
  }

  @override
  void initState() {
    widget.model.fetchEvents();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return WillPopScope(
        onWillPop: () {
          print('back button presses');
          Navigator.pop(context, false);
          return Future.value(false);
          //true, true closes the app
          //true, false goes back but deletes the product.
          //false, true closes the app
          //false, false goes back, product saved.
          //remove navigator.pop statement(false), no back allowed
          //remove navigator.pop statement(true), back allowed, but null returned
          //remove return (false), back allowed, but null returned
          //remove return (true), back allowed, product deleted.
        },
        child: Scaffold(
          appBar: AppBar(
            title: Text('Events page'),
          ),
          body: _events(),
        ));
  }
}
