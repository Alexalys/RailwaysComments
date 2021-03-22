# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class UiAddShowComment(object):
    def setup_ui(self, comment):
        comment.setObjectName("Comment")
        comment.resize(349, 219)
        comment.setWhatsThis("")
        comment.setAccessibleName("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(comment)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ButtonSee = QtWidgets.QPushButton(comment)
        self.ButtonSee.setMinimumSize(QtCore.QSize(0, 23))
        self.ButtonSee.setObjectName("ButtonSee")
        self.horizontalLayout.addWidget(self.ButtonSee)
        self.ButtonAdd = QtWidgets.QPushButton(comment)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.horizontalLayout.addWidget(self.ButtonAdd)

        self.retranslate_ui(comment)
        QtCore.QMetaObject.connectSlotsByName(comment)
        comment.setTabOrder(self.ButtonSee, self.ButtonAdd)

    def retranslate_ui(self, comment):
        _translate = QtCore.QCoreApplication.translate
        comment.setWindowTitle(_translate("Comment", "Feedback"))
        self.ButtonSee.setText(_translate("Comment", "See comments"))
        self.ButtonAdd.setText(_translate("Comment", "Add comment"))
