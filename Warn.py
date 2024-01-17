# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warn.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes m
# ade in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WarnWindow(object):
    def setupUi(self, WarnWindow):
        WarnWindow.setObjectName("WarnWindow")
        width = 320
        height = 114
        WarnWindow.setFixedSize(width, height)
        WarnWindow.setWindowIcon(QtGui.QIcon('Logo.ico'))
        self.buttonBox = QtWidgets.QDialogButtonBox(WarnWindow)
        self.buttonBox.setGeometry(QtCore.QRect(140, 80, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(WarnWindow)
        self.pushButton.setGeometry(QtCore.QRect(10, 83, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(WarnWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(WarnWindow)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 81, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Warn.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(WarnWindow)
        self.buttonBox.accepted.connect(WarnWindow.accept)
        self.buttonBox.rejected.connect(WarnWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(WarnWindow)
        
        self.pushButton.setStyleSheet("background-color:#232326;")
        self.buttonBox.setStyleSheet("background-color:#232326;")
        WarnWindow.setStyleSheet("QWidget{\n"
          "background-color: rgb(0, 3, 18);\n"
          "color:rgb(255, 255, 255);\n"
          "}")

    def retranslateUi(self, WarnWindow):
        _translate = QtCore.QCoreApplication.translate
        WarnWindow.setWindowTitle(_translate("WarnWindow", "Warning"))
        self.pushButton.setText(_translate("WarnWindow", "Delete All"))
        self.label.setText(_translate("WarnWindow", "Are you sure you want to delete this item?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WarnWindow = QtWidgets.QDialog()
    ui = Ui_WarnWindow()
    ui.setupUi(WarnWindow)
    WarnWindow.show()
    sys.exit(app.exec_())

