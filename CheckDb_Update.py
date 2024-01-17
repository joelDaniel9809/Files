# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckDb.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CheckDb(object):
    def setupUi(self, CheckDb):
        CheckDb.setObjectName("CheckDb")
        CheckDb.resize(433, 357)
        self.buttonBox = QtWidgets.QDialogButtonBox(CheckDb)
        self.buttonBox.setGeometry(QtCore.QRect(80, 300, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(CheckDb)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 410, 281))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.label_3 = QtWidgets.QLabel(CheckDb)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(CheckDb)
        self.checkBox.setGeometry(QtCore.QRect(270, 330, 141, 17))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(CheckDb)
        self.buttonBox.accepted.connect(CheckDb.accept)
        self.buttonBox.rejected.connect(CheckDb.reject)
        QtCore.QMetaObject.connectSlotsByName(CheckDb)

    def retranslateUi(self, CheckDb):
        _translate = QtCore.QCoreApplication.translate
        CheckDb.setWindowTitle(_translate("CheckDb", "Dialog"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("CheckDb", " 1 "))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("CheckDb", " 2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("CheckDb", " 3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("CheckDb", " 4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("CheckDb", "Service"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("CheckDb", "Price"))
        self.label_3.setText(_translate("CheckDb", "Tip: You Can Double Clic on any Row of the table to delete it"))
        self.checkBox.setText(_translate("CheckDb", "Edit Values"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckDb = QtWidgets.QDialog()
    ui = Ui_CheckDb()
    ui.setupUi(CheckDb)
    CheckDb.show()
    sys.exit(app.exec_())

