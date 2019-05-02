class UserTable{
  static String userTable='users';
  static String colId = 'id';
  static String colemail = 'email';
  static String colpassword = 'password';
  static String colFirstname='Firstname';
  static String colLastname='lastname';
  static String colStreetname='Streetname';
  static String colState='State';
  static  String colCity='City';
  static String colPincode='Pincode';
  static String colusertype='usertype';
  static String colmobileno='mobileno';
  static String createindex ='indexmail';
  static String createtable='CREATE TABLE $userTable($colId INTEGER PRIMARY KEY AUTOINCREMENT, $colemail TEXT, $colpassword TEXT,$colFirstname TEXT,$colLastname TEXT,$colStreetname TEXT,$colCity TEXT,$colState TEXT,$colPincode TEXT,$colusertype TEXT,$colmobileno TEXT)';

  static String indexSQL = 'CREATE INDEX $createindex  ON $userTable ($colemail)';


}
class FarmerTable{
static String colId = 'id';
static String collongitude='longitude';
static String collatitude='latitude';
static String farmertable='farmer';
static String createtable='CREATE TABLE $farmertable($colId INTEGER  , $collatitude TEXT, $collongitude TEXT ,FOREIGN KEY($colId) REFERENCES ${UserTable.userTable} (${UserTable.colId}) ,CONSTRAINT PK_FARMER PRIMARY KEY($collatitude,$collongitude) )';
    
}
class AgroTable{
static String colId = 'id';
static String colqualifications='qualifications';
static String agroexperttable='agroexpert';
static String mobileno='mobileno';
static String createtable='CREATE TABLE $agroexperttable($colId INTEGER  PRIMARY KEY ,  $colqualifications TEXT,FOREIGN KEY($colId) REFERENCES ${UserTable.userTable}(${UserTable.colId}) )';
    


}
class ClockTable{
static String clockTable='clock_table';
static String colclockId='idf';
static String colDate='date';
static String colTime='time';
static String colReason='reason';
static String colId = 'id';
static String createtable='CREATE TABLE $clockTable($colId INTEGER , $colclockId INTEGER PRIMARY KEY AUTOINCREMENT ,$colDate TEXT,$colTime TEXT,$colReason TEXT,FOREIGN KEY($colId) REFERENCES ${UserTable.userTable}(${UserTable.colId}))';
}
class CropTable{

static String colcrop='crop';
static String colpesticides='pesticides';
static String  cropTable='croptable';
static String createTable='CREATE TABLE $cropTable($colcrop TEXT PRIMARY KEY,$colpesticides Text)';



}

class FarmerAgriInteraction{

static String colfid='fid';
static String colaid='aid';
static String colstatus='status';
static String interactiontable='interactiontable';
static String createTable='CREATE TABLE $interactiontable($colfid INTEGER,$colaid INTEGER ,$colstatus VARCHAR(10) NOT NULL CHECK ($colstatus IN ("filled", "pending")),FOREIGN KEY($colfid) REFERENCES ${FarmerTable.farmertable}(${FarmerTable.colId}) , FOREIGN KEY($colaid) REFERENCES ${AgroTable.agroexperttable}(${AgroTable.colId}),CONSTRAINT PK_AGROFARMERINTRO PRIMARY KEY($colfid,$colaid) )';

}


class Farmercrop{
  static String colfid='fid';
  static String colcropfarmer='crop';
  static String colprice='price';
  static String farmercrop='farmercrop';
  static String createtable='CREATE TABLE $farmercrop($colfid INTEGER,$colcropfarmer VARCHAR(10),$colprice VARCHAR(10),FOREIGN KEY($colfid) REFERENCES ${FarmerTable.farmertable}(${FarmerTable.colId}))';

}
class Trigdelclock{

static String colid='id';
static String colalarmid='alarmid';
static String createTable='CREATE TABLE ${ClockTable.clockTable}_Ondelete($colid INTEGER,$colalarmid INTEGER  )';

}
class Trigupclock{
static String colclockId='idf';
static String colDate='date';
static String colTime='time';
static String colReason='reason';
static String colId = 'id';
static String createtable='CREATE TABLE ${ClockTable.clockTable}_Onupdate($colId INTEGER , $colclockId INTEGER PRIMARY KEY AUTOINCREMENT ,$colDate TEXT,$colTime TEXT,$colReason TEXT)';
}
class Trigupfarm{
  static String colId = 'id';
static String colnewemail='newemail';
static String cololdemail='oldemail';
static String createtable='CREATE TABLE ${UserTable.userTable}_OnUpdate($colId INTEGER  , $colnewemail TEXT, $cololdemail TEXT  )';
    
}