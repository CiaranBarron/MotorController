# This Python file uses the following encoding: utf-8
# Ciaran Barron 07.11.24

import sys
import time

from serial import Serial

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form_2 import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because I have the motor control script in a different folder.
sys.path.insert(1, '../Backend')
import LithoMotors as LM

# Create Motors object, interact via with statement which opens and closes connection.
Motors = LM.Motors()

class MotorControllerQt(QWidget):
    """Class for connecting the motors to the UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)

        # set values of spin boxes.
        self._move_strength = 0 # number of steps no distances.
        self._exposure_time = 90
        self._pattern = False

        self._DIR1_step_size = 0
        self._DIR1_no_steps = 0
        self._DIR2_step_size = 0
        self._DIR2_no_steps = 0

        self._t = 0

        # Click actions linked to functions.
        self.ui.DO_IT.clicked.connect(self.doit_method)
        self.ui.HOME.clicked.connect(self.home)
        self.ui.EXPOSE.clicked.connect(self.litho)
        self.ui.HOME_CONOR.clicked.connect(self.home_conor)
        self.ui.UP.clicked.connect(lambda: self._move_rel_dir('up'))
        self.ui.DOWN.clicked.connect(lambda: self._move_rel_dir('down'))
        self.ui.LEFT.clicked.connect(lambda: self._move_rel_dir('left'))
        self.ui.RIGHT.clicked.connect(lambda: self._move_rel_dir('right'))

        # values of spin boxes & updates.
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)  # set default value in spin box.
        self.ui.MOVE_MOTORS_ARROW_SETTING.valueChanged.connect(self.update_move_strength)  # does this change it?
        self.ui.LITHO_TIMER_SECONDS.setValue(90)
        self.ui.LITHO_TIMER_SECONDS.valueChanged.connect(self.update_exposure_time)
        self.ui.LINE_PATTERN_CHECK.stateChanged.connect(self.update_line_checkboxes)
        self.ui.SQUARE_PATTERN_CHECK.stateChanged.connect(self.update_square_checkboxes)
        self.ui.DIR1_STEP_SIZE.valueChanged.connect(self.update_DIR1_step_size)
        self.ui.DIR1_NO_STEPS.valueChanged.connect(self.update_DIR1_no_steps)
        self.ui.DIR2_STEP_SIZE.valueChanged.connect(self.update_DIR2_step_size)
        self.ui.DIR2_NO_STEPS.valueChanged.connect(self.update_DIR2_no_steps)
        # set up checkboxes at the start.
        self.ui.LINE_PATTERN_CHECK.setChecked(1)
        self.ui.DIR2_UP.setDisabled(True)
        self.ui.DIR2_DOWN.setDisabled(True)
        self.ui.DIR2_LEFT.setDisabled(True)
        self.ui.DIR2_RIGHT.setDisabled(True)


    def update_move_strength(self):
        # address this function on the arduino side. Move all checks on position there. NONE IN UI.
        ms = self.ui.MOVE_MOTORS_ARROW_SETTING.value()

        if ms > 1000:
            ms = 1000
        if ms < 0:
            ms = 0
        print(f"Motor move strength: steps - {ms}")
        self._move_strength = ms
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)

        return None

    def update_exposure_time(self):
        # update the exposure time stored in the object.
        exposure_time = self.ui.LITHO_TIMER_SECONDS.value()
        if exposure_time < 0:
            print("No negative exposure times pls")
            exposure_time = 0
        self._exposure_time = exposure_time
        self.ui.LITHO_TIMER_SECONDS.setValue(self._exposure_time)
        return None

    def update_line_checkboxes(self):
        # enable the checkboxes.
        if self.ui.LINE_PATTERN_CHECK.isChecked():
            self.ui.SQUARE_PATTERN_CHECK.setChecked(False)
            self.ui.DIR2_UP.setDisabled(True)
            self.ui.DIR2_DOWN.setDisabled(True)
            self.ui.DIR2_LEFT.setDisabled(True)
            self.ui.DIR2_RIGHT.setDisabled(True)
            self._pattern = "line"

        else:
            self.ui.SQUARE_PATTERN_CHECK.setChecked(True)
            self.ui.DIR2_UP.setEnabled(1)
            self.ui.DIR2_DOWN.setEnabled(1)
            self.ui.DIR2_LEFT.setEnabled(1)
            self.ui.DIR2_RIGHT.setEnabled(1)
            self._pattern = "square"

        return None

    def update_square_checkboxes(self):
        # enable the checkboxes.
        if self.ui.SQUARE_PATTERN_CHECK.isChecked():
            self.ui.LINE_PATTERN_CHECK.setChecked(False)
            self.ui.DIR2_UP.setEnabled(1)
            self.ui.DIR2_DOWN.setEnabled(1)
            self.ui.DIR2_LEFT.setEnabled(1)
            self.ui.DIR2_RIGHT.setEnabled(1)
            self._pattern = "square"

        else:
            self.ui.LINE_PATTERN_CHECK.setChecked(True)
            self.ui.DIR2_UP.setDisabled(1)
            self.ui.DIR2_DOWN.setDisabled(1)
            self.ui.DIR2_LEFT.setDisabled(1)
            self.ui.DIR2_RIGHT.setDisabled(1)
            self._pattern = "line"

        return None

    def update_DIR1_step_size(self):
        step_size = self.ui.DIR1_STEP_SIZE.value()
        if step_size < 0:
            step_size = 0
        self._DIR1_step_size = step_size
        return None

    def update_DIR1_no_steps(self):
        step_size = self.ui.DIR1_NO_STEPS.value()
        if step_size < 0:
            step_size = 0
        self._DIR1_no_steps = step_size
        return None

    def update_DIR2_step_size(self):
        step_size = self.ui.DIR2_STEP_SIZE.value()
        if step_size < 0:
            step_size = 0
        self._DIR2_step_size = step_size
        return None

    def update_DIR2_no_steps(self):
        step_size = self.ui.DIR2_NO_STEPS.value()
        if step_size < 0:
            step_size = 0
        self._DIR2_no_steps = step_size
        return None

    def doit_method(self):
        """
        Will use the move_left/right/up/down methods but also reference
        the values in the motor pos and current and target boxes.
        """
        self.ui.STAGE_FRAME.setWindowTitle(str(self._move_strength))
        return

    def home(self):
        """Home the Motors. This should happen automatically in the arduino code at startup. Testing only."""
        with Motors:
            Motors.home()

    def home_conor(self):
        with Motors:
            Motors.home()
        with Motors:
            Motors.move(3332, 1700)

    def _move(self, stepsA, stepsB):
        with Motors:
            Motors.move(stepsA, stepsB)

    def _move_rel_dir(self, _dir):

        with Motors:
            match _dir:
                case 'left':
                    Motors.move_rel(self._move_strength, 0, dirA='left')
                case 'right':
                    Motors.move_rel(self._move_strength, 0, dirA='right')
                case 'up':
                    Motors.move_rel(0, self._move_strength, dirB='up')
                case 'down':
                    Motors.move_rel(0, self._move_strength, dirB='down')

    def litho(expose_time_seconds = 43):

        with Serial('COM3', baudrate=115200, timeout=0.5) as s:

            s.readline()
            _message = f"<{expose_time_seconds}>".encode()
            s.write(_message)
            msg = s.readline().decode()
            print(msg)

    def load(self, steps = 6, mode='square', flipped_dir=False, _dir='left'):
        ''' Patterns for litho '''

        if mode=='line':
            # move_dir = 'right'
            for _ in range(steps):
                print(f"exposure {_} of {steps}")
                self.litho()
                time.sleep(95)
                if flipped_dir:
                    with Motors:
                        Motors.move_rel(10, 0, dirA=_dir)
                with Motors:
                    Motors.move_rel(24, 0, dirA=_dir)

        elif mode=='square':
            ''' 12 left and up, then twelve right and up etc.. '''
            steps = (12, 3)

            self.litho(expose_time_seconds=43)
            time.sleep(44)
            for i in range(steps[1]):
                for  j in range(steps[0]):
                    with Motors:
                        # if even move right. else left.
                        if i % 2 != 0:
                            Motors.move_rel(24, 0, dirA='right')
                        else:
                            Motors.move_rel(24, 0, dirA='left')
                    self.litho(expose_time_seconds=43)
                    time.sleep(44)
                with Motors:
                    Motors.move_rel(0, 6, dirB='down')


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

