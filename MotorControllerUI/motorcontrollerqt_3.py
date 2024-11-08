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
from ui_form_3 import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because
# I have the motor control script in a different folder.
# Not sure if it's legal but it works.
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

        # Options for line and square patterns
        self._DIR1 = False
        self._DIR2 = False
        self._TRIANGLE_DIR = False
        self._DIR1_step_size = 0
        self._DIR1_no_steps = 0
        self._DIR2_step_size = 0
        self._DIR2_no_steps = 0

        # options for triangle pattern
        self._triangle_rows = 0
        self._triangle_start_size = 0
        self._triangle_y_step_size = 0
        self._triangle_x_step_size = 0

        # no idea what this is even for tbh. leaving it here in case it breaks something.
        self._t = 0

        # Click actions linked to functions.
        self.ui.DO_IT.clicked.connect(self.doit_method)
        self.ui.HOME.clicked.connect(self.home)
        self.ui.EXPOSE.clicked.connect(self.expose)
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
        self.ui.TRIANGLE_PATTERN_CHECK.stateChanged.connect(self.update_triangle_checkboxes)

        self.ui.DIR1_STEP_SIZE.valueChanged.connect(self.update_DIR1_step_size)
        self.ui.DIR1_NO_STEPS.valueChanged.connect(self.update_DIR1_no_steps)

        self.ui.DIR2_STEP_SIZE.valueChanged.connect(self.update_DIR2_step_size)
        self.ui.DIR2_NO_STEPS.valueChanged.connect(self.update_DIR2_no_steps)


        self.ui.TRIANGLE_X_STEPS.valueChanged.connect(self.update_triangle_x_steps)
        self.ui.TRIANGLE_Y_STEPS.valueChanged.connect(self.update_triangle_y_steps)
        self.ui.TRIANGLE_ROWS.valueChanged.connect(self.update_triangle_rows)
        self.ui.TRIANGLE_START_SIZE.valueChanged.connect(self.update_triangle_start_size)

        # set up checkboxes at the start.
        self.ui.LINE_PATTERN_CHECK.setChecked(1)
        self.ui.DIR2_UP.setDisabled(True)
        self.ui.DIR2_DOWN.setDisabled(True)
        self.ui.DIR2_LEFT.setDisabled(True)
        self.ui.DIR2_RIGHT.setDisabled(True)
        self.ui.TRIANGLE_UP.setDisabled(True)
        self.ui.TRIANGLE_DOWN.setDisabled(True)

        self.ui.DIR1_UP.stateChanged.connect(self.update_DIR1_up_setting)
        self.ui.DIR1_DOWN.stateChanged.connect(self.update_DIR1_down_setting)
        self.ui.DIR1_LEFT.stateChanged.connect(self.update_DIR1_left_setting)
        self.ui.DIR1_RIGHT.stateChanged.connect(self.update_DIR1_right_setting)

        self.ui.DIR2_UP.stateChanged.connect(self.update_DIR2_up_setting)
        self.ui.DIR2_DOWN.stateChanged.connect(self.update_DIR2_down_setting)
        self.ui.DIR2_LEFT.stateChanged.connect(self.update_DIR2_left_setting)
        self.ui.DIR2_RIGHT.stateChanged.connect(self.update_DIR2_right_setting)

    def update_DIR2_up_setting(self):
        if self.ui.DIR2_UP.isChecked():
            self._DIR2 = "UP"
            self.ui._LABEL_DIR2.setText("Direction 2:   Up")
            self.ui.DIR2_DOWN.setChecked(False)
            self.ui.DIR2_LEFT.setChecked(False)
            self.ui.DIR2_RIGHT.setChecked(False)

        return None

    def update_DIR2_down_setting(self):
        if self.ui.DIR2_DOWN.isChecked():
            self._DIR2 = "DOWN"
            self.ui._LABEL_DIR2.setText("Direction 2:   Down")
            self.ui.DIR2_UP.setChecked(False)
            self.ui.DIR2_LEFT.setChecked(False)
            self.ui.DIR2_RIGHT.setChecked(False)

        return None

    def update_DIR2_left_setting(self):
        if self.ui.DIR2_LEFT.isChecked():
            self._DIR2 = "LEFT"
            self.ui._LABEL_DIR2.setText("Direction 2:   Left")
            self.ui.DIR2_DOWN.setChecked(False)
            self.ui.DIR2_UP.setChecked(False)
            self.ui.DIR2_RIGHT.setChecked(False)

        return None

    def update_DIR2_right_setting(self):
        if self.ui.DIR2_RIGHT.isChecked():
            self._DIR2 = "RIGHT"
            self.ui._LABEL_DIR2.setText("Direction 2:   Right")
            self.ui.DIR2_DOWN.setChecked(False)
            self.ui.DIR2_LEFT.setChecked(False)
            self.ui.DIR2_UP.setChecked(False)

        return None


    def update_DIR1_up_setting(self):
        if self.ui.DIR1_UP.isChecked():
            self._DIR1 = "UP"
            self.ui._LABEL_DIR1.setText("Direction 1:   Up")
            self.ui.DIR1_DOWN.setChecked(False)
            self.ui.DIR1_LEFT.setChecked(False)
            self.ui.DIR1_RIGHT.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_DOWN.isChecked():
                    self.ui.DIR2_DOWN.setChecked(False)
                if self.ui.DIR2_UP.isChecked():
                    self.ui.DIR2_UP.setChecked(False)
                self.ui.DIR2_UP.setDisabled(True)
                self.ui.DIR2_DOWN.setDisabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_DIR1_down_setting(self):
        if self.ui.DIR1_DOWN.isChecked():
            self._DIR1 = "DOWN"
            self.ui._LABEL_DIR1.setText("Direction 1:   Down")
            self.ui.DIR1_UP.setChecked(False)
            self.ui.DIR1_LEFT.setChecked(False)
            self.ui.DIR1_RIGHT.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_DOWN.isChecked():
                    self.ui.DIR2_DOWN.setChecked(False)
                if self.ui.DIR2_UP.isChecked():
                    self.ui.DIR2_UP.setChecked(False)
                self.ui.DIR2_UP.setDisabled(True)
                self.ui.DIR2_DOWN.setDisabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_DIR1_left_setting(self):

        if self.ui.DIR1_LEFT.isChecked():
            self._DIR1 = "LEFT"
            self.ui._LABEL_DIR1.setText("Direction 1:   Left")
            self.ui.DIR1_DOWN.setChecked(False)
            self.ui.DIR1_UP.setChecked(False)
            self.ui.DIR1_RIGHT.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_LEFT.isChecked():
                    self.ui.DIR2_LEFT.setChecked(False)
                if self.ui.DIR2_RIGHT.isChecked():
                    self.ui.DIR2_RIGHT.setChecked(False)
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setDisabled(True)
                self.ui.DIR2_RIGHT.setDisabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None

    def update_DIR1_right_setting(self):

        if self.ui.DIR1_RIGHT.isChecked():
            self._DIR1 = "RIGHT"
            self.ui._LABEL_DIR1.setText("Direction 1:   Right")
            self.ui.DIR1_DOWN.setChecked(False)
            self.ui.DIR1_LEFT.setChecked(False)
            self.ui.DIR1_UP.setChecked(False)

            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                if self.ui.DIR2_LEFT.isChecked():
                    self.ui.DIR2_LEFT.setChecked(False)
                if self.ui.DIR2_RIGHT.isChecked():
                    self.ui.DIR2_RIGHT.setChecked(False)
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setDisabled(True)
                self.ui.DIR2_RIGHT.setDisabled(True)
        else:
            if self.ui.SQUARE_PATTERN_CHECK.isChecked():
                self.ui.DIR2_UP.setEnabled(True)
                self.ui.DIR2_DOWN.setEnabled(True)
                self.ui.DIR2_LEFT.setEnabled(True)
                self.ui.DIR2_RIGHT.setEnabled(True)

        return None
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
            self.ui.TRIANGLE_PATTERN_CHECK.setChecked(False)

            self.ui.DIR1_UP.setEnabled(True)
            self.ui.DIR1_RIGHT.setEnabled(True)
            self.ui.DIR1_LEFT.setEnabled(True)
            self.ui.DIR1_DOWN.setEnabled(True)

            self.ui.DIR2_UP.setDisabled(True)
            self.ui.DIR2_DOWN.setDisabled(True)
            self.ui.DIR2_LEFT.setDisabled(True)
            self.ui.DIR2_RIGHT.setDisabled(True)

            self.ui.TRIANGLE_DOWN.setDisabled(True)
            self.ui.TRIANGLE_UP.setDisabled(True)

            self._pattern = "line"

        return None

    def update_square_checkboxes(self):

        if self.ui.SQUARE_PATTERN_CHECK.isChecked():

            self.ui.LINE_PATTERN_CHECK.setChecked(False)
            self.ui.TRIANGLE_PATTERN_CHECK.setChecked(False)

            self.ui.DIR1_UP.setEnabled(True)
            self.ui.DIR1_RIGHT.setEnabled(True)
            self.ui.DIR1_LEFT.setEnabled(True)
            self.ui.DIR1_DOWN.setEnabled(True)

            self.ui.DIR2_UP.setEnabled(True)
            self.ui.DIR2_DOWN.setEnabled(True)
            self.ui.DIR2_LEFT.setEnabled(True)
            self.ui.DIR2_RIGHT.setEnabled(True)

            self.ui.TRIANGLE_DOWN.setDisabled(True)
            self.ui.TRIANGLE_UP.setDisabled(True)

            self._pattern = "square"

        return None

    def update_triangle_checkboxes(self):

        if self.ui.TRIANGLE_PATTERN_CHECK.isChecked():

            self.ui.LINE_PATTERN_CHECK.setChecked(False)
            self.ui.SQUARE_PATTERN_CHECK.setChecked(False)

            self.ui.DIR1_UP.setDisabled(True)
            self.ui.DIR1_RIGHT.setDisabled(True)
            self.ui.DIR1_LEFT.setDisabled(True)
            self.ui.DIR1_DOWN.setDisabled(True)

            self.ui.DIR2_UP.setDisabled(True)
            self.ui.DIR2_DOWN.setDisabled(True)
            self.ui.DIR2_LEFT.setDisabled(True)
            self.ui.DIR2_RIGHT.setDisabled(True)

            self.ui.TRIANGLE_DOWN.setEnabled(True)
            self.ui.TRIANGLE_UP.setEnabled(True)

            self._pattern = "triangle"

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

    def update_triangle_x_steps(self):
        x_steps = self.ui.TRIANGLE_X_STEPS.value()
        self._triangle_x_step_size = x_steps
        return None

    def update_triangle_y_steps(self):
        y_steps = self.ui.TRIANGLE_Y_STEPS.value()
        self._triangle_y_step_size = y_steps
        return None

    def update_triangle_rows(self):
        self._triangle_rows = self.ui.TRIANGLE_ROWS.value()
        return None

    def update_triangle_start_size(self):
        self._triangle_start_size = self.ui.TRIANGLE_START_SIZE.value()
        return None

    def expose(self):
        # add any checks here before sending message to litho arduino.
        self.litho(expose_time_seconds=self._exposure_time)
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

    def litho(self, expose_time_seconds = 43):

        # taken directly from PCOEdgeGUI-Litho
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

