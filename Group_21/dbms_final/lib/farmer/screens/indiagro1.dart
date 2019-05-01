
import 'package:dbms_final/servies/authentication.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'package:dbms_final/login/models/interaction.dart';
import 'package:dbms_final/utils/datbasefiles/farmeragrointeractioncrud.dart';
class Individualexpert extends StatefulWidget {

  final Map<String,dynamic> cityagro;
  
  Individualexpert({this.cityagro});
  @override
  
  State<StatefulWidget> createState() {
    debugPrint("werty");
    debugPrint(cityagro.toString());
    return _Individualexpertstate(this.cityagro);
  }
}

class _Individualexpertstate extends State<Individualexpert> {
  Map<String,dynamic> cityagro;
   _Individualexpertstate(this.cityagro);
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(
          title: new Directionality(
              textDirection: TextDirection.ltr,
              child: new Text('agricultureexpert')),
          backgroundColor: Color.fromRGBO(40, 80, 40, 0.8)),
      body: new Column(
        children: <Widget>[
          new Row(
            children: <Widget>[
              new Text('FirstName : '),
              new Text(cityagro['Firstname'])
            ],
          ),
          new Row(
            children: <Widget>[
              new Text('LastName : '),
              new Text(cityagro['lastname'])
            ],
          ),
          new Row(
            children: <Widget>[new Text('City : '), new Text(cityagro['City'])],
          ),
          new Row(
            children: <Widget>[
              new Text(' MOBILENUMBER: '),
              new Text(cityagro['mobileno'])
            ],
          ),
          new Row(
            children: <Widget>[new Text(' mailid: '), new Text(cityagro['email'])],
          ),
          new RaisedButton(
            child: new Text('request'),
           onPressed: () {

									    	setState(() {
									    	  debugPrint("Save button clicked");
									    	  agrostatusupdate(cityagro['id']);
									    	});
									    },
          )
        ],
      ),
    );
  }

  void agrostatusupdate(int aid) async{
    int result;
     String status="pending";
    //print(user.email);
    FirebaseUser user = await BaseAuth().getCurrentUser();
    //print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);

    Interaction interaction=Interaction(userrecord['id'],aid,status);
    print(userrecord['id']);
    print(aid);
    print(interaction.status);
    result=await Farmeragrointeraction().insertinteraction(interaction);
    if(result!=0){
      
     	_showAlertDialog('Status', 'requested Successfully');
        
        // Navigator.popAndPushNamed()
        print('hellloooo');
        Navigator.pop(context, true);
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
