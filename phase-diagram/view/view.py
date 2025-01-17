from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog
from PyQt5.QtCore import pyqtSlot
import numpy as np
from view.main_view_ui import Ui_MainWindow
from view.about_view_ui import Ui_AboutWindow
from view.github_view_ui import Ui_GithubWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui_about = AboutView()
        self._ui_github = GithubView()
        self._ui.setupUi(self)

        ####################################################################
        #   trigger function for UI widgets
        ####################################################################
        self._ui.action_about.triggered.connect(lambda: self._ui_about.show())
        self._ui.action_github.triggered.connect(lambda: self._ui_github.show())

        ####################################################################
        #   connect widgets to controllers
        ####################################################################
        # open file buttons
        self._ui.button_ternary_file.clicked.connect(lambda: self.open_file_name_dialog("ternary"))
        self._ui.button_master_file.clicked.connect(lambda: self.open_file_name_dialog("master"))
        self._ui.button_config_file.clicked.connect(lambda: self.open_file_name_dialog("config"))

        # plot button
        self._ui.button_reset_config.clicked.connect(lambda: self.reset_file("config"))

        # plot button
        self._ui.button_plot.clicked.connect(self.plot_ternary)

        # export button
        self._ui.button_export.clicked.connect(self.export)

        # color scaling
        self._ui.checkbox_default_color.stateChanged.connect(lambda checked: self.enable_color_scale(checked))

        # compare option
        self._ui.checkbox_compare.stateChanged.connect(lambda checked: self.enable_compare(checked))

        # calculation signal
        self._ui.comboBox_type_1.currentIndexChanged.connect(self.perform_calculation)
        self._ui.comboBox_type_2.currentIndexChanged.connect(self.perform_calculation)
        self._ui.comboBox_operation.currentIndexChanged.connect(self.perform_calculation)
        self._ui.checkbox_compare.stateChanged.connect(self.perform_calculation)
        self._ui.checkbox_percentage.stateChanged.connect(self.perform_calculation)

        ####################################################################
        #   listen for model event signals
        ####################################################################
        # file name is updated
        self._model.file_name_changed.connect(self.on_file_name_changed)

        ####################################################################
        #   listen for controller event signals
        ####################################################################
        # status bar  message
        self._main_controller.task_bar_message.connect(self.on_task_bar_message)

    ####################################################################
    #   model listener functions
    ####################################################################
    @pyqtSlot(str)
    def on_file_name_changed(self, file_type):
        file_label_color = "green"
        self.on_task_bar_message({"color": file_label_color, "message": "Successfully loaded {} file".format(file_type)})

        # enable buttons in UI
        if file_type == "master" or file_type == "ternary":
            self._ui.checkbox_default_color.setEnabled(True)
            self._ui.comboBox_type_1.setEnabled(True)
            self._ui.button_plot.setEnabled(True)
            self._ui.checkbox_compare.setEnabled(True)
            self._ui.button_export.setEnabled(True)

            # populate combo box cycles
            column_list = self.get_columns()
            self._ui.comboBox_type_1.clear()
            self._ui.comboBox_type_1.addItems(column_list)
            self._ui.comboBox_type_2.clear()
            self._ui.comboBox_type_2.addItems(column_list)

        elif file_type == "config":
            self._ui.button_reset_config.setEnabled(True)


    ####################################################################
    #   controller listener functions
    ####################################################################
    @pyqtSlot(dict)
    def on_task_bar_message(self, task_bar_data):
        color = task_bar_data['color']
        message = task_bar_data['message']
        self._ui.statusbar.show()
        self._ui.statusbar.showMessage(message)
        self._ui.statusbar.setStyleSheet('color: {}'.format(color))
        if "tooltip" in task_bar_data:
            self._ui.statusbar.setToolTip(task_bar_data["tooltip"])

    ####################################################################
    #   helper functions to send request to controller
    ####################################################################

    def perform_calculation(self):
        selected_type_1 = self._ui.comboBox_type_1.currentText()

        if selected_type_1 == "" or selected_type_1 == "":
            return
        selected_type_2 = None
        selected_operation = None
        is_percentage = None

        if self._ui.checkbox_compare.isChecked():
            selected_type_2 = self._ui.comboBox_type_2.currentText()
            selected_operation = self._ui.comboBox_operation.currentText()
            is_percentage = self._ui.checkbox_percentage.isChecked()

        # perform calculation
        data, _ = self._main_controller.calculate(self._model.ternary_file_data, selected_type_1, selected_type_2,
                              selected_operation, is_percentage)

        # remove the inf and nan
        inf_nan_indexes = data.index[data['calculated'].isin([np.nan, np.inf, -np.inf])].tolist()
        # print("bad indexes:", inf_nan_indexes)
        data = data.drop(inf_nan_indexes)

        # get min and max
        min_color_scale = min(data["calculated"].values)
        max_color_scale = max(data["calculated"].values)

        # set min and max user on UI.
        self._ui.lineEdit_min_color.setText(str(min_color_scale))
        self._ui.lineEdit_max_color.setText(str(max_color_scale))

    def export(self):
        selected_type_1 = self._ui.comboBox_type_1.currentText()
        selected_type_2 = None
        selected_operation = None
        min_color_scale = None
        max_color_scale = None
        is_percentage = None

        if self._ui.checkbox_compare.isChecked():
            selected_type_2 = self._ui.comboBox_type_2.currentText()
            selected_operation = self._ui.comboBox_operation.currentText()
            is_percentage = self._ui.checkbox_percentage.isChecked()

        file_name = self.save_file_dialog()
        if file_name:
            self._main_controller.export(selected_type_1, selected_type_2,
                                       selected_operation, is_percentage, file_name)


    def plot_ternary(self):
        selected_type_1 = self._ui.comboBox_type_1.currentText()
        selected_type_2 = None
        selected_operation = None
        min_color_scale = None
        max_color_scale = None
        is_percentage = None

        if self._ui.checkbox_compare.isChecked():
            selected_type_2 = self._ui.comboBox_type_2.currentText()
            selected_operation = self._ui.comboBox_operation.currentText()
            is_percentage = self._ui.checkbox_percentage.isChecked()

        if not self._ui.checkbox_default_color.isChecked():
            min_color_scale = self._ui.lineEdit_min_color.text()
            max_color_scale = self._ui.lineEdit_max_color.text()

        self._main_controller.plot(selected_type_1, selected_type_2,
                                   selected_operation, min_color_scale, max_color_scale, is_percentage)

    # Set one file
    def open_file_name_dialog(self, file_type):
        # open window to select file
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        if file_type == "config":
            file_name, _ = QFileDialog.getOpenFileName(self, "Select {} file".format(file_type), "",
                                                       "JSON File (*.json);;All Files (*)", options=options)
        else:
            file_name, _ = QFileDialog.getOpenFileName(self,"Select {} file".format(file_type), "",
                                                       "CSV File (*.csv);;All Files (*)", options=options)
        if file_name:
            exclude_channels = self._ui.lineEdit_outlier.text()
            self._main_controller.file_name_changed(file_name, file_type, exclude_channels=exclude_channels)

    ####################################################################
    #   View helper methods
    ####################################################################

    def reset_file(self, file_type):
        data = None
        self._model.add_data(data, file_type)
        if file_type == "config":
            self._ui.button_reset_config.setEnabled(False)
            self.on_task_bar_message({"color": "green", "message": "Successfully removed config file"})

    def get_cycle_list(self):
        data = self._model.ternary_file_data
        columns = data.columns
        # get all the columns names with charge in it
        charges = []
        for column in columns:
            if "charge_" in column:
                charges.append(column)

        # get cycles
        cycles = []
        for charge in charges:
            cycles.append(charge[len("charge_"):])

        return cycles

    def get_columns(self):
        data = self._model.ternary_file_data
        columns = list(data.columns)
        columns.remove("x")
        columns.remove("y")
        columns.remove("channels")
        return columns

    def enable_color_scale(self, checked):
        self._ui.lineEdit_min_color.setEnabled(not checked)
        self._ui.lineEdit_max_color.setEnabled(not checked)

    def enable_compare(self, checked):
        # things to enable or disabled based on the compare checkbox
        self._ui.comboBox_operation.setEnabled(checked)
        self._ui.comboBox_type_2.setEnabled(checked)
        self._ui.checkbox_percentage.setEnabled(checked)

    # save file
    def save_file_dialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save to file", "",
                                                   "CSV File (*.csv) ;; All Files (*)", options=options)
        if file_name:
            return file_name
        else:
            return False

class AboutView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutWindow()
        self.ui.setupUi(self)


class GithubView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_GithubWindow()
        self.ui.setupUi(self)


