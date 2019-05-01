import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'package:scoped_model/scoped_model.dart';
import 'package:charts_flutter/flutter.dart' as charts;

import '../scoped_models/main.dart';

import '../models/task.dart';



class AnalysisPage extends StatefulWidget {
  final MainModel model;

  AnalysisPage(this.model);

  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _AnalysisPageState();
  }
}

class _AnalysisPageState extends State<AnalysisPage> {

  List<charts.Series<Task, String>> _seriesPieData;
  List<charts.Series<Task, String>> _seriesPieData2;


  List<Task> _generatePieData(){
    return [
      Task('support BJP', widget.model.pro_bjp, Colors.orange),
      Task('support Congress', widget.model.pro_cong, Colors.redAccent),
    ];
  }

  List<Task> _generatePieData2(){
    return [
      Task('Anti BJP', widget.model.anti_bjp, Colors.orange),
      Task('Anti Congress', widget.model.anti_cong, Colors.redAccent),
    ];
  }

  _generateData() {
    _seriesPieData.add(
      charts.Series(
        data: _generatePieData(),
        domainFn: (Task task, _) => task.task,
        measureFn: (Task task, _) => task.taskvalue,
        colorFn: (Task task, _) => charts.ColorUtil.fromDartColor(task.color),
        id: 'Pro Comments',
        labelAccessorFn: (Task row, _) => '${row.taskvalue}',
      ),
    );
  }

  _generateData2() {
    _seriesPieData2.add(
      charts.Series(
        data: _generatePieData2(),
        domainFn: (Task task, _) => task.task,
        measureFn: (Task task, _) => task.taskvalue,
        colorFn: (Task task, _) => charts.ColorUtil.fromDartColor(task.color),
        id: 'Anti Comments',
        labelAccessorFn: (Task row, _) => '${row.taskvalue}',
      ),
    );
  }

  void initState() {
    super.initState();
    _seriesPieData2 = List<charts.Series<Task, String>>();
    _seriesPieData = List<charts.Series<Task, String>>();

    //fetch the data
    _generateData();
    _generateData2();


  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: Text(
            'Analysis',
            style: TextStyle(
              color: Colors.white,
            ),
          ),
          bottom: TabBar(
            tabs: <Widget>[
              Tab(
                icon: Icon(Icons.pie_chart),
              ),
              Tab(
                icon: Icon(Icons.insert_chart),
              ),
            ],
          ),
        ),
        body: TabBarView(
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(8.0),
              child: Center(
                child: Column(
                  children: <Widget>[
                    Text(
                      'Party Supports',
                      style: TextStyle(
                          fontSize: 24.0, fontWeight: FontWeight.bold),
                    ),
                    Expanded(
                      child: charts.PieChart(
                        _seriesPieData,
                        animate: true,
                        animationDuration: Duration(seconds: 2),
                        behaviors: [
                          charts.DatumLegend(
                            outsideJustification:
                            charts.OutsideJustification.endDrawArea,
                            horizontalFirst: false,
                            desiredMaxRows: 4,
                            cellPadding:
                            EdgeInsets.only(right: 4.0, bottom: 4.0),
                            entryTextStyle: charts.TextStyleSpec(
                              color: charts.MaterialPalette.purple.shadeDefault,
                              fontSize: 11,
                            ),
                          ),
                        ],
                        defaultRenderer: charts.ArcRendererConfig(
                            arcWidth: 100,
                            arcRendererDecorators: [
                              charts.ArcLabelDecorator(
                                labelPosition: charts.ArcLabelPosition.inside,
                              )
                            ]),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.all(8.0),
              child: Center(
                child: Column(
                  children: <Widget>[
                    Text(
                      'Anti Party',
                      style: TextStyle(
                          fontSize: 24.0, fontWeight: FontWeight.bold),
                    ),
                    Expanded(
                      child: charts.BarChart(
                        _seriesPieData2,
                        animate: true,
                        animationDuration: Duration(seconds: 2),
                        behaviors: [
                          charts.DatumLegend(
                            outsideJustification:
                            charts.OutsideJustification.endDrawArea,
                            horizontalFirst: false,
                            desiredMaxRows: 4,
                            cellPadding:
                            EdgeInsets.only(right: 4.0, bottom: 4.0),
                            entryTextStyle: charts.TextStyleSpec(
                              color: charts.MaterialPalette.purple.shadeDefault,
                              fontSize: 11,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}


