# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddClient.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddService(object):
    def setupUi(self, AddService):
        AddService.setObjectName("AddService")
        AddService.resize(476, 143)
        self.gridLayoutWidget = QtWidgets.QWidget(AddService)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 451, 127))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 8)

        self.retranslateUi(AddService)
        self.lineEdit_3.returnPressed.connect(self.lineEdit.setFocus)
        QtCore.QMetaObject.connectSlotsByName(AddService)

    def retranslateUi(self, AddService):
        _translate = QtCore.QCoreApplication.translate
        AddService.setWindowTitle(_translate("AddService", "Add Service"))
        self.label.setText(_translate("AddService", "Client Name"))
        self.label_3.setText(_translate("AddService", "Age"))
        self.pushButton.setText(_translate("AddService", "Add"))
        self.label_2.setText(_translate("AddService", "Gender"))
        self.pushButton_2.setText(_translate("AddService", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddService = QtWidgets.QDialog()
    ui = Ui_AddService()
    ui.setupUi(AddService)
    AddService.show()
    sys.exit(app.exec_())

