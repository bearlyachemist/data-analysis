from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import pyqtSlot
from os import path
from view.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()
        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        ####################################################################
        #   connect widgets to controllers
        ####################################################################
        # open file buttons
        self._ui.pushButton_master.clicked.connect(self.open_file_name_dialog)

        # plot buttons
        self._ui.pushButton_current.clicked.connect(lambda: self.plot("current"))
        self._ui.pushButton_charge.clicked.connect(lambda: self.plot("charge"))

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

    def on_file_name_changed(self, name):
        # label color based on file_name
        # if the file name is empty them it means file is reseted
        name = path.basename(name)
        file_label_color = "green"
        self.on_task_bar_message(file_label_color, "Successfully loaded {} file".format(name))

        # update cycle dropdown
        all_cycles = []
        master_data = self._model.master_data
        cycle_1 = master_data[0][0].Cycle.unique().tolist()
        cycle_2 = master_data[1][0].Cycle.unique().tolist()
        cycle_3 = master_data[2][0].Cycle.unique().tolist()
        all_cycles += cycle_1
        all_cycles += cycle_2
        all_cycles += cycle_3

        cycle_list = list(set(all_cycles))
        sorted(cycle_list)

        # assuming there are always even cycles
        self._ui.comboBox_cycle.clear()
        for index in range(0, len(cycle_list), 2):
            charge = cycle_list[index]
            discharge = cycle_list[index + 1]
            self._ui.comboBox_cycle.addItem("{},{}".format(charge, discharge))

        # update buttons
        self._ui.comboBox_cycle.setEnabled(True)
        self._ui.checkBox_x_y.setEnabled(True)
        self._ui.pushButton_charge.setEnabled(True)
        self._ui.pushButton_current.setEnabled(True)

    def plot(self, plot_name):
        # get cycles
        cycles = self._ui.comboBox_cycle.currentText()
        cycle_list = list(map(int, cycles.split(",")))
        # show title
        show_title = self._ui.checkBox_x_y.isChecked()

        if plot_name == "current":
            self._main_controller.plot_norm_volt_cur(cycle_list, show_title)
        elif plot_name == "charge":
            self._main_controller.plot_charge_voltage(cycle_list, show_title)

    @pyqtSlot(str, str)
    def on_task_bar_message(self, color, message):
        self._ui.statusbar.show()
        self._ui.statusbar.showMessage(message)
        self._ui.statusbar.setStyleSheet('color: {}'.format(color))

    # Set one file
    def open_file_name_dialog(self):
        # self._main_controller.validate_master("master-template.csv")
        # open window to select file
        options = QFileDialog.Options()

        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                   "",
                                                   "All Files (*)", options=options)

        if file_name:
            self._main_controller.validate_master(file_name)
