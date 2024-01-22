import sys
from PyQt5 import QtWidgets

from driver import Driver
from motor import Motor
from gui import UserInterface
from console import Console

PORT = "COM4"
DEBUG_MODE = False


def main():
    driver = Driver(PORT, DEBUG_MODE)
    motor = Motor(driver)

    app = QtWidgets.QApplication([])
    window = UserInterface(driver, motor)
    window.show()
    sys.exit(app.exec_())

    # To run a command line version of the motor control program, uncomment the line below:
    # Console(motor)


if __name__ == "__main__":
    main()
