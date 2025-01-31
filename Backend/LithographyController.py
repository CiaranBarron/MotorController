# This Python file uses the following encoding: utf-8
# Ciaran Barron 31.01.25
import time

from serial import Serial
from serial.tools import list_ports


class LEDController:
    """
    Class for communications and control of the LEDs in the UV lithography setup.

    =========== Controller Firmware Command Summary ==========
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
    """
    def __init__(self, board_description='SparkFun Pro Micro'):

        # Variables for description of controller board and the port the LED controller is connected to.
        self._board_description = board_description
        self._serial_number = "5&10DC9A0C&0&4"
        self._port = False

        # These are the values for the LED currents that the LEDS are set to. SET to Ciaran's Default.
        self._red_current = 30
        self._uv_current = 400

        # the time of the last exposure.
        self._last_exposure = 0

        # On init find the port the board is connected to.
        self._port = self.find_leds_port()

    def _cam_set(self, on=True):
        with Serial(self._port, baudrate=9600, timeout=1) as ser:
            ser.write(f"<CAM_SET, {1 if on else 0}>\n".encode())

    def find_leds_port(self):
        """Use the description of the SparkFun Pro Micro controller to find corresponding serial port."""
        ports = list_ports.comports(include_links=True)
        if len(ports) > 0:
            for p in ports:
                if p.description == self._board_description or p.serial_number == self._serial_number:
                    print(f'Litho USB Port: {p.device}')
                    return p.device
        raise Exception("Litho Controller not found. Check it is connected.")

    def show_port(self):
        return self._port

    def set_led_currents(self, uv, red):
        """Write the new current for the LED to the controller. Update local stored value."""
        with Serial(self._port, baudrate=9600, timeout=1) as ser:
            ser.write(f"<UV_I_SET,{uv}>\n".encode())
            ser.write(f"<RED_I_SET,{red}>\n".encode())

    def get_led_currents(self):
        """retrieve the state of the LED (mA setting no whether it is on or off)"""
        with Serial(self._port, baudrate=9600, timeout=1) as ser:

            ser.write(f"<UV_I_GET,0>\n".encode())
            start_time = time.perf_counter()
            while time.perf_counter() - start_time < 1:
                # awaiting response
                if ser.in_waiting > 0:
                    s = ser.readline().decode()
                    self._uv_current = s.split(' ')[-2]
                    break

            ser.write(f"<RED_I_GET,0>\n".encode())
            start_time = time.perf_counter()
            while time.perf_counter() - start_time < 1:
                # awaiting response
                if ser.in_waiting > 0:
                    s = ser.readline().decode()
                    self._red_current = s.split(' ')[-2]
                    break

        return self._uv_current, self._red_current

    def get_last_exposure_time(self):

        with Serial(self._port, baudrate=9600, timeout=1) as ser:
            ser.write(f"<UV_T_GET,0>\n".encode())
            start_time = time.perf_counter()
            while time.perf_counter() - start_time < 1:
                # awaiting response
                if ser.in_waiting > 0:
                    exposure_time = ser.readline().decode().split(' ')[-2]
                    break

        return exposure_time

    def expose(self, t):
        """set the controller to turn on the UV light for a set amount of time."""
        assert t <= 300, "Max exposure time is 5 min"

        # Max exposure time
        timeout = 300
        start = time.perf_counter()
        with Serial(self._port, baudrate=9600, timeout=1) as ser:
            ser.write(f"<UV_T_SET,{t}>\n".encode())

            while time.perf_counter() - start < timeout:
                if ser.in_waiting > 0:
                    ser.readline().decode()
                    break


    def turn_off_leds(self):
        with Serial(self._port, baudrate=9600, timeout=1) as ser:
            ser.write(f"<ALL,0>\n".encode())


if __name__ == '__main__':

    ### test the port and read/write speed ###

    leds = LEDController()

    # switch on the relay for power to the leds.
    leds._cam_set()

    # Test the read time
    st = time.perf_counter()

    uv_i, red_i = leds.get_led_currents()

    print(f"Time to read: {round(1000*(time.perf_counter() - st), 1)} ms")

    # Test the write & read time.
    st2 = time.perf_counter()

    new_uv_i = 13
    new_red_i = 10
    leds.set_led_currents(new_uv_i, new_red_i)

    uv_i2, red_i2 = leds.get_led_currents()

    print(f"Time to write then read: {round(1000 * (time.perf_counter() - st2), 1)} ms")

    # Time to run a 5 second exposure.
    st3 = time.perf_counter()
    leds.expose(5)

    print(f"Time (overhead) to complete 5s expose: {round(1000 * (time.perf_counter() - (5 + st3)), 1)} ms")


    st4 = time.perf_counter()
    leds.get_last_exposure_time()

    print(f"Time to get las exposure time: {round(1000 * (time.perf_counter() - st4), 1)} ms")
    # turn off power to the leds.
    leds._cam_set(on=False)
