# This Python file uses the following encoding: utf-8
# Ciaran Barron 29.01.25

import sys
import time

from serial import Serial
from serial.tools import list_ports

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form_1p5 import Ui_Dialog_MotorController

# This line allows the file to see back up one directory because I have the motor control script in a different folder.
sys.path.insert(1, '../Backend')

# ignore this error. The path insert solves it.
from Electronic_Modules.Koco_Linear_Actuator.linearmotor_comms import LinearMotor

y_id = 842400280  # Motor id for y motion
x_id = 842400780  # Motor id for x motion
s_id = "FT7AX5XQA" # Serial number for motor controller board.

def find_litho_port(description='SparkFun Pro Micro'):
    """
    Use the description of the SparkFun Pro Micro controller to find corresponding serial port.
    """
    ports = list_ports.comports(include_links=True)
    if len(ports) > 0:
        for p in ports:
            if p.description == description:
                print(f'Litho USB Port: {p.device}')
                return p.device
    raise Exception("Litho Controller not found. Check it is connected.")

class MotorControllerQt(QWidget):
    """Class for connecting the motors to the UI"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_MotorController()
        self.ui.setupUi(self)

        # set this here or find it every time you want to connect?
        # No one is going to unplug it mid session. Right??? oh no.
        self.litho_port = find_litho_port()

        # set values of spin boxes.
        self._move_strength = 10 # um - (default) named this badly. Back when it was steps.
        self._previous_exposure_time = 0 # record of last exposure time
        self._uv_current = 10 # uv current (in spinbox, to be set)
        self._uv_current_setting = 10 # mA - this is the value currently set
        self._red_current = 10 # red current  (in spinbox, to be set)
        self._red_current_setting = 30 # mA - this is the value currently set.
        self._exposure_time = 0 # the setting in the spinbox (to be sent)

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
        self.ui.UV_ON_CHECKBOX.stateChanged.connect(self.update_uv_light_on())
        # Update on open with current settings.
        self.update_LED_settings_list()
        self.update_previous_expose_time_ui()

    def update_uv_light_on(self):
        if self.ui.UV_ON_CHECKBOX.isChecked():
            self.litho_send("UV_T_SET, -1", read_output=False)
        else:
            self.litho_send("UV_T_SET, 0", read_output=False)

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
        self.litho_send(f"UV_T_SET,{self._exposure_time}", exposure=True)
        self.update_previous_expose_time_ui()
        return None

    def set_LED_currents(self):
        """set the currents on the LEDs (set both each time). """

        self.litho_send(f"UV_I_SET,{self._uv_current}")
        t = time.perf_counter()
        self._uv_current_setting = self.get_uv_current()
        print("time to get uv: ", time.perf_counter() - t)

        t = time.perf_counter()
        self.litho_send(f"RED_I_SET,{self._red_current}")
        self._red_current_setting = self.get_uv_current()
        print("time to set and get red: ",time.perf_counter() - t)

        print("DONE")
        self.update_LED_settings_list()
        return None

    def litho_send(self, message: str, read_output=False, exposure=False):
        """
        Connect to litho controller and send message.
        if read_output is for getter commands.
        if exposure is to switch off the ui while the exposure is happening.

        :PARAMS:
        =========== Command Summary ==========
        <H,_>              : This help file
        <RED_I_SET,VALUE>  : Set RED current to VALUE (mA)
        <RED_I_GET,_>      : Get RED current (mA)
        <UV_I_SET,VALUE>   : Set UV current to VALUE (mA)
        <UV_I_GET,_>       : Get UV current (mA)
        <UV_T_SET,VALUE>   : Set UV On Time to VALUE & turn on for value (secs)
        <UV_T_GET,_>       : Get UV On Time (secs)
        <CAM_SET,0>        : Disable camera
        <CAM_SET,1>        : Enable camera
        <CAM_GET,_>        : Query camera state
        <ALL,0>            : Turn off both RED and UV

        > Example: <RED_I_SET,100> to set RED current to 100mA
        > Example: <UV_I_SET,200> to set UV current to 200mA
        > Example: <CAM,1> to enable camera
        > Example: <ALL,0> to turn off both RED and UV

        Baudrate doesn't matter

        :OUTPUT:
        str: *txt* value *txt* .split(' ')[-2] to access value.
        """

        with Serial(self.litho_port, baudrate=9600, timeout=1) as s:

            s.write(f"<{message}>".encode())
            # time.sleep(0.1)
            if exposure:
                # I should deactivate all UI for this while loop.
                self.setEnabled(False)

                # wait max 5 mins for a finished resopnse.
                read_timeout = 300
                start_time = time.perf_counter()
                while time.perf_counter() - start_time < read_timeout:
                    time.sleep(1)
                    msg = s.readline().decode()
                    if msg == "FIN":
                        self.setEnabled(True)
                        self.update_previous_expose_time_ui()
                        break
                # And reactivate UI here after it has recieved the FIN message.
                self.setEnabled(True)
                print("Exposure timeout reached. Exiting. Light should also switch off. ")

            if read_output:
                start_time = time.perf_counter()
                while time.perf_counter() - start_time < 5:
                    # awaiting response, if not found return error.
                    if s.in_waiting > 0:
                        msg = s.readline().decode()
                        print(msg)
                        return msg
                return "Not data found. ERROR "
            else:
                return None


    def get_last_exposure_time(self):
        """replace with correct getter syntax."""
        t = self.litho_send("UV_T_GET,0", read_output=True)
        return t.split(' ')[-2]

    def get_uv_current(self):
        """replace with correct getter syntax."""
        x = self.litho_send("UV_I_GET,0", read_output=True)
        return x.split(' ')[-2]

    def get_red_current(self):
        """replace with correct getter syntax."""
        y = self.litho_send("RED_I_GET,0", read_output=True)
        return y.split(' ')[-2]

    def update_LED_settings_list(self):
        """Update the list widget with the LED current settings. These are pulled from the UV controller."""

        self.ui.LED_SETTINGS_BOX.clear()
        self.ui.LED_SETTINGS_BOX.addItem("LED Settings:")

        t = time.perf_counter()

        uv_led_current_setting = self.get_uv_current()
        print("time taken UV:", time.perf_counter() - t)

        t = time.perf_counter()

        red_led_current_setting = self.get_red_current()
        print("time taken RED:", time.perf_counter() - t)

        self.ui.LED_SETTINGS_BOX.addItem(f"UV: \t {uv_led_current_setting} mA")
        self.ui.LED_SETTINGS_BOX.addItem(f"RED:\t {red_led_current_setting} mA")

        return None

    def update_previous_expose_time_ui(self):
        """Ask the UV controller for the stored value for last exposure time. Set it on the UI."""
        _exp_time_string = self.get_last_exposure_time()
        self.ui.PREVIOUS_EXPOSURE_TIME_.setText(f"Last exposure time: {_exp_time_string} s")
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

