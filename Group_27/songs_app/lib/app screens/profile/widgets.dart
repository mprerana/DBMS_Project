import 'package:flutter/material.dart';


// Profile Picture...
Widget buildProfilePicture(BuildContext context, String imageUrl) {

  Size screenSize = MediaQuery.of(context).size;
  
  return Container(
    margin: EdgeInsets.only(left: 30),
    width: screenSize.width / 4.3,
    height: screenSize.width / 4.3,
    decoration: BoxDecoration(
      image: DecorationImage(
        image: AssetImage(imageUrl),
        fit: BoxFit.cover
      ),
      borderRadius: BorderRadius.circular(85),
      border: Border.all(
        color: Colors.white,
        width: 5.0,
      )
    ),
  );
}

// Cover Picture...
Widget buildCoverPicture() {
  return Container(
    child: Image.asset('assets/msc-bg-3.jpg', fit: BoxFit.cover, width: double.infinity, height: 250,),
  );
}


/// Go Back Button...
Widget appBar(BuildContext context) {
  return AppBar(
    backgroundColor: Colors.blue[400],
    leading: IconButton(icon: Icon(Icons.arrow_back), onPressed: () {Navigator.pop(context);},),
    centerTitle: true,
    title: Text('profile'.toUpperCase(), style: TextStyle(fontSize: 30, fontFamily: 'underworld',),),
    actions: <Widget>[
      IconButton(
        icon: Icon(Icons.edit),
        onPressed: () {Navigator.pushNamed(context, '/editProfile');}
      )
    ],
  );
}


Widget userImgName(BuildContext context, String imageUrl, String userName, String email) {

  Size screenSize = MediaQuery.of(context).size;

  return SafeArea(
    child: SingleChildScrollView(
      child: Column(
        children: <Widget>[
          SizedBox(height: screenSize.height / 6.4,),
          Row(
            children: <Widget>[

              buildProfilePicture(context, imageUrl),
              Container(
                margin: EdgeInsets.only(left: 30, top: 30),
                child: Column(
                  children: <Widget>[

                    Text(
                      userName.toUpperCase(),
                      style: TextStyle(
                        fontSize: (screenSize.width * 1.35) / userName.length,
                        fontFamily: 'Halfomania', 
                        fontWeight: FontWeight.bold, 
                        color: Colors.white
                      ),
                    ),
                    Text(
                      email,
                      style: TextStyle(
                        fontFamily: 'Magnificent',
                        fontSize: (screenSize.width * 0.85) / email.length,
                        color: Colors.white
                      ),
                    )

                  ],
                ),
              ),

            ],
          ),
        ],
      ),
    ),
  );
}
