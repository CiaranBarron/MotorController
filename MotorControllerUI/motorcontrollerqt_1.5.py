# This Python file uses the following encoding: utf-8
# Ciaran Barron 31.01.25

import sys

from PySide6.QtWidgets import QApplication, QWidget

from ui_form_1p5 import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because I have the motor control script in a different folder.
sys.path.insert(1, '../Backend')

# ignore this error. The path insert solves it.
from Backend.Electronic_Modules.Koco_Linear_Actuator.linearmotor_comms import LinearMotor
from Backend.LithographyController import LEDController

# Basic stylesheet structure
stylesheet = """
    /* Widget name */
    QWidget {
        background-color: #ffffff;
        color: #000000;
    }
"""

y_id = 842400280    # Motor id for y motion
x_id = 842400780    # Motor id for x motion
s_id = "FT7AX5XQA"  # Serial number for motor controller board.

# Init LEDs Object.
LEDs = LEDController()

class MotorControllerQt(QWidget):
    """Class for connecting the motors to the UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)

        self.setStyleSheet(stylesheet)

        # set values of spin boxes.
        self._move_strength = 10  # um - (default) named this badly. Back when it was steps.
        self._uv_current = 10  # uv current (in spinbox, to be set)
        self._red_current = 10  # red current  (in spinbox, to be set)
        self._exposure_time = 10  # the setting in the spinbox (to be sent)

        # Click actions
        # self.ui.DO_IT.clicked.connect(self.doit_method)
        self.ui.HOME.clicked.connect(self.home)
        self.ui.EXPOSE.clicked.connect(self.expose)
        self.ui.SET_LED_CURRENTS.clicked.connect(self.set_LED_currents)
        self.ui.HOME_CONOR.clicked.connect(self.home_conor)
        self.ui.UP.clicked.connect(lambda: self._move_rel_dir('up'))
        self.ui.DOWN.clicked.connect(lambda: self._move_rel_dir('down'))
        self.ui.LEFT.clicked.connect(lambda: self._move_rel_dir('left'))
        self.ui.RIGHT.clicked.connect(lambda: self._move_rel_dir('right'))
        self.ui.MOVE_MOTORS_ARROW_SETTING.setValue(self._move_strength)  # set default value in spin box.
        self.ui.MOVE_MOTORS_ARROW_SETTING.valueChanged.connect(self.update_move_strength)  # does this change it?
        self.ui.RED_CURRENT_SETTING.valueChanged.connect(self.update_red_current_setting)
        self.ui.UV_CURRENT_SETTING.valueChanged.connect(self.update_uv_current_setting)
        self.ui.EXPOSURE_TIME_SETTING.valueChanged.connect(self.update_exposure_setting)
        self.ui.UV_ON_CHECKBOX.clicked.connect(self.update_uv_light_on)

        # Update on open with current settings.
        self.update_LED_settings_list()
        self.update_previous_expose_time_ui()

    def update_uv_light_on(self):
        """toggle uv light"""
        light_state = -1 if self.ui.UV_ON_CHECKBOX.isChecked() else 0
        LEDs.switchUV(light_state)


    def update_exposure_setting(self):
        """This is the spinbox ui value - the exposure time you want to use. """
        self._exposure_time = self.ui.EXPOSURE_TIME_SETTING.value()
        return None

    def update_red_current_setting(self):
        """This is the spinbox ui value - the current you want to use. """
        self._red_current = self.ui.RED_CURRENT_SETTING.value()
        return None

    def update_uv_current_setting(self):
        """This is the spinbox ui value - the current you want to use. """
        self._uv_current = self.ui.UV_CURRENT_SETTING.value()
        return None

    def expose(self):
        """UV light to turn on for set amount of time. Time pulled from UI."""

        assert self.ui.UV_ON_CHECKBOX.isChecked() == False, "UV already on. Must be off to time exposure"
        # self.ui.UV_ON_CHECKBOX.blockSignals(True)
        self.ui.UV_ON_CHECKBOX.paintEvent(1, force_on=True)
        LEDs.expose(self._exposure_time)
        self.ui.UV_ON_CHECKBOX.paintEvent(1, force_off=True)
        # self.ui.UV_ON_CHECKBOX.blockSignals(False)
        self.update_previous_expose_time_ui()
        return None

    def set_LED_currents(self):
        """set the currents on the LEDs (set both each time). """
        LEDs.set_led_currents(self._uv_current, self._red_current)
        self.update_LED_settings_list()
        return None

    def update_LED_settings_list(self):
        """Update the list widget with the LED current settings. These are pulled from the UV controller."""

        self.ui.LED_SETTINGS_BOX.clear()
        self.ui.LED_SETTINGS_BOX.addItem("LED Settings:")

        uv_led_current_setting, red_led_current_setting = LEDs.get_led_currents()

        self.ui.LED_SETTINGS_BOX.addItem(f"UV: \t {uv_led_current_setting} mA")
        self.ui.LED_SETTINGS_BOX.addItem(f"RED:\t {red_led_current_setting} mA")

        # also update the spin boxes on the ui.
        self.ui.UV_CURRENT_SETTING.setValue(int(uv_led_current_setting))
        self.ui.RED_CURRENT_SETTING.setValue(int(red_led_current_setting))

        return None

    def update_previous_expose_time_ui(self):
        """Ask the UV controller for the stored value for last exposure time. Set it on the UI."""
        self.ui.PREVIOUS_EXPOSURE_TIME_.setText(f"Last exposure time: {LEDs.get_last_exposure_time()} s")
        return None

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

        self.update_list_widget_with_position()

    def update_list_widget_with_position(self):

        self.ui.listWidget.clear()

        with LinearMotor(serial_number=s_id) as lm:
            x_pos = lm.steps2micron(lm.get_position(x_id))
            y_pos = lm.steps2micron(lm.get_position(y_id))

        self.ui.listWidget.addItem("Motor Positions")
        self.ui.listWidget.addItem(f"X: {round(x_pos,1)}")
        self.ui.listWidget.addItem(f"Y: {round(y_pos,1)}")

    def home_conor(self):
        """
        Set home position that is slide specific.
        """
        # move there first then check position set here.
        home_x = 10500
        home_y = 12400

        with LinearMotor(serial_number = s_id) as lm:
            lm.move_absolute(x_id, home_x)
            lm.move_absolute(y_id, home_y)

        print(f"Motors set to: {home_x},{home_y}")
        self.update_list_widget_with_position()
    def _move_rel_dir(self, _dir):

        with LinearMotor(serial_number=s_id) as lm:
            match _dir:
                case 'left':
                    lm.move_relative(x_id, 1 * self._move_strength)
                case 'right':
                    lm.move_relative(x_id, -1 * self._move_strength)
                case 'up':
                    lm.move_relative(y_id, -1 * self._move_strength)
                case 'down':
                    lm.move_relative(y_id, 1 * self._move_strength)

        self.update_list_widget_with_position()

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


        self.update_list_widget_with_position()

        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MotorControllerQt()
    widget.show()

    sys.exit(app.exec())

