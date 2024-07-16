# This Python file uses the following encoding: utf-8
# Ciaran Barron 16.06.24

import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because I have the motor control script in a different folder.
sys.path.insert(1, '../Backend')
import LithoMotors as LM

# Create Motors object, interact via with statement which opens and closes connection.
Motors = LM.Motors()

class MotorControllerQt(QWidget):
    '''Class for connecting the motors to the UI'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)

        # set values of spin boxes.
        self._move_strength = 1 # number of steps no distances.
        self._t = 0

        # Click actions
        self.ui.DO_IT.clicked.connect(self.doit_method)
        self.ui.HOME.clicked.connect(self.home)
        self.ui.LOAD_ROUTE.clicked.connect(self.load)
        self.ui.UP.clicked.connect(self.move_up)
        self.ui.DOWN.clicked.connect(self.move_down)
        self.ui.LEFT.clicked.connect(self.move_left)
        self.ui.RIGHT.clicked.connect(self.move_right)

    def doit_method(self):
        """
        Will use the move_left/right/up/down methods but also reference
        the values in the motor pos and current and target boxes.
        """
        print('test')
        return

    def home(self):
        """Home the Motors. This should happen automatically in the arduino code at startup. Testing only."""
        with Motors:
            Motors.move(0,0)
        return

    def load(self):
        return

    def move_left(self):
        # Go and grab the number on the distance setting box and send move that amount command to motors.
        return

    def move_right(self):
        return

    def move_up(self):
        return

    def move_down(self):
        return

    def load_map(self):
        # Go and grab the name of the shape and load the pre-made file of positions.
        # Maybe auto generate
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MotorControllerQt()
    widget.show()

    sys.exit(app.exec())

