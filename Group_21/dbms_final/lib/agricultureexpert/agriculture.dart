import 'dart:async';
import 'package:dbms_final/Components/Form.dart';
import 'package:dbms_final/farmer/screens/userprofile.dart';
import 'package:dbms_final/homepage.dart';
import 'package:dbms_final/servies/authentication.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:dbms_final/login/screens/login.dart';
import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:dbms_final/utils/dbhelper.dart';
import 'package:dbms_final/utils/datbasefiles/farmeragrointeractioncrud.dart';
class Viewagro extends StatefulWidget {
 
  @override
  State<StatefulWidget> createState() {
    return _ViewagroState();
  }
}

class _ViewagroState extends State<Viewagro> {
  
  DatabaseHelper databaseHelper = DatabaseHelper();
  
  List<Map<String,dynamic >>agroList;
  List<Map<String,dynamic >>userList;
  List<Map<String,dynamic >>useralllist;
  int count = 0;
  int count1=0;
  var i=0;
  @override
  Widget build(BuildContext context) {

    if(agroList == null) {
      agroList =List<Map<String,dynamic >>();
      updateagroListView();
      print(agroList.toString());
      print("hii");
    }

    return Scaffold(
      appBar: AppBar(
        title: Text('All Requests'),
         backgroundColor: Color.fromRGBO(40, 80, 40, 0.8),
      ),
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: getlistView(),
      ),
      drawer: new Drawer(
        child: new ListView(
          padding: new EdgeInsets.only(top: 30.0, left: 10.0),
          children: <Widget>[
            ListTile(
              leading: Editimage(),
              title: const Text('Edit Profile'),
              onTap: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => UserProfile()));
              },
            ),
            ListTile(
              leading: Logoutimage(),
              title: const Text('Logout'),
            ),
          ],
        ),
      ),
      
    );
  }

  ListView getlistView() {
    TextStyle textStyle = Theme.of(context).textTheme.subhead;
    return ListView.builder(
      itemCount: count,
      itemBuilder: (BuildContext context,int position) {
        print(agroList[position]['fid']);
        userListview(agroList[position]['fid']);
        print(userList.toString());
        return 
        Container(
          
          child:Card(
          color: Colors.white,
          elevation: 2.0,
          child: ListTile(
            title: Text(this.agroList[position]['fid'].toString(), style: textStyle),
             subtitle: Text("accept"),
               onTap: (){

									    	setState(() {
									    	  debugPrint("Save button clicked");
									    	  // agrostatusupdate(agroList[position]['fid']);
									    	});
									    },
                ),
          ),
         
        decoration: new BoxDecoration(boxShadow:[
            new BoxShadow(
              color:Colors.green[200],
              blurRadius: 20.0,
            ),
        ],
        ),

        
    
     );
      }
            
          );
      
  }

  
void navigatetodetail(BuildContext context, Map<String,dynamic> cityagroList){
     

}
  

  
  void updateagroListView() async{
    
    final Future<Database> dbFuture = databaseHelper.database;
    FirebaseUser user = await BaseAuth().getCurrentUser();
    //print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);

    
    String status = 'pending';
    dbFuture.then((database) {
      Future<List<Map<String,dynamic >>> agrofuture = Farmeragrointeraction().getinterList(userrecord['id'],status);
      agrofuture.then((agrofuture) {
        setState(() {
        
        this.agroList = agrofuture;
        print("xrctfvgbhn");
        // print(agrofuture.length);
        this.count = agrofuture.length; 
        });
      });
    });
  }

    void userListview(int dummyid) async{
      List<Map<String,dynamic >> userList = await Usercrudoperations().getuserwithid(dummyid);
     
        
        
        print(userList.toString());
      
  }
  
  void agrostatusupdate(int fid) async{
    int result;
     
    //print(user.email);
    FirebaseUser user = await BaseAuth().getCurrentUser();
    //print(user.email);
    var userrecord = await Usercrudoperations().getUserwithEmail(user.email);

    
    result=await Farmeragrointeraction().updatestatus(fid,userrecord['id']);
    if(result!=0){
      
     	_showAlertDialog('Status', 'Successfully');
        
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
