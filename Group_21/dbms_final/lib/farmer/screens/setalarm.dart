

import 'package:flutter/material.dart';
import 'dart:async';
import 'package:intl/intl.dart';
import 'package:dbms_final/farmer/models/clock.dart';
import 'package:dbms_final/utils/dbhelper.dart';

import 'package:dbms_final/servies/authentication.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'package:dbms_final/utils/datbasefiles/clockcrud.dart';
import 'dart:ui';
import 'package:flutter/cupertino.dart';

GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();
class MyApp1 extends StatefulWidget {
  final String appbartitle;
  final Clockset clockset;
  MyApp1(this.clockset,this.appbartitle);
  @override
  State<StatefulWidget> createState(){
    return  _State(this.clockset,this.appbartitle);
  } 
   }

class _State extends State<MyApp1> {
  DatabaseHelper helper=DatabaseHelper();
  String appbartitle;
  Clockset clockset;

  DateTime _date = new DateTime.now();
  TimeOfDay _time = new TimeOfDay.now();
  TextEditingController reasonController = TextEditingController();
_State(this.clockset,this.appbartitle);
  

  Future<Null> _selectDate(BuildContext context) async {
    final DateTime picked = await showDatePicker(
        context: context,
        initialDate: _date,
        firstDate: DateTime.now().subtract(Duration(days: 1)),
        lastDate: new DateTime(2050)
    );
    if(picked != null && picked != _date) {
      print('Date selected: ${_date.toString()}');
      setState((){
        _date = picked;
        
      
        clockset.date=_date.toString();
      });
    }
  }

  Future<Null> _selectTime(BuildContext context) async {
     TimeOfDay picked ;
     var now = new DateTime.now();
     var formatter = new DateFormat('yyyy-MM-dd');
     String presentdate = formatter.format(now);
     String _pickeddate = formatter.format(_date);
     if(_pickeddate==presentdate){
     picked= await showTimePicker(
        context: context,
        initialTime: TimeOfDay.now(),  
    );
    }
    else{
      picked= await showTimePicker(
        context: context,
        initialTime:_time,
    );
    }
    
    if(picked != null && picked != _time) {
        if (_pickeddate==presentdate)
        {
            if((((DateTime.now()).hour)>picked.hour)||((DateTime.now().minute>picked.minute)&&((DateTime.now()).hour)==picked.hour))
            {
      
                _scaffoldKey.currentState.showSnackBar(
        
                SnackBar(
          
                content: new Text('choose correct time'),
                duration: new Duration(seconds:5),
                backgroundColor: Colors.red,
                
               )
              );
            new RaisedButton(
                        child: new Text('Selectcorrect time'),
                        onPressed: (){_selectTime(context);}
                      );

              }
  
        } 
      print('time selected: ${_time.toString()}');
      setState((){
        _time = picked;
        
        String timeformettohoursandminutes='${_time.hour}'+':'+'${_time.minute}';
        print(timeformettohoursandminutes);
        clockset.time=timeformettohoursandminutes;
       
      });
     print('Time selected:');
     print(_time);
    } 
  } 
  
   @override
  Widget build(BuildContext context) {
    TextStyle textStyle = Theme.of(context).textTheme.title;
    reasonController.text=clockset.reason;
    return WillPopScope(
      onWillPop: (){
        movetolastscreen();
      },
      child:Scaffold(
      key: _scaffoldKey ,
      
      appBar: new AppBar(title: new Text("set alarm"),
       backgroundColor: Color.fromRGBO(40, 80, 40, 0.8),
        leading: IconButton(icon: Icon(
				    Icons.arrow_back),
				    onPressed: () {
		    	    
		    	    movetolastscreen();
				    }
		    ),
        ),
      body: new Container(
       padding: new EdgeInsets.all(32.0),
        child: ListView(
            children: <Widget>[
              new Text('Date selected: ${clockset.date}'),
              new RaisedButton(
                child: new Text('Select Date'),
                onPressed: (){_selectDate(context);},
                color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
                  shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
              ),
              new Text('Time selected: ${clockset.time}'),
               new RaisedButton(
                child: new Text('Select time'),
                onPressed: (){_selectTime(context);},
                color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
                  shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
              ),
              Padding(
					    padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
					    child: TextField(
						    controller: reasonController,
						    style: textStyle,
						    onChanged: (value) {
						    	debugPrint('Something changed in Title Text Field');
						    	updatereason();
						    },
						    decoration: InputDecoration(
							    labelText: 'Title',
							    labelStyle: textStyle,
							    border: OutlineInputBorder(
								    borderRadius: BorderRadius.circular(5.0)
							    )
						    ),
					    ),
				    ),
          
                  Padding(
					    padding: EdgeInsets.only(top: 15.0, bottom: 15.0),
					    child: Row(
						    children: <Widget>[
						    	Expanded(
								    child: RaisedButton(
									    shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
									    color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
									    child: Text(
										    'Save',
										    textScaleFactor: 1.5,
									    ),
									    onPressed: () {

									    	setState(() {
									    	  debugPrint("Save button clicked");
									    	  _save();
									    	});
									    },
								    ),
							    ),

							    Container(width: 5.0,),

							    Expanded(
								    child: RaisedButton(
									    shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
									    color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
									    child: Text(
										    'Delete',
										    textScaleFactor: 1.5,
									    ),
									    onPressed: () {
										    setState(() {
											    debugPrint("Delete button clicked");
											    _delete();
										    });
									    },
								    ),
							    ),

						    ],
					    ),
				    ),
            ],
          
        ),
      ),
    )
    );
  }
  void movetolastscreen() {
		Navigator.pop(context, true);
  }
  void updatereason(){
    clockset.reason=reasonController.text;
  }
 
 void _save() async{
   int result;
   if(clockset.id!=null && clockset.idf!=null){
     print('hdfsghf');
     result=await Clockcrudoperations().updateTime(clockset);
     

   }
   else{

    FirebaseUser user = await BaseAuth().getCurrentUser();
    print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);
     clockset.id = userrecord['id'];
     print('${clockset.id}, ${clockset.idf}');
     result=await Clockcrudoperations().insertTime(clockset);
     print('Inserted alarm to database');
     print(result);
   }
   if(result!=0){
      
     	_showAlertDialog('Status', 'alarm Saved Successfully');
        // Navigator.of(context)
        //         .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
        //       return new MyAppmain();
        //         }
        //         )
        //         );
        // Navigator.popAndPushNamed()
        print('hellloooo');
        //movetolastscreen();
   }
   else{
     	_showAlertDialog('Status', 'Problem Saving alarm');
   }
  print("working");
 }
 void _delete() async {

		movetolastscreen();

		
		if ( clockset.idf==null) {
			_showAlertDialog('Status', 'No alarm was deleted');
			return;
		}

		// Case 2: User is trying to delete the old note that already has a valid ID.
		int result = await Clockcrudoperations().deleteTime(clockset.idf);
		if (result != 0) {
			_showAlertDialog('Status', 'alarm Deleted Successfully');
		} else {
			_showAlertDialog('Status', 'Error Occured while Deleting alarm');
		}
	}
void _showAlertDialog(String title, String message) {

		AlertDialog alertDialog = AlertDialog(
			title: Text(title),
			content: Text(message),
		);
         print("working");
		showDialog(
				context: context,
				builder: (_) => alertDialog
		);
	}
}