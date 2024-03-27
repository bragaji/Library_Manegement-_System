# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book_search.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import rec as r

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
	    return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
	    return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
	    return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

	def search(self):
		name=str(self.lineEdit.text())

		if(name == "\0"):
			print("No choice")
		else:
			print "Book selected is:", name
			self.send=r.Ui_Recwindow()			#	 sending to rec.py for recommendations
			self.send.recommend(name)



			#	Open recommendation window

			self.window=QtGui.QMainWindow()
			self.ui=r.Ui_Recwindow()
			self.ui.setupUi(self.window)
			self.window.show()
			MainWindow.hide()


	def setupUi(self, MainWindow):
	    MainWindow.setObjectName(_fromUtf8("MainWindow"))
	    MainWindow.resize(800, 600)
	    MainWindow.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 127)"))
	    self.centralwidget = QtGui.QWidget(MainWindow)
	    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

	    self.pushButton = QtGui.QPushButton(self.centralwidget)
	    self.pushButton.setGeometry(QtCore.QRect(320, 210, 97, 27))
	    self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(255, 170, 0);\n"
	"color:rgb(0, 0,0)"))
	    self.pushButton.setObjectName(_fromUtf8("pushButton"))

	    self.lineEdit = QtGui.QLineEdit(self.centralwidget)
	    self.lineEdit.setGeometry(QtCore.QRect(243, 154, 271, 41))
	    self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
	    self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
	    MainWindow.setCentralWidget(self.centralwidget)
	    
	    self.statusbar = QtGui.QStatusBar(MainWindow)
	    self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
	    self.statusbar.setSizeGripEnabled(True)
	    self.statusbar.setObjectName(_fromUtf8("statusbar"))
	    MainWindow.setStatusBar(self.statusbar)

	    self.pushButton.clicked.connect(self.search)

	    self.retranslateUi(MainWindow)
	    QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
		self.pushButton.setText(_translate("MainWindow", "search book", None))
		

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

