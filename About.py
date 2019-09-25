# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 250)
        Dialog.setMinimumSize(QtCore.QSize(500, 250))
        Dialog.setMaximumSize(QtCore.QSize(500, 250))
        Dialog.setSizeIncrement(QtCore.QSize(500, 250))
        Dialog.setBaseSize(QtCore.QSize(500, 250))
        Dialog.setFocusPolicy(QtCore.Qt.TabFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(250, 250))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(250, 250))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About SRAN Reading Tool"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label.setText(_translate("Dialog", "TextLabel"))

