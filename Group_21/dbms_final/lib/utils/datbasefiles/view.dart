import 'package:dbms_final/utils/datbasefiles/databasetables.dart';
class Views {

  
  static String getfarmerslist = 'CREATE VIEW getfarmerslist AS '+
                                    'SELECT (${UserTable.colId}) '+
                                     'FROM ${UserTable.userTable} WHERE ${UserTable.colusertype}=Farmer';
  static String getagricultureslist = 'CREATE VIEW getagricultureslist AS '+
                                    'SELECT (${UserTable.colId}) '+
                                     'FROM ${UserTable.userTable} WHERE ${UserTable.colusertype}=AgricultureExpert';
  static String getcustomerslist = 'CREATE VIEW getcustomerslist AS '+
                                    'SELECT (${UserTable.colId}) '+
                                     'FROM ${UserTable.userTable} WHERE ${UserTable.colusertype}=Customer';                                     

}