# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog_MotorController

class MotorControllerQt(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)
        self.ui.DO_IT.clicked.connect(self.doit_method)


    def doit_method(self):
        """
        Will use the move_left/right/up/down methods but also reference
        the values in the motor pos and current and target boxes.
        """
        print('test')
        return

    def home(self):
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

