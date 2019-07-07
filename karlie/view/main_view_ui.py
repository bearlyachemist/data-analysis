# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.button_capacity = QtWidgets.QPushButton(self.centralwidget)
        self.button_capacity.setEnabled(False)
        self.button_capacity.setObjectName("button_capacity")
        self.gridLayout.addWidget(self.button_capacity, 16, 3, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout.addWidget(self.line_20, 13, 0, 1, 4)
        self.button_avg_volt = QtWidgets.QPushButton(self.centralwidget)
        self.button_avg_volt.setEnabled(False)
        self.button_avg_volt.setObjectName("button_avg_volt")
        self.gridLayout.addWidget(self.button_avg_volt, 16, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setEnabled(False)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 17, 0, 1, 4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 7, 0, 1, 4)
        self.button_export = QtWidgets.QPushButton(self.centralwidget)
        self.button_export.setEnabled(False)
        self.button_export.setObjectName("button_export")
        self.gridLayout.addWidget(self.button_export, 18, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.button_x_y_file = QtWidgets.QPushButton(self.centralwidget)
        self.button_x_y_file.setObjectName("button_x_y_file")
        self.gridLayout.addWidget(self.button_x_y_file, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 15, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 11, 0, 1, 4)
        self.label_mass_file = QtWidgets.QLabel(self.centralwidget)
        self.label_mass_file.setObjectName("label_mass_file")
        self.gridLayout.addWidget(self.label_mass_file, 3, 0, 1, 4)
        self.label_config_file = QtWidgets.QLabel(self.centralwidget)
        self.label_config_file.setObjectName("label_config_file")
        self.gridLayout.addWidget(self.label_config_file, 5, 0, 1, 4)
        self.button_mass_file = QtWidgets.QPushButton(self.centralwidget)
        self.button_mass_file.setObjectName("button_mass_file")
        self.gridLayout.addWidget(self.button_mass_file, 1, 1, 1, 1)
        self.medusa_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.medusa_file_button.setAutoFillBackground(False)
        self.medusa_file_button.setStyleSheet("")
        self.medusa_file_button.setObjectName("medusa_file_button")
        self.gridLayout.addWidget(self.medusa_file_button, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_karlie_mapping = QtWidgets.QLabel(self.centralwidget)
        self.label_karlie_mapping.setStyleSheet("color: green; font: bold")
        self.label_karlie_mapping.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_karlie_mapping.setObjectName("label_karlie_mapping")
        self.gridLayout_6.addWidget(self.label_karlie_mapping, 0, 2, 1, 1)
        self.label_eloi_mapping = QtWidgets.QLabel(self.centralwidget)
        self.label_eloi_mapping.setObjectName("label_eloi_mapping")
        self.gridLayout_6.addWidget(self.label_eloi_mapping, 0, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 0, 1, 1, 1)
        self.slider_mapping = QtWidgets.QSlider(self.centralwidget)
        self.slider_mapping.setStyleSheet("\n"
"QSlider::handle:horizontal {\n"
"    background-color: green;\n"
"    }")
        self.slider_mapping.setMaximum(1)
        self.slider_mapping.setPageStep(10)
        self.slider_mapping.setOrientation(QtCore.Qt.Horizontal)
        self.slider_mapping.setObjectName("slider_mapping")
        self.gridLayout_6.addWidget(self.slider_mapping, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_6.setColumnStretch(0, 3)
        self.gridLayout_6.setColumnStretch(3, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 0, 2, 1, 2)
        self.label_medusa_file = QtWidgets.QLabel(self.centralwidget)
        self.label_medusa_file.setObjectName("label_medusa_file")
        self.gridLayout.addWidget(self.label_medusa_file, 2, 0, 1, 4)
        self.button_config_file = QtWidgets.QPushButton(self.centralwidget)
        self.button_config_file.setObjectName("button_config_file")
        self.gridLayout.addWidget(self.button_config_file, 1, 3, 1, 1)
        self.button_norm_curr_volt = QtWidgets.QPushButton(self.centralwidget)
        self.button_norm_curr_volt.setEnabled(False)
        self.button_norm_curr_volt.setObjectName("button_norm_curr_volt")
        self.gridLayout.addWidget(self.button_norm_curr_volt, 16, 0, 1, 1)
        self.button_charge_discharge = QtWidgets.QPushButton(self.centralwidget)
        self.button_charge_discharge.setEnabled(False)
        self.button_charge_discharge.setObjectName("button_charge_discharge")
        self.gridLayout.addWidget(self.button_charge_discharge, 16, 1, 1, 1)
        self.label_x_y_file = QtWidgets.QLabel(self.centralwidget)
        self.label_x_y_file.setObjectName("label_x_y_file")
        self.gridLayout.addWidget(self.label_x_y_file, 4, 0, 1, 4)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)
        self.lineEdit_cycle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cycle.setEnabled(False)
        self.lineEdit_cycle.setInputMask("")
        self.lineEdit_cycle.setObjectName("lineEdit_cycle")
        self.gridLayout_2.addWidget(self.lineEdit_cycle, 4, 1, 1, 1)
        self.checkbox_cycle = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_cycle.setEnabled(False)
        self.checkbox_cycle.setChecked(True)
        self.checkbox_cycle.setObjectName("checkbox_cycle")
        self.gridLayout_2.addWidget(self.checkbox_cycle, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.checkbox_channel = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_channel.setEnabled(False)
        self.checkbox_channel.setChecked(True)
        self.checkbox_channel.setObjectName("checkbox_channel")
        self.gridLayout_2.addWidget(self.checkbox_channel, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 3, 1, 1)
        self.lineEdit_channel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_channel.setEnabled(False)
        self.lineEdit_channel.setToolTipDuration(-1)
        self.lineEdit_channel.setObjectName("lineEdit_channel")
        self.gridLayout_2.addWidget(self.lineEdit_channel, 4, 3, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 2, 2, 3, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 2, 0, 3, 1)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_2.addWidget(self.line_13, 2, 4, 3, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 1, 0, 1, 5)
        self.gridLayout.addLayout(self.gridLayout_2, 10, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_scale_x_min = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_scale_x_min.setEnabled(False)
        self.lineEdit_scale_x_min.setObjectName("lineEdit_scale_x_min")
        self.gridLayout_4.addWidget(self.lineEdit_scale_x_min, 3, 1, 1, 1)
        self.lineEdit_scale_x_max = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_scale_x_max.setEnabled(False)
        self.lineEdit_scale_x_max.setObjectName("lineEdit_scale_x_max")
        self.gridLayout_4.addWidget(self.lineEdit_scale_x_max, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 1, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_4.addWidget(self.line_15, 2, 2, 3, 1)
        self.lineEdit_scale_y_min = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_scale_y_min.setEnabled(False)
        self.lineEdit_scale_y_min.setObjectName("lineEdit_scale_y_min")
        self.gridLayout_4.addWidget(self.lineEdit_scale_y_min, 3, 3, 1, 1)
        self.lineEdit_scale_y_max = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_scale_y_max.setEnabled(False)
        self.lineEdit_scale_y_max.setObjectName("lineEdit_scale_y_max")
        self.gridLayout_4.addWidget(self.lineEdit_scale_y_max, 4, 3, 1, 1)
        self.checkbox_scale_default = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_scale_default.setEnabled(False)
        self.checkbox_scale_default.setChecked(True)
        self.checkbox_scale_default.setObjectName("checkbox_scale_default")
        self.gridLayout_4.addWidget(self.checkbox_scale_default, 0, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 2, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_4.addWidget(self.line_14, 2, 0, 3, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 2, 4, 3, 1)
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_4.addWidget(self.line_12, 1, 0, 1, 5)
        self.gridLayout.addLayout(self.gridLayout_4, 10, 2, 1, 2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 0, 1, 1, 2)
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.gridLayout_7.addWidget(self.line_22, 2, 2, 3, 1)
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.gridLayout_7.addWidget(self.line_23, 1, 0, 1, 3)
        self.checkbox_x_y_plot_label = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_x_y_plot_label.setEnabled(False)
        self.checkbox_x_y_plot_label.setChecked(True)
        self.checkbox_x_y_plot_label.setObjectName("checkbox_x_y_plot_label")
        self.gridLayout_7.addWidget(self.checkbox_x_y_plot_label, 3, 1, 1, 1)
        self.checkbox_show_title = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_show_title.setEnabled(False)
        self.checkbox_show_title.setChecked(True)
        self.checkbox_show_title.setObjectName("checkbox_show_title")
        self.gridLayout_7.addWidget(self.checkbox_show_title, 2, 1, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_7.addWidget(self.line_21, 2, 0, 3, 1)
        self.gridLayout.addLayout(self.gridLayout_7, 12, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 14, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 1, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_3.addWidget(self.line_16, 2, 0, 2, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)
        self.lineEdit_min_voltage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_min_voltage.setEnabled(False)
        self.lineEdit_min_voltage.setObjectName("lineEdit_min_voltage")
        self.gridLayout_3.addWidget(self.lineEdit_min_voltage, 3, 1, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 1, 0, 1, 5)
        self.checkbox_default_voltage_range = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_default_voltage_range.setEnabled(False)
        self.checkbox_default_voltage_range.setChecked(True)
        self.checkbox_default_voltage_range.setObjectName("checkbox_default_voltage_range")
        self.gridLayout_3.addWidget(self.checkbox_default_voltage_range, 0, 3, 1, 1)
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_3.addWidget(self.line_18, 2, 4, 2, 1)
        self.lineEdit_max_voltage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_max_voltage.setEnabled(False)
        self.lineEdit_max_voltage.setObjectName("lineEdit_max_voltage")
        self.gridLayout_3.addWidget(self.lineEdit_max_voltage, 3, 3, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_3.addWidget(self.line_17, 2, 2, 2, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 12, 0, 1, 2)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_8.addWidget(self.line_10, 2, 2, 2, 1)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_8.addWidget(self.line_9, 1, 0, 1, 3)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_8.addWidget(self.line_8, 2, 0, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 1, 1, 2)
        self.button_reset_config = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset_config.setEnabled(False)
        self.button_reset_config.setObjectName("button_reset_config")
        self.gridLayout_8.addWidget(self.button_reset_config, 3, 1, 1, 1)
        self.button_reset_mass = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset_mass.setEnabled(False)
        self.button_reset_mass.setObjectName("button_reset_mass")
        self.gridLayout_8.addWidget(self.button_reset_mass, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 12, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.menubar.setObjectName("menubar")
        self.menuwhats_here = QtWidgets.QMenu(self.menubar)
        self.menuwhats_here.setObjectName("menuwhats_here")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_github = QtWidgets.QAction(MainWindow)
        self.action_github.setObjectName("action_github")
        self.menuwhats_here.addAction(self.action_about)
        self.menuwhats_here.addSeparator()
        self.menuwhats_here.addAction(self.action_github)
        self.menubar.addAction(self.menuwhats_here.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Karlie\'s Application"))
        self.button_capacity.setText(_translate("MainWindow", "Capacity vs Cycle"))
        self.button_avg_volt.setText(_translate("MainWindow", "Average Voltage vs Cycle"))
        self.button_export.setText(_translate("MainWindow", "Export"))
        self.label_2.setText(_translate("MainWindow", "Load Files"))
        self.button_x_y_file.setText(_translate("MainWindow", "Open X Y File"))
        self.label_4.setText(_translate("MainWindow", "Plots"))
        self.label_mass_file.setText(_translate("MainWindow", "Mass file selected: "))
        self.label_config_file.setText(_translate("MainWindow", "Config file selected: "))
        self.button_mass_file.setText(_translate("MainWindow", "Open Mass File"))
        self.medusa_file_button.setText(_translate("MainWindow", "Open Medusa File"))
        self.label_karlie_mapping.setText(_translate("MainWindow", "Karlie"))
        self.label_eloi_mapping.setText(_translate("MainWindow", "Eloi"))
        self.label_10.setText(_translate("MainWindow", "Select mapping:"))
        self.slider_mapping.setToolTip(_translate("MainWindow", "mapping slider"))
        self.label_medusa_file.setText(_translate("MainWindow", "Medusa file Selected: "))
        self.button_config_file.setText(_translate("MainWindow", "Open Config File"))
        self.button_norm_curr_volt.setText(_translate("MainWindow", "Normalized Current \n"
"vs Voltage"))
        self.button_charge_discharge.setText(_translate("MainWindow", "Charge vs Discharge"))
        self.label_x_y_file.setText(_translate("MainWindow", "X Y file selected: "))
        self.label_13.setText(_translate("MainWindow", "Settings & Options"))
        self.label.setText(_translate("MainWindow", "Cycles"))
        self.lineEdit_cycle.setToolTip(_translate("MainWindow", "Enter cycles separated  by comas"))
        self.lineEdit_cycle.setText(_translate("MainWindow", "1,2"))
        self.lineEdit_cycle.setPlaceholderText(_translate("MainWindow", "Enter cycles"))
        self.checkbox_cycle.setText(_translate("MainWindow", "Select all"))
        self.label_3.setText(_translate("MainWindow", "Filter"))
        self.checkbox_channel.setText(_translate("MainWindow", "Select all"))
        self.label_5.setText(_translate("MainWindow", "Channels"))
        self.lineEdit_channel.setToolTip(_translate("MainWindow", "Enter a Channel from 1 to 64"))
        self.lineEdit_channel.setText(_translate("MainWindow", "1"))
        self.lineEdit_channel.setPlaceholderText(_translate("MainWindow", "Enter a Channel 1-64"))
        self.lineEdit_scale_x_min.setToolTip(_translate("MainWindow", "set x-axis minimum limit"))
        self.lineEdit_scale_x_min.setPlaceholderText(_translate("MainWindow", "min"))
        self.lineEdit_scale_x_max.setToolTip(_translate("MainWindow", "set x-axis maximum limit"))
        self.lineEdit_scale_x_max.setPlaceholderText(_translate("MainWindow", "max"))
        self.label_7.setText(_translate("MainWindow", "x-axis"))
        self.lineEdit_scale_y_min.setToolTip(_translate("MainWindow", "set y-axis minimum limit"))
        self.lineEdit_scale_y_min.setPlaceholderText(_translate("MainWindow", "min"))
        self.lineEdit_scale_y_max.setToolTip(_translate("MainWindow", "set y-axis maximum limit"))
        self.lineEdit_scale_y_max.setPlaceholderText(_translate("MainWindow", "max"))
        self.checkbox_scale_default.setText(_translate("MainWindow", "Use Default Scale"))
        self.label_8.setText(_translate("MainWindow", "y-axis"))
        self.label_6.setText(_translate("MainWindow", "Scale"))
        self.label_11.setText(_translate("MainWindow", "Titles"))
        self.checkbox_x_y_plot_label.setText(_translate("MainWindow", "Show x y Values on Plot"))
        self.checkbox_show_title.setText(_translate("MainWindow", "Show Plot Title"))
        self.label_14.setText(_translate("MainWindow", "Min Voltage"))
        self.label_12.setText(_translate("MainWindow", "Integration"))
        self.checkbox_default_voltage_range.setText(_translate("MainWindow", "Use Default Range"))
        self.label_15.setText(_translate("MainWindow", "Max Voltage"))
        self.label_9.setText(_translate("MainWindow", "Reset"))
        self.button_reset_config.setText(_translate("MainWindow", "Reset Config"))
        self.button_reset_mass.setText(_translate("MainWindow", "Reset Mass"))
        self.menuwhats_here.setTitle(_translate("MainWindow", "Help"))
        self.action_about.setText(_translate("MainWindow", "About application"))
        self.action_github.setText(_translate("MainWindow", "GitHub"))


