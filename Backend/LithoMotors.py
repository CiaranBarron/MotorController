# Ciaran Barron 16.07.24

import SerialDeviceBase
import os
"""
:TO DO:
- Finish read output / clear output function
- setup the UI side of things
- 
"""
stageAmax = 5000
stageBmax = 3000

class Motors(SerialDeviceBase.SerialDevice):
    """ Control motors moving stage on LMA310 lithography set up"""

    def __init__(self):
        """The init should also home the motors. Then they should be kept on for the remainder of the use time."""
        super().__init__()

        self._arduino_serial_number = "FE9AF43E51514746324B2020FF0C3822"
        self._port = SerialDeviceBase.SerialDevice.find_device_comport(
            "serial_number",
            self._arduino_serial_number
        )
        self._baudrate = 115200

    def __enter__(self):
        """Enter function for context manager"""
        print("Connecting to Motors...")

        ui_rel_file_path = "/../Backend/MotorPositions.bin"
        cwd = os.getcwd()
        with open(cwd + ui_rel_file_path, 'rb') as f:
        # with open("MotorPositions.bin", 'rb') as f:
            pos = f.readline()

        a, b = pos.decode().split(" ")
        self._Apos, self._Bpos = int(a), int(b)

        super().__enter__()
        print("Connected.")

        self.readline(display=False) # clear messages from arduino

        self.set_motor_positions()

    def __exit__(self, *args):
        """ Exit function for context manager. Update file with Motor Positions. """
        ui_rel_file_path = "/../Backend/MotorPositions.bin"
        cwd = os.getcwd()
        with open(cwd + ui_rel_file_path, 'wb') as f:
        # with open("MotorPositions.bin", 'wb') as f:
            f.write(bytes(f"{self._Apos} {self._Bpos}", "utf-8"))

        super().__exit__()
        print("Motors disconnected.")

    def send(self, message, display=True):
        # writing message to the serial device. printing sent messages to console.
        try:
            self.conn.write(bytes(message + "\n", 'UTF-8'))
            if display:
                print("sent\t\t->\t" + message)
        except Exception as e:
            print(repr(e))

    def readline(self, display=True, terminator=""):
        # read_until -> check for enotyt string or timeout -> continue.
        message = False
        while message != terminator:
            message = self.conn.read_until().decode()
            if display:
                print(f"received\t<-\t{message}")
        return message

    def verify_positions(self, A: int, B: int):
        """Make sure that the values of A and B are within movement limits for the stage. """
        assert 0 <= A <= stageAmax, f"Check 0 <= A < Max. Current: {self._Apos, self._Bpos}"
        assert 0 <= B <= stageBmax, f"Check 0 <= B < Max. Current: {self._Apos, self._Bpos}"
        # fix this later
        return A, B
    
    def format_json(self, A: int, B: int, home=0):
        """Take A and B positions (in motor steps) and format for the arduino"""
        self.verify_positions(A, B)
        return "{\"stepsA\":"+str(A)+",\"stepsB\":"+str(B)+ ",\"Home\":"+str(home)+"}"

    def set_motor_positions(self):
        a, b = str(self._Apos), str(self._Bpos)
        update_string = f"\"currentApos\":{a}, \"currentBpos\":{b}"
        update_message = "{" + f"\"stepsA\":{a}," + f"\"stepsB\":{b}, \"Home\":0," + update_string + "}"
        self.send(update_message)

    def update_positions(self, A: int, B: int):
        """update the positions of A and B"""
        self._Apos, self._Bpos = self.verify_positions(A, B)

    def home(self):
        self.send(self.format_json(self._Apos, self._Bpos, home=1))
        self._Apos = 0
        self._Bpos = 0

        print("Homing...", end='')
        message = "False"
        while not "Done" in message:
            message = self.conn.read_until().decode()
        print("Done")


    def move(self, A, B):
        """Take absolute positions to move the device to. (steps of motor)"""
        self.send(self.format_json(A, B))
        self.update_positions(A, B)
        self.readline()

    def move_rel(self, A, B, dirA='left', dirB='up'):
        """Move motors by amount relative to current position."""
        offsetA = -A if dirA == 'left' else A
        offsetB = B if dirB == 'up' else -B
        self.move(self._Apos + offsetA, self._Bpos + offsetB)
        print(f"Current steps: A: {self._Apos} B: {self._Bpos}")


if __name__ == "__main__":
    """Test that Motors behave as expected. Move to a middle position and perform scan action."""
    M = Motors()
    with M:
        M.readline()
        # M.move(2000, 2000)

        M.home()

        M.set_motor_positions()

        print(M._Apos)

        M.move(800,800)
    # M.format_msg(10000000,0)