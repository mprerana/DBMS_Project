import 'package:flutter/material.dart';
import 'package:dbms_final/homepage.dart';
import 'package:dbms_final/customer/customer.dart';
import 'package:dbms_final/farmer/screens/setalarmmain.dart';
import 'package:dbms_final/servies/authentication.dart';
import 'package:dbms_final/login/screens/login.dart';
import 'package:dbms_final/customer/weather.dart';
import 'package:dbms_final/farmer/screens/userprofile.dart';
import 'package:dbms_final/farmer/screens/agroexpert1.dart';
import 'package:dbms_final/customer/newsfeed.dart';

class Farmerinterface extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return _FarmerinterfaceState();
  }
}

class _FarmerinterfaceState extends State<Farmerinterface> {
  int _selectedIndex = 0;
  void redirect(index) {
    if (index == 0) {
      Navigator.of(context)
          .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
        return new Customer();
      }));
    }
    ;
    if (index == 1) {
      Navigator.of(context)
          .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
        return new Viewcityagro();
      }));
    }
    if (index == 2) {
      Navigator.of(context)
          .push(MaterialPageRoute<Null>(builder: (BuildContext context) {
        return new weather();
      }));
    }
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
      redirect(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: new AppBar(
          title: new Directionality(
              textDirection: TextDirection.ltr,
              child: new Text('Farmerinterface')),
          backgroundColor: Color.fromRGBO(40, 80, 40, 0.8)),
      body: Center(
        child: Container(
          child: RaisedButton(
            child: Text('Set alarm'),
            shape: new RoundedRectangleBorder(
                borderRadius: new BorderRadius.circular(30.0)),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => MyAppmain()),
              );
            },
            color: Color.fromRGBO(40, 80, 40, 0.8),
            padding: const EdgeInsets.all(8.0),
            textColor: Colors.white,
          ),
        ),
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
              leading: Customerimage(),
              title: const Text('customer'),
              onTap: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => Customer()));
              },
            ),
            ListTile(
              leading: Newsimage(),
              title: const Text('News'),
              onTap: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => News()));
              },
            ),
            ListTile(
              leading: Agricultureimage(),
              title: const Text('agriculture'),
              onTap: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => Viewcityagro()));
              },
            ),
            ListTile(
              leading: Logoutimage(),
              title: const Text('Logout'),
              onTap: () async {
                await BaseAuth().signOut();
                Navigator.of(context).push(
                    MaterialPageRoute<Null>(builder: (BuildContext context) {
                  return new LoginPage();
                }));
              },
            ),
          ],
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: <BottomNavigationBarItem>[
          BottomNavigationBarItem(
              icon: Icon(Icons.people), title: Text('Customer')),
          BottomNavigationBarItem(
              icon: Icon(Icons.person), title: Text('Experts')),
          BottomNavigationBarItem(
              icon: Icon(Icons.cloud), title: Text('Weather')),
        ],
        currentIndex: _selectedIndex,
        fixedColor: Color.fromRGBO(40, 80, 40, 0.8),
        onTap: _onItemTapped,
      ),
    );
  }
}
