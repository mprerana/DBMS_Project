#def main():

#print("zxcv")
from PyQt5 import QtWidgets
from main1 import Database as db
from main2 import Main
import sys

	# Entry point for application
if __name__ == '__main__':
	#print("1234")
    if not db.checkSetup():
        db.setup()
 #   print("1234")    
    app = QtWidgets.QApplication(sys.argv)
    parent = QtWidgets.QMainWindow()
    Main.MainWindow(parent)
    parent.show()
    sys.exit(app.exec_())
