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
        MainWindow.resize(517, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 13, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 13, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 4, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 2, 2, 3, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 0, 3, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 3)
        self.gridLayout.addLayout(self.gridLayout_3, 5, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 13, 0, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_7.addWidget(self.line_16, 2, 0, 3, 1)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_7.addWidget(self.line_12, 1, 0, 1, 4)
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_7.addWidget(self.line_17, 2, 3, 3, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_7.addWidget(self.checkBox_4, 3, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_7.addWidget(self.checkBox_3, 2, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_7.addWidget(self.checkBox_6, 2, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_7.addWidget(self.checkBox_7, 3, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 7, 1, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 8, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 6, 0, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 12, 0, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout.addWidget(self.line_20, 11, 0, 1, 3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_6.addWidget(self.line_11, 1, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_6.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_6.addWidget(self.line_15, 2, 2, 3, 1)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_6.addWidget(self.line_14, 2, 0, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 7, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_8.addWidget(self.line_18, 2, 0, 2, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_8.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_8.addWidget(self.line_13, 1, 0, 1, 3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_8.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.gridLayout_8.addWidget(self.line_19, 2, 2, 2, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 7, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 2, 4, 3, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 1, 0, 1, 5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 0, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 4, 3, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 3, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_4.addWidget(self.line_6, 2, 0, 3, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 2, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_4.addWidget(self.line_8, 2, 2, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 5, 1, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 10, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 10, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 9, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 517, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Impedance"))
        self.pushButton_4.setText(_translate("MainWindow", "Plot"))
        self.pushButton_5.setText(_translate("MainWindow", "Export"))
        self.label_4.setText(_translate("MainWindow", "Channels"))
        self.checkBox.setText(_translate("MainWindow", "Select all"))
        self.label_3.setText(_translate("MainWindow", "Filter"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter a channel"))
        self.lineEdit.setText(_translate("MainWindow", "1"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter a Channel"))
        self.checkBox_5.setText(_translate("MainWindow", "Apply Fitting"))
        self.label_10.setText(_translate("MainWindow", "Titles"))
        self.checkBox_4.setText(_translate("MainWindow", "x y"))
        self.checkBox_3.setText(_translate("MainWindow", "Title"))
        self.checkBox_6.setText(_translate("MainWindow", "R"))
        self.checkBox_7.setText(_translate("MainWindow", "Con"))
        self.pushButton.setText(_translate("MainWindow", "Main File"))
        self.label_2.setText(_translate("MainWindow", "Settings & Options"))
        self.label.setText(_translate("MainWindow", "Load Files"))
        self.pushButton_2.setText(_translate("MainWindow", "x y File"))
        self.pushButton_7.setText(_translate("MainWindow", "Guess-Model File"))
        self.pushButton_3.setText(_translate("MainWindow", "Config File"))
        self.label_12.setText(_translate("MainWindow", "Plot"))
        self.label_9.setText(_translate("MainWindow", "Missing"))
        self.label_8.setText(_translate("MainWindow", "Enter Missing Channels"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Total: "))
        self.label_11.setText(_translate("MainWindow", "Parameters"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "Enter Area"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "Enter thickness"))
        self.label_7.setText(_translate("MainWindow", "x-axis"))
        self.label_5.setText(_translate("MainWindow", "Scale"))
        self.checkBox_2.setText(_translate("MainWindow", "Use default Scale"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "max"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "min"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "min"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "max"))
        self.label_6.setText(_translate("MainWindow", "y-axis"))
        self.pushButton_6.setText(_translate("MainWindow", "Area-Thickness File"))
        self.comboBox.setItemText(0, _translate("MainWindow", "\"some model\""))
        self.comboBox.setItemText(1, _translate("MainWindow", "some model2"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Guess 1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Guess 2"))
        self.label_13.setText(_translate("MainWindow", "Initial Guess"))
        self.label_14.setText(_translate("MainWindow", "Model"))


