# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Downloads\designMain1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogAddComment(object):
    def setupUi(self, DialogAddComment):
        DialogAddComment.setObjectName("DialogAddComment")
        DialogAddComment.resize(564, 346)
        self.buttonBox = QtWidgets.QDialogButtonBox(DialogAddComment)
        self.buttonBox.setGeometry(QtCore.QRect(180, 280, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DialogAddComment)
        self.label.setGeometry(QtCore.QRect(11, 191, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogAddComment)
        self.label_2.setGeometry(QtCore.QRect(420, 190, 90, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DialogAddComment)
        self.plainTextEdit.setGeometry(QtCore.QRect(379, 51, 171, 99))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.surnameLine = QtWidgets.QLineEdit(DialogAddComment)
        self.surnameLine.setGeometry(QtCore.QRect(190, 90, 133, 20))
        self.surnameLine.setObjectName("surnameLine")
        self.spinBox = QtWidgets.QSpinBox(DialogAddComment)
        self.spinBox.setGeometry(QtCore.QRect(11, 90, 31, 20))
        self.spinBox.setMaximum(5)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(DialogAddComment)
        self.label_3.setGeometry(QtCore.QRect(220, 190, 67, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DialogAddComment)
        QtCore.QMetaObject.connectSlotsByName(DialogAddComment)

    def retranslateUi(self, DialogAddComment):
        _translate = QtCore.QCoreApplication.translate
        DialogAddComment.setWindowTitle(_translate("DialogAddComment", "Dialog"))
        self.label.setText(_translate("DialogAddComment", "Set rating(1-5)"))
        self.label_2.setText(_translate("DialogAddComment", "Add your comment"))
        self.label_3.setText(_translate("DialogAddComment", "Your Surname"))
