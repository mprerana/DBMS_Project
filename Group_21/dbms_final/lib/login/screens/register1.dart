import 'styles.dart';
import 'package:flutter/material.dart';

import 'package:dbms_final/utils/dbhelper.dart';

import  'package:dbms_final/login/models/farmer.dart';
import 'package:dbms_final/login/screens/login.dart';

import 'package:dbms_final/utils/datbasefiles/farmercrud.dart';
import 'package:dbms_final/utils/datbasefiles/userscrud.dart';
import 'package:dbms_final/utils/datbasefiles/cropfarmercrud.dart';
import 'package:dbms_final/farmer/models/cropfarmer.dart';

class RegisterPage1 extends StatefulWidget {
  
  @override
  State<StatefulWidget> createState() {
    return _RegisterPageState1();
  }
}  

class _RegisterPageState1 extends State<RegisterPage1> {
  DatabaseHelper databaseHelper = DatabaseHelper();
  final GlobalKey<FormState> formkey =GlobalKey<FormState>();
   String _longitude0;
   String  _latitude0;
   String _longitude1;
   String  _latitude1;
   String _longitude2;
   String  _latitude2;
   String _longitude3;
   String  _latitude3;
  String _crop;
  String _price;

   @override
  Widget build(BuildContext context) {
return Scaffold(
      // resizeToAvoidBottomPadding: false,

     appBar: AppBar(
           backgroundColor: Color.fromRGBO(40,80, 40, 0.8),
        title: Text('Land Details'),
      ),
          body: new Container(
              decoration: new BoxDecoration(
                image: backgroundImage,
                
              ),
              
              child: new Container(
                padding: EdgeInsets.all(20.0),
                  decoration: new BoxDecoration(
                      gradient: new LinearGradient(
                    colors: <Color>[
                      const Color.fromRGBO(255,250, 250, 0.8),
                      const Color.fromRGBO(0, 0, 0, 0.9),
                    ],
                    stops: [0.2, 1.0],
                    begin: const FractionalOffset(0.0, 0.0),
                    end: const FractionalOffset(0.0, 1.0),
                  )),
                  child: new ListView(
                    padding: const EdgeInsets.all(0.0),
                    
                    children: <Widget>[
                      new Stack(
                        
                        alignment: AlignmentDirectional.bottomCenter,
                        children: <Widget>[
                          new Form(
                            key:formkey,
                            child:
                            new Column(
                            children: <Widget>[
         new Container(
              width:100,
 
              child:TextFormField(

                 decoration: InputDecoration(labelText: 'longitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            )),
                validator: (value) => value.isEmpty ? 'fields can\'t be empty' : null,
                onSaved: (value) {
                  _longitude0 = value ;
                  
                },
              )),
              new Container(
              width:100,

            child:TextFormField(
                decoration: InputDecoration(labelText: 'latitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
                validator: (value) => value.isEmpty ? 'fields can\'t be empty ' : null,
                onSaved: (value) {
                  _latitude0= value ;
                  
                },
              )),
            
              new Container(
              width:100,
 
              child:TextFormField(

                 decoration: InputDecoration(labelText: 'longitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            )),
                validator: (value) => value.isEmpty ? 'fields can\'t be empty' : null,
                onSaved: (value) {
                  _longitude1 = value ;
                  
                },
              )),
              new Container(
              width:100,

            child:TextFormField(
                decoration: InputDecoration(labelText: 'latitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
                validator: (value) => value.isEmpty ? 'fields can\'t be empty ' : null,
                onSaved: (value) {
                  _latitude1= value ;
                  
                },
              )),
            new Container(
              width:100,
 
              child:TextFormField(

                 decoration: InputDecoration(labelText: 'longitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            )),
                validator: (value) => value.isEmpty ? 'fields can\'t be empty' : null,
                onSaved: (value) {
                  _longitude2 = value ;
                  
                },
              )),
              new Container(
              width:100,

            child:TextFormField(
                decoration: InputDecoration(labelText: 'latitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
                validator: (value) => value.isEmpty ? 'fields can\'t be empty ' : null,
                onSaved: (value) {
                  _latitude2= value ;
                  
                },
              )),
            new Container(
              width:100,
 
              child:TextFormField(

                 decoration: InputDecoration(labelText: 'longitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            )),
                validator: (value) => value.isEmpty ? 'fields can\'t be empty' : null,
                onSaved: (value) {
                  _longitude3 = value ;
                  
                },
              )),
              new Container(
              width:100,

            child:TextFormField(
                decoration: InputDecoration(labelText: 'latitude', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
                validator: (value) => value.isEmpty ? 'fields can\'t be empty ' : null,
                onSaved: (value) {
                  _latitude3= value ;
                  
                },
              )
              ),
               new Container(
              width:100,

            child:TextFormField(
                decoration: InputDecoration(labelText: 'crop', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
            
                onSaved: (value) {
                  _crop= value ;
                  
                },
              )),
              new Container(
              width:100,

            child:TextFormField(
                decoration: InputDecoration(labelText: 'price', icon: new Icon(
              Icons.gps_fixed,
              color: Colors.grey,
            ),),
              
                
                onSaved: (value) {
                 _price= value ;
                  
                },
              )),
            
              new SizedBox(
           width:250,
               child:
            RaisedButton(
                child: Text('Create farmer account'),
                shape: new RoundedRectangleBorder(borderRadius: new BorderRadius.circular(30.0)),
                onPressed:(){
            validateAndSubmit();
                   Navigator.of(context).push(MaterialPageRoute<Null>(builder: (BuildContext context) {
              return new LoginPage();
            
                }
                )
                );
                } ,
               color: Color.fromRGBO(40,80,40,0.8),
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
                  ))
             ],
                          ),
                          
                          )],
                          
                      ),
                    ],
                      
                  ))),
        );
  }
  
  void _saveUserToDatabase() async {
    // Navigator.pop(context);
    int dummyid = await Usercrudoperations().getid();
    Farmer farmer0 = Farmer(dummyid,_latitude0,_longitude0);
    Farmer farmer1 = Farmer(dummyid,_latitude1,_longitude1);
    Farmer farmer2 = Farmer(dummyid,_latitude2,_longitude2);
    Farmer farmer3 = Farmer(dummyid,_latitude3,_longitude3);
    
    Cropfarmer crop1 = Cropfarmer(dummyid,_price,_crop);
    print("result4");
    
    int result4= await Farmercropinteraction().insertcrop(crop1);
  
    
    int result0 = await Farmercrudoperations().insertfarmer(farmer0);
    int result1 = await Farmercrudoperations().insertfarmer(farmer1);
    int result2 = await Farmercrudoperations().insertfarmer(farmer2);
    int result3 = await Farmercrudoperations().insertfarmer(farmer3);
    if((result0 == 0)&&(result1 == 0)&&(result2 == 0)&&(result3 == 0)) {
      _showAlertDialog('Status','Problem saving user to database');
    }
    else {
      _showAlertDialog('Status','Successfully saved user to database');
    }
    }
    
  
void _showAlertDialog(String title, String message) {
    AlertDialog alertDialog = AlertDialog(
      title: Text(title),
      content: Text(message),
    );
    showDialog(
      context: context,
      builder: (_) {
        return alertDialog;
      }
    );
  }
  bool validateLoginForm() {
  final FormState form = formkey.currentState;
  if (form.validate()) {
    form.save();
    return true;
  }
  else
    return false;
  }

  void validateAndSubmit() async {
    if(validateLoginForm()) {
      debugPrint('Validated the form');
        debugPrint('successfully registered User');
        _saveUserToDatabase();
      }
      
    }

 

}