# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rec.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import csv
import random
#import re

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

reccomendation_based_on_current_author=[]
reccomendation_based_on_average_ratings=[]
reccomendation_based_on_genre=[]

class Ui_Recwindow(object):

    def recommend(self,searched_buk):
        print "You searched for :- ", searched_buk                 #   book name accessed !

           

           # Suggestions to choose book and obtain accurate name

        ################################################################################################################################################################
            
        #    for line in csv_reader:            
        #        for suggested_buk in line['title'].split('\n'):
        #            if(searched_buk in suggested_buk):
        #                print suggested_buk                                     # suggestions for input book search 
             
        ####################################################################################################################################################
        



            #####  Recommendation Trial code !!!!
        with open('output.csv','r') as csv_file:
            data= csv.DictReader(csv_file)
            current_author=""
            current_genre=""

            for line in data:
                if(searched_buk.lower() == line['title'].lower()):
                    current_author=line['authors']
                    current_genre=line['genre']

            print "Current authors:  ", current_author                      #### Current authors based on selected book 
            print "Current genre:  ", current_genre	                     #### Current authors based on selected book 

            csv_file.seek(0)                                                #### Set DictReader back to start of file

            ###############  Books From Similar author

            del reccomendation_based_on_current_author[:]               #######     CLears contents of global lists
            del reccomendation_based_on_average_ratings[:]
            del reccomendation_based_on_genre[:]               			#######

            for line in data:
                if(line['title'].lower() == searched_buk.lower()):
                    continue
                if(len(set(line['authors'].split(',')).intersection(set(current_author.split(',')))) > 0 ):
                    reccomendation_based_on_current_author.append(line['title'])        

            if(len(reccomendation_based_on_current_author) > 0):
                print " \n Also from :",  current_author 
                print "\n", reccomendation_based_on_current_author                              ######   Reccomends books based on atleast one author
                print " \n Enjoy your Book ! \n "
            else:
                print " \n Enjoy your Book ! \n "   

            print "*****************************************************************************************************************************************"
            


            csv_file.seek(0)

                #####################   Top Rated Books 
            next(data)                                                                              ### We dont want the headers in list        

            for line in data:
                if(line['average_rating'] >= str(4.5) ):
                    reccomendation_based_on_average_ratings.append(line['title'])                   ######   Recommends books based on average ratings of all books

            if(len(reccomendation_based_on_average_ratings) > 0):
                print "\n Also Check Out Top Rated Books in all Categories : \n"
                print reccomendation_based_on_average_ratings
                print "\n Thanks & Keep Reading \n"     
            
            print "*****************************************************************************************************************************************"

            csv_file.seek(0)

            ###########  Books based on same genre

            next(data)

            for line in data:
            	if(line['genre'] == current_genre):
            		reccomendation_based_on_genre.append(line['title'])				########   Recommends Based on Genre 
            		
            print "\n Similar Genre Books: \n"		
            print reccomendation_based_on_genre	        		

            print "*****************************************************************************************************************************************"
			
 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 598)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(90, 150, 256, 192))
        self.listWidget.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);\n"
"color:rgb(0, 0, 0);"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.addItems(reccomendation_based_on_current_author)				##### DiSplays other books based on current author

        self.listWidget_2 = QtGui.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(420, 150, 256, 192))
        self.listWidget_2.setStyleSheet(_fromUtf8("background-color: rgb(85, 255, 255);\n"
"color:rgb(0, 0, 0);"))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.listWidget_2.addItems(random.sample(reccomendation_based_on_genre, 10))				##### DiSplays other books based on ratings

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 321, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("color:rgb(255, 38, 19);\n"
"background-color:rgb(255, 255, 0);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(125, 125, 200, 27))
        self.lineEdit_2.setStyleSheet(_fromUtf8("color:rgb(255, 38, 19);\n"
"background-color:rgb(255, 255, 0);"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(455, 125, 200, 27))
        self.lineEdit_3.setStyleSheet(_fromUtf8("color:rgb(255, 38, 19);\n"
"background-color:rgb(255, 255, 0);"))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))   

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 340, 101, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(145, 145, 145);\n"
"color:rgb(85, 85, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lineEdit.setText(_translate("MainWindow", "                           Recommeded to read", None))
        self.lineEdit_2.setText(_translate("MainWindow", "  Also From this Author ", None))
        self.lineEdit_3.setText(_translate("MainWindow", "     Similar Genre Books  ", None))
        self.pushButton.setText(_translate("MainWindow", "Search Book", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_Recwindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

