# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainview.ui'
#
# Created: Tue Jun  2 14:11:06 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainView(object):
    def setupUi(self, MainView):
        MainView.setObjectName(_fromUtf8("MainView"))
        MainView.resize(669, 414)
        self.centralWidget = QtGui.QWidget(MainView)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listView = QtGui.QListView(self.centralWidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        MainView.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainView)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 669, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainView.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainView)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainView.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainView)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainView.setStatusBar(self.statusBar)

        self.retranslateUi(MainView)
        QtCore.QMetaObject.connectSlotsByName(MainView)

    def retranslateUi(self, MainView):
        MainView.setWindowTitle(_translate("MainView", "MainView", None))
        self.label.setText(_translate("MainView", "Put Shellcode:", None))
        self.pushButton.setText(_translate("MainView", "Shellyze", None))

