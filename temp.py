import sys 
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

#Excel
from openpyxl import Workbook


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Main.ui",self)
        
        
    



#main
app= QApplication(sys.argv)
mainwindow= MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(460)
widget.setFixedWidth(430)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")