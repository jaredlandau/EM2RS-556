# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 441, 391))
        self.groupBox.setObjectName("groupBox")
        self.directionGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.directionGroupBox.setGeometry(QtCore.QRect(10, 30, 421, 71))
        self.directionGroupBox.setObjectName("directionGroupBox")
        self.clockwiseRadioButton = QtWidgets.QRadioButton(self.directionGroupBox)
        self.clockwiseRadioButton.setGeometry(QtCore.QRect(60, 30, 110, 24))
        self.clockwiseRadioButton.setChecked(True)
        self.clockwiseRadioButton.setObjectName("clockwiseRadioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.clockwiseRadioButton)
        self.counterclockwiseRadioButton = QtWidgets.QRadioButton(self.directionGroupBox)
        self.counterclockwiseRadioButton.setGeometry(QtCore.QRect(220, 30, 141, 24))
        self.counterclockwiseRadioButton.setObjectName("counterclockwiseRadioButton")
        self.buttonGroup.addButton(self.counterclockwiseRadioButton)
        self.speedGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.speedGroupBox.setGeometry(QtCore.QRect(10, 110, 421, 71))
        self.speedGroupBox.setObjectName("speedGroupBox")
        self.speedHorizontalSlider = QtWidgets.QSlider(self.speedGroupBox)
        self.speedHorizontalSlider.setGeometry(QtCore.QRect(10, 30, 281, 22))
        self.speedHorizontalSlider.setMaximum(5000)
        self.speedHorizontalSlider.setSingleStep(10)
        self.speedHorizontalSlider.setProperty("value", 60)
        self.speedHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedHorizontalSlider.setObjectName("speedHorizontalSlider")
        self.speedSpinBox = QtWidgets.QSpinBox(self.speedGroupBox)
        self.speedSpinBox.setGeometry(QtCore.QRect(301, 30, 61, 26))
        self.speedSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.speedSpinBox.setMaximum(5000)
        self.speedSpinBox.setSingleStep(10)
        self.speedSpinBox.setProperty("value", 60)
        self.speedSpinBox.setObjectName("speedSpinBox")
        self.label = QtWidgets.QLabel(self.speedGroupBox)
        self.label.setGeometry(QtCore.QRect(370, 30, 41, 20))
        self.label.setObjectName("label")
        self.intervalGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.intervalGroupBox.setGeometry(QtCore.QRect(10, 190, 421, 71))
        self.intervalGroupBox.setObjectName("intervalGroupBox")
        self.intervalHorizontalSlider = QtWidgets.QSlider(self.intervalGroupBox)
        self.intervalHorizontalSlider.setGeometry(QtCore.QRect(10, 30, 281, 22))
        self.intervalHorizontalSlider.setMaximum(10000)
        self.intervalHorizontalSlider.setSingleStep(100)
        self.intervalHorizontalSlider.setProperty("value", 100)
        self.intervalHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.intervalHorizontalSlider.setObjectName("intervalHorizontalSlider")
        self.intervalSpinBox = QtWidgets.QSpinBox(self.intervalGroupBox)
        self.intervalSpinBox.setGeometry(QtCore.QRect(301, 30, 81, 26))
        self.intervalSpinBox.setMaximum(10000)
        self.intervalSpinBox.setSingleStep(100)
        self.intervalSpinBox.setProperty("value", 100)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.label_2 = QtWidgets.QLabel(self.intervalGroupBox)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 21, 20))
        self.label_2.setObjectName("label_2")
        self.startButton = QtWidgets.QPushButton(self.groupBox)
        self.startButton.setGeometry(QtCore.QRect(10, 350, 141, 29))
        self.startButton.setObjectName("startButton")
        self.stepsGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.stepsGroupBox.setGeometry(QtCore.QRect(10, 270, 421, 71))
        self.stepsGroupBox.setObjectName("stepsGroupBox")
        self.stepsHorizontalSlider = QtWidgets.QSlider(self.stepsGroupBox)
        self.stepsHorizontalSlider.setGeometry(QtCore.QRect(10, 30, 281, 22))
        self.stepsHorizontalSlider.setMaximum(100)
        self.stepsHorizontalSlider.setSingleStep(1)
        self.stepsHorizontalSlider.setPageStep(1)
        self.stepsHorizontalSlider.setProperty("value", 1)
        self.stepsHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.stepsHorizontalSlider.setObjectName("stepsHorizontalSlider")
        self.stepsSpinBox = QtWidgets.QSpinBox(self.stepsGroupBox)
        self.stepsSpinBox.setGeometry(QtCore.QRect(301, 30, 61, 26))
        self.stepsSpinBox.setMaximum(100)
        self.stepsSpinBox.setSingleStep(1)
        self.stepsSpinBox.setProperty("value", 1)
        self.stepsSpinBox.setDisplayIntegerBase(10)
        self.stepsSpinBox.setObjectName("stepsSpinBox")
        self.label_3 = QtWidgets.QLabel(self.stepsGroupBox)
        self.label_3.setGeometry(QtCore.QRect(370, 30, 41, 20))
        self.label_3.setObjectName("label_3")
        self.stopButton = QtWidgets.QPushButton(self.groupBox)
        self.stopButton.setGeometry(QtCore.QRect(290, 350, 141, 29))
        self.stopButton.setObjectName("stopButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 431, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 26))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuMotor = QtWidgets.QMenu(self.menubar)
        self.menuMotor.setObjectName("menuMotor")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionReconnect = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../GitHub/EM2RS-556/icons/connect.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReconnect.setIcon(icon)
        self.actionReconnect.setObjectName("actionReconnect")
        self.menuConnection.addAction(self.actionReconnect)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuMotor.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.speedHorizontalSlider.valueChanged['int'].connect(self.speedSpinBox.setValue) # type: ignore
        self.speedSpinBox.valueChanged['int'].connect(self.speedHorizontalSlider.setValue) # type: ignore
        self.intervalHorizontalSlider.valueChanged['int'].connect(self.intervalSpinBox.setValue) # type: ignore
        self.intervalSpinBox.valueChanged['int'].connect(self.intervalHorizontalSlider.setValue) # type: ignore
        self.stepsHorizontalSlider.valueChanged['int'].connect(self.stepsSpinBox.setValue) # type: ignore
        self.stepsSpinBox.valueChanged['int'].connect(self.stepsHorizontalSlider.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Motor Controls"))
        self.directionGroupBox.setTitle(_translate("MainWindow", "Direction"))
        self.clockwiseRadioButton.setText(_translate("MainWindow", "Clockwise"))
        self.counterclockwiseRadioButton.setText(_translate("MainWindow", "Counterclockwise"))
        self.speedGroupBox.setTitle(_translate("MainWindow", "Speed"))
        self.label.setText(_translate("MainWindow", "r/min"))
        self.intervalGroupBox.setTitle(_translate("MainWindow", "Interval"))
        self.label_2.setText(_translate("MainWindow", "ms"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stepsGroupBox.setTitle(_translate("MainWindow", "Iterations"))
        self.label_3.setText(_translate("MainWindow", "steps"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status"))
        self.menuConnection.setTitle(_translate("MainWindow", "&Driver"))
        self.menuMotor.setTitle(_translate("MainWindow", "&Motor"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionReconnect.setText(_translate("MainWindow", "Reconnect"))
        self.actionReconnect.setShortcut(_translate("MainWindow", "Ctrl+R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
