# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/pyQtEpisoder.ui'
#
# Created: Thu Sep 26 00:30:01 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Episoder(object):
    def setupUi(self, Episoder):
        Episoder.setObjectName(_fromUtf8("Episoder"))
        Episoder.resize(473, 325)
        self.horizontalLayout = QtGui.QHBoxLayout(Episoder)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.view = QtGui.QTableView(Episoder)
        self.view.setObjectName(_fromUtf8("view"))
        self.horizontalLayout.addWidget(self.view)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bUpdate = QtGui.QPushButton(Episoder)
        self.bUpdate.setObjectName(_fromUtf8("bUpdate"))
        self.verticalLayout.addWidget(self.bUpdate)
        self.bAdd = QtGui.QPushButton(Episoder)
        self.bAdd.setObjectName(_fromUtf8("bAdd"))
        self.verticalLayout.addWidget(self.bAdd)
        self.bRemove = QtGui.QPushButton(Episoder)
        self.bRemove.setObjectName(_fromUtf8("bRemove"))
        self.verticalLayout.addWidget(self.bRemove)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.bClose = QtGui.QPushButton(Episoder)
        self.bClose.setObjectName(_fromUtf8("bClose"))
        self.verticalLayout.addWidget(self.bClose)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Episoder)
        QtCore.QObject.connect(self.bClose, QtCore.SIGNAL(_fromUtf8("clicked()")), Episoder.close)
        QtCore.QMetaObject.connectSlotsByName(Episoder)

    def retranslateUi(self, Episoder):
        Episoder.setWindowTitle(_translate("Episoder", "Episoder", None))
        self.bUpdate.setText(_translate("Episoder", "Update", None))
        self.bAdd.setText(_translate("Episoder", "Add", None))
        self.bRemove.setText(_translate("Episoder", "Remove", None))
        self.bClose.setText(_translate("Episoder", "Close", None))

