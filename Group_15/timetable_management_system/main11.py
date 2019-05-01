import sqlite3
#from PyQt5 import QtCore, QtGui
#from PyQt5.QtGui import *
#from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
#from PyQt5 import QtWidgets

from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import sys
#from main import MainWindow
#from components import Database as db
from main2 import Main
from gui import Main as a
import main
import os

# # try:
# #     _fromUtf8 = QtCore.QString.fromUtf8
# # except AttributeError:
# #     def _fromUtf8(s):
# #         return s

# try:
#     _encoding = QtGui.QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QtGui.QApplication.translate(context, text, disambig)

def db():
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
    c.execute('create table if not exists users(name TEXT NOT NULL,age INT NOT NULL,username TEXT NOT NULL,password TEXT NOT NULL, gender TEXT NOT NULL)')
    db.commit()
    c.close()
    db.close()

class Ui_win(object):

    # def openWindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     #self.ui = Ui_OtherWindow()
    #     self.ui.setupUi(self.window)
    #     MainWindow.hide()
    #     self.window.show()
    


    def setupUi(self, win):
        # win.setObjectName(_fromUtf8("win"))
        win.setObjectName("MainWindow")
        win.resize(622, 512)
        win.setMinimumSize(QtCore.QSize(622, 512))
        win.setMaximumSize(QtCore.QSize(622, 512))
        self.label = QtWidgets.QLabel(win)
        self.label.setGeometry(QtCore.QRect(210, 10, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(win)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 621, 431))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.accTab = QtWidgets.QWidget()
        self.accTab.setObjectName("accTab")
        self.label_2 = QtWidgets.QLabel(self.accTab)
        self.label_2.setGeometry(QtCore.QRect(180, 0, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.firstname = QtWidgets.QLineEdit(self.accTab)
        self.firstname.setGeometry(QtCore.QRect(100, 70, 201, 41))
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.accTab)
        self.lastname.setGeometry(QtCore.QRect(320, 70, 191, 41))
        self.lastname.setObjectName("lastname")
        self.cr_username = QtWidgets.QLineEdit(self.accTab)
        self.cr_username.setGeometry(QtCore.QRect(100, 130, 351, 41))
        self.cr_username.setObjectName("cr_username")
        self.cr_password = QtWidgets.QLineEdit(self.accTab)
        self.cr_password.setGeometry(QtCore.QRect(100, 180, 351, 41))
        #----------------------------
        self.cr_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cr_password.setText("")
        self.cr_password.setObjectName("cr_password")
        self.cr_age = QtWidgets.QLineEdit(self.accTab)
        self.cr_age.setGeometry(QtCore.QRect(100, 240, 101, 31))
        self.cr_age.setMaxLength(2)
        self.cr_age.setObjectName("cr_age")
        self.male_radio = QtWidgets.QRadioButton(self.accTab)
        self.male_radio.setGeometry(QtCore.QRect(310, 240, 115, 31))
        self.male_radio.setObjectName("male_radio")
        self.female_radio = QtWidgets.QRadioButton(self.accTab)
        self.female_radio.setGeometry(QtCore.QRect(410, 240, 115, 31))
        self.female_radio.setObjectName("female_radio")
        self.label_4 = QtWidgets.QLabel(self.accTab)
        self.label_4.setGeometry(QtCore.QRect(220, 240, 81, 31))
        self.label_4.setObjectName("label_4")
        self.createAccount = QtWidgets.QPushButton(self.accTab)
        self.createAccount.setGeometry(QtCore.QRect(100, 300, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.createAccount.setFont(font)
        self.createAccount.setObjectName("createAccount")
        self.cr_clear = QtWidgets.QPushButton(self.accTab)
        self.cr_clear.setGeometry(QtCore.QRect(350, 300, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.cr_clear.setFont(font)
        self.cr_clear.setObjectName("cr_clear")
        self.tabWidget.addTab(self.accTab, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.label_3 = QtWidgets.QLabel(self.log)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.log_username = QtWidgets.QLineEdit(self.log)
        self.log_username.setGeometry(QtCore.QRect(110, 90, 401, 51))
        self.log_username.setObjectName("log_username")
        self.log_password = QtWidgets.QLineEdit(self.log)
        self.log_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.log_password.setGeometry(QtCore.QRect(110, 170, 401, 51))
        self.log_password.setObjectName("log_password")
        self.log_in = QtWidgets.QPushButton(self.log)
        self.log_in.setGeometry(QtCore.QRect(110, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.log_in.setFont(font)
        self.log_in.setObjectName("log_in")
        self.log_clear = QtWidgets.QPushButton(self.log)
        self.log_clear.setGeometry(QtCore.QRect(320, 250, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.log_clear.setFont(font)
        self.log_clear.setObjectName("log_clear")
        self.tabWidget.addTab(self.log, "")

        self.retranslateUi(win)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "Login Form", None))
        self.label.setText(_translate("win", "LOGIN FORM", None))
        self.label_2.setText(_translate("win", "Create Account ", None))
        self.firstname.setPlaceholderText(_translate("win", "First Name", None))
        self.lastname.setPlaceholderText(_translate("win", "Last Name", None))
        self.cr_username.setPlaceholderText(_translate("win", "Type a username...", None))
        self.cr_password.setPlaceholderText(_translate("win", "Type a password...", None))
        self.cr_age.setPlaceholderText(_translate("win", "Age....", None))
        self.male_radio.setText(_translate("win", "Male", None))
        self.female_radio.setText(_translate("win", "Female", None))
        self.label_4.setText(_translate("win", "Gender: ", None))
        self.createAccount.setText(_translate("win", "Create Account", None))
        self.cr_clear.setText(_translate("win", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.accTab), _translate("win", "Create Account", None))
        self.label_3.setText(_translate("win", "Log In", None))
        self.log_username.setPlaceholderText(_translate("win", "Type username here ....", None))
        self.log_password.setPlaceholderText(_translate("win", "Type password here ....", None))
        self.log_in.setText(_translate("win", "Log In", None))
        self.log_clear.setText(_translate("win", "Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("win", "Log In", None))
        self.cr_clear.clicked.connect(self.clear1)
        self.log_clear.clicked.connect(self.clear2)
        self.createAccount.clicked.connect(self.create_account)
        self.log_in.clicked.connect(self.login)

    def clear1(self):
        self.firstname.setText('')
        self.lastname.setText('')
        self.cr_username.setText('')
        self.cr_password.setText('')
        self.cr_age.setText('')

    def clear2(self):
        self.log_username.setText('')
        self.log_password.setText('')

    def login(self):

        # print("sdfgh")
        # os.system('python main.py')
        # #main.main()
        # self.quit()
        #sys.exit()
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Main.MainWindow(QtWidgets.QMainWindow())
        # self.ui.setupUi(self.window)
        # win.hide()
        # self.window.show()

        
        with sqlite3.connect('users.db') as db:
            c = db.cursor()
            
        username = str(self.log_username.text())
        password = str(self.log_password.text())

        c.execute('SELECT * FROM users WHERE username = ? and password = ?',(username,password))
        data = c.fetchone()
        db.commit()
        if data != None:
            os.system('python main.py')
            sys.exit()
            # info = '''
            #     Name = %s ,

            #     Age = %s,

            #     Gender = %s,

            #     Username = %s,
                
            #     You are Loged In.
            #     Pressing Ok Will Close The Application.
            #         '''  %(data[0],str(data[1]),data[4],data[2])
            # QMessageBox.information(win,"Loged In",info)
            # sys.exit()
        else:
            QMessageBox.critical(win,"Error", 'No Account With That Username And Password')

    def create_account(self):
        try:
            gender = None
            name = str(self.firstname.text()+' '+self.lastname.text())
            age = int(self.cr_age.text())
            username = str(self.cr_username.text())
            password = str(self.cr_password.text())
        
            if self.male_radio.isChecked():
                gender = 'Male'
            if self.female_radio.isChecked():
                gender = 'Female'
            
            with sqlite3.connect('users.db') as db:
                c = db.cursor()
            c.execute('INSERT INTO users VALUES(?,?,?,?,?)',(name,age,username,password,gender))
            db.commit()
            c.execute('SELECT * FROM users')
            db.commit()
            c.close()
            db.close()
            QMessageBox.information(win,"Success!!", 'Account Created Successfully.')
            self.clear1()
            
        except:
            QMessageBox.critical(win,"Error",'Error !!! Check Entries Again .Make Sure No Filed Is Empty.' )
            pass



    
        
            

if __name__ == "__main__" :

    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_win()
    ui.setupUi(win)
    win.show()
    db()


    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # app.exec_()


    sys.exit(app.exec_())
