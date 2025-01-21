# This Python file uses the following encoding: utf-8
# Ciaran Barron 16.06.24

import sys
import time

from serial import Serial

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because I have the motor control script in a different folder.
sys.path.insert(1, '../Backend')

# ignore this error. The path insert solves it.
from Electronic_Modules.Koco_Linear_Actuator.linearmotor_comms import LinearMotor

x_id = 842400280  # Motor id for x
y_id = 842400780  # Motor id for y
s_id = "FT7AX5XQ" # Serial number for motor controller board.

class MotorControllerQt(QWidget):
    """Class for connecting the motors to the UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)

        # set values of spin boxes.
        self._move_strength = 10 # um - (default) named this badly. Back when it was steps.

        # Click actions
        # self.ui.DO_IT.clicked.connect(self.doit_method)
        self.ui.HOME.clicked.connect(self.home)
        self.ui.LOAD_ROUTE.clicked.connect(self.load)
        self.ui.HOME_CONOR.clicked.connect(self.home_conor)
        self.ui.UP.clicked.connect(lambda: self._move_rel_dir('up'))
        self.ui.DOWN.clicked.connect(lambda: self._move_rel_dir('down'))
        self.ui.LEFT.clicked.connect(lambda: self._move_rel_dir('left'))
        self.ui.RIGHT.clicked.connect(lambda: self._move_rel_dir('right'))
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)  # set default value in spin box.
        self.ui.MOVE_MOTORS_ARROW_SETTING.valueChanged.connect(self.update_move_strength)  # does this change it?

    # :REMOVED: do_it method - not used in basic.

    def update_move_strength(self):
        """
        Set the distance to be moved.
        Need to rename to distance from steps in the dialog box.
        """
        ms = self.ui.MOVE_MOTORS_ARROW_SETTING.value()

        if ms > 1000:
            ms = 1000
        if ms < 0:
            ms = 0
        self._move_strength = ms
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)
        return None

    def home(self):
        """
        Home the Motors. Builtin LinearMotor func
        """
        with LinearMotor(serial_number = s_id) as lm:
            lm.home_motor(x_id)
            lm.home_motor(y_id)


    def home_conor(self):
        """
        Set home position that is slide specific.
        """
        # move there first then check position set here.
        home_x = 100
        home_y = 100

        with LinearMotor(serial_number = s_id) as lm:
            lm.move_absolute(x_id, home_x)
            lm.move_absolute(y_id, home_y)

        print(f"Motors set to: {home_x},{home_y}")


    def _move_rel_dir(self, _dir):

        with LinearMotor(serial_number=s_id) as lm:
            match _dir:
                case 'left':
                    lm.move_relative(x_id, self._move_strength)
                case 'right':
                    lm.move_relative(x_id, -1 * self._move_strength)
                case 'up':
                    lm.move_relative(y_id, self._move_strength)
                case 'down':
                    lm.move_relative(y_id, -1 * self._move_strength)

    def _move(self, x, y):
        """
        Move the motors to a specific x,y position
        """
        # need to add some verification of the coords x and y before continuing.
        with LinearMotor(serial_number=s_id) as lm:

            lm.move_absolute(x_id, x)
            lm.move_absolute(y_id, y)

            delta_pos = 74E-3 # define acceptable difference of 10 motor steps (73nm)
            new_x = lm.steps2micron(lm.get_position(x_id))
            new_y = lm.steps2micron(lm.get_position(y_id))

            assert new_x - x > delta_pos, "Error: x position deviated by more than 10 steps"
            assert new_y - y > delta_pos, "Error: y position deviated by more than 10 steps"

            print(f"Motors moved to: {new_x, new_y}")

            return None

    def litho(self, expose_time_seconds = 90):
        """
        Separate to motor control.
        """
        with Serial('COM3', baudrate=115200, timeout=0.5) as s:

            s.readline()
            _message = f"<{expose_time_seconds}>".encode()
            s.write(_message)
            msg = s.readline().decode()
            print(msg)

    def load(self, steps = 6, mode='square', flipped_dir=False, _dir='left'):
        ''' Patterns for litho '''
        #
        # if mode=='line':
        #     # move_dir = 'right'
        #     for _ in range(steps):
        #         print(f"exposure {_} of {steps}")
        #         self.litho()
        #         time.sleep(95)
        #         if flipped_dir:
        #             with Motors:
        #                 Motors.move_rel(10, 0, dirA=_dir)
        #         with Motors:
        #             Motors.move_rel(24, 0, dirA=_dir)
        #
        # elif mode=='square':
        #     ''' 12 left and down, then twelve right and up/down etc.. '''
        #
        #     step_y = int(input("steps y: "))
        #     step_x = int(input("steps x: "))
        #     steps = (step_x, step_y)
        #     exp_time = int(input("expose_time: "))
        #     dir_v = input("direction: ")
        #     self.litho(expose_time_seconds=exp_time)
        #     time.sleep(exp_time+1)
        #     for i in range(steps[1]):
        #         for  j in range(steps[0]):
        #             print(f"time left: {steps[0] * steps[1] * exp_time - (i*exp_time + j*exp_time)}")
        #             with Motors:
        #                 # if even move right. else left.
        #                 # start moving left!
        #                 if i % 2 != 0:
        #                     Motors.move_rel(24, 0, dirA='right')
        #                 else:
        #                     Motors.move_rel(24, 0, dirA='left')
        #             self.litho(expose_time_seconds=exp_time)
        #             time.sleep(exp_time+1)
        #             if (steps[1] == 1) and (j == steps[0] - 1):
        #                 return None
        #         with Motors:
        #
        #             Motors.move_rel(0, 6, dirB=dir_v)
        #
        #
        # return



    def load_map(self):
        # Go and grab the name of the shape and load the pre-made file of positions.
        # Maybe auto generate
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MotorControllerQt()
    widget.show()

    sys.exit(app.exec())

