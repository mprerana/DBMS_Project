import 'package:dbms_final/farmer/models/clock.dart';
import 'package:dbms_final/login/models/agro.dart';
import 'package:dbms_final/login/models/farmer.dart';
import 'package:dbms_final/login/models/user.dart';

import 'package:dbms_final/utils/datbasefiles/agrocrud.dart';
import 'package:dbms_final/utils/datbasefiles/clockcrud.dart';
import 'package:dbms_final/utils/datbasefiles/farmercrud.dart';
import 'package:dbms_final/utils/datbasefiles/usersCRUD.dart';

class InitData {
  static InitData _initData;

  InitData._createInstance();

  factory InitData() {
    if (_initData == null) {
      _initData = InitData._createInstance();
      _populateDatatoDatabase();
    }
    return _initData;
  }

  static void _populateDatatoDatabase() async {
    List<User> userlist = List<User>();
    List<Farmer> farmerlatloglist = List<Farmer>();
    List<Agro> agroqualificationlist = List<Agro>();
    List<  Clockset> alarmlist = List<Clockset>();
    String fName = 'firstName';
    String lName = 'lastName';
    String pesticide = 'pesticide';
    String emailprfx = 'user';
    String emailsfx = '@gmail.com';
    String streetname = 'ganganammapet';
    String mobileno='98765432';
    int count = 0;
    int count1 = 0;
    int sufix = 1;
    int mobilesufix=10;
    List<String> usertype = ['Farmer', 'AgricultureExpert', 'Customer'];
    List<String> city = ['tenali', 'hyderabad', 'vadodara', 'panaji', 'kochi'];
    List<String> state = [
      'andhrapradesh',
      'telangana',
      'gujarath',
      'goa',
      'kerala'
    ];
    List<String> pincode = ['522201', '500010', '300018', '403002', '682001'];


//populate users table
    for (var i = 0; i < 50; i++, count++, count1++,mobilesufix++) {
      userlist.add(User(
          emailprfx + sufix.toString() + emailsfx,
          i.toString(),
          fName + sufix.toString(),
          lName + sufix.toString(),
          streetname + sufix.toString(),
          city[count],
          state[count],
          pincode[count],
          usertype[count1],
          mobileno+mobilesufix.toString()
          ));

      sufix += 1;
      if (count == 4) count = -1;
      if (count1 == 2) count1 = -1;
      
    }

    for (int i = 0; i < userlist.length; i++) {
      await Usercrudoperations().insertUser(userlist[i]);
    }
//populate farmers table
    count = 0;
    for (int i = 0; i < 50; i = i +1, count = count + 4) {
      print(i);
      if (userlist[i].usertype == 'Farmer'){
        print(i);
      farmerlatloglist.add(Farmer(i+1, count.toString(), count.toString()));
      farmerlatloglist
          .add(Farmer(i+1, (count + 1).toString(), (count + 1).toString()));
      farmerlatloglist
          .add(Farmer(i+1, (count + 2).toString(), (count + 2).toString()));
      farmerlatloglist
          .add(Farmer(i+1, (count + 3).toString(), (count + 3).toString()));
      }

    }
    


    for (int i = 0; i < farmerlatloglist.length; i++) {
      await Farmercrudoperations().insertfarmer(farmerlatloglist[i]);
    }

    
//populte agrotable
    for (int i = 0; i < 50; i = i +1) {
      if (userlist[i].usertype == 'AgricultureExpert') {
        agroqualificationlist.add(Agro(i+1,'B.Sc'));

      }
    }
    for (int i = 0; i < agroqualificationlist.length; i++) {
      await Agrocrudoperations().insertagro(agroqualificationlist[i]);
      print('agro inserted');
    }
    //populate alarm table
    count=1;
    count1=1;
    for(int i=0;i<40;i=i+4,count++,count1++)
    {
      String year='2020';
      String seperatordate='-';
      String seperatortime=':';
      String datealrm=year+seperatordate+count1.toString()+seperatordate+count.toString();
      String timealarm='5'+seperatortime+'45';
        alarmlist.add(Clockset(farmerlatloglist[i].id,count,datealrm,timealarm,pesticide+count.toString()));
        if(count1==12) count1=0;
        if(count==28) count=0;
    }

    for(int i=0;i<alarmlist.length;i++)
    {
    
      await Clockcrudoperations().insertTime(alarmlist[i]);
    }
  }
}
