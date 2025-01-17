# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.pushButton_master = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_master.setObjectName("pushButton_master")
        self.gridLayout.addWidget(self.pushButton_master, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_cycle = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_cycle.setEnabled(False)
        self.comboBox_cycle.setObjectName("comboBox_cycle")
        self.comboBox_cycle.addItem("")
        self.gridLayout.addWidget(self.comboBox_cycle, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)
        self.pushButton_charge = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_charge.setEnabled(False)
        self.pushButton_charge.setObjectName("pushButton_charge")
        self.gridLayout.addWidget(self.pushButton_charge, 12, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 9, 0, 1, 1)
        self.pushButton_current = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_current.setEnabled(False)
        self.pushButton_current.setObjectName("pushButton_current")
        self.gridLayout.addWidget(self.pushButton_current, 11, 0, 1, 1)
        self.checkBox_x_y = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_x_y.setEnabled(False)
        self.checkBox_x_y.setObjectName("checkBox_x_y")
        self.gridLayout.addWidget(self.checkBox_x_y, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cycles"))
        self.label_2.setText(_translate("MainWindow", "Settings"))
        self.pushButton_master.setText(_translate("MainWindow", "Load Master file"))
        self.label.setText(_translate("MainWindow", "Load Files"))
        self.comboBox_cycle.setItemText(0, _translate("MainWindow", "1,2"))
        self.label_3.setText(_translate("MainWindow", "Select Cycles"))
        self.label_4.setText(_translate("MainWindow", "Plot (Red, Blue, Green:  This is the order of coloring.)"))
        self.pushButton_charge.setText(_translate("MainWindow", "Voltage vs Charge/Discharge"))
        self.pushButton_current.setText(_translate("MainWindow", "Voltage Vs Current"))
        self.checkBox_x_y.setText(_translate("MainWindow", "X Y"))
        self.label_5.setText(_translate("MainWindow", "Title"))


