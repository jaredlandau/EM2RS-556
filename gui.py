import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from mainwindow import Ui_MainWindow


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self, motor):
        super(UserInterface, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set window title
        self.setWindowTitle("MOT-186 Control Software")

        # Define motor object
        self.motor = motor

        # Values
        self.direction = "CLOCKWISE"
        self.speed = 60
        self.interval = 100
        self.steps = 1

        # Signals
        self.ui.clockwiseRadioButton.toggled.connect(self.clockwise_radio_toggled)
        self.ui.counterclockwiseRadioButton.toggled.connect(self.counterclockwise_radio_toggled)

        self.ui.speedSpinBox.valueChanged.connect(self.speed_value_changed)
        self.ui.intervalSpinBox.valueChanged.connect(self.interval_value_changed)
        self.ui.stepsSpinBox.valueChanged.connect(self.steps_value_changed)

        self.ui.startButton.clicked.connect(self.start_button_clicked)
        self.ui.stopButton.clicked.connect(self.stop_button_clicked)

    def clockwise_radio_toggled(self, checked):
        if checked:
            self.direction = "CLOCKWISE"

    def counterclockwise_radio_toggled(self, checked):
        if checked:
            self.direction = "COUNTERCLOCKWISE"

    def speed_value_changed(self, value):
        self.speed = value

    def interval_value_changed(self, value):
        self.interval = value

    def steps_value_changed(self, value):
        self.steps = value

    def start_button_clicked(self):
        self.motor.start_thread(self.direction, self.steps, self.speed)

    def stop_button_clicked(self):
        self.motor.stop()
