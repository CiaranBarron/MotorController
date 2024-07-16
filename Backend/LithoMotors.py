# Ciaran Barron 16.07.24

import SerialDeviceBase
import numpy as np

"""
:TO DO:
- Finish read output / clear output function
- setup the UI side of things
- setup the serial comms identification to auto find board controlling the motor on the computer.
- 
"""


class Motors(SerialDeviceBase.SerialDevice):
    """ Control motors moving stage on LMA310 lithography set up"""

    def __init__(self):
        """The init should also home the motors. Then they should be kept on for the remainder of the use time."""
        super().__init__()

        self._baudrate = 115200
        # self._description - naming of the device (arduino nano every)

        # A and B positions. The motors will home when switched on. 
        self._Apos = 0
        self._Bpos = 0

        # :NOTE: These need to be set in the lab.
        self._stageAmax = 10000
        self._stageBmax = 10000

    def __enter__(self):
        """Enter function for context manager"""
        print("Connecting to Motors...")
        # super().__enter__()
        print("Connected.")

    def __exit__(self):
        """Exit function for context manager. """    
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

    def verify_positions(self, A, B):
        """Make sure that the values of A and B are within movement limits for the stage. """

        # check steps >= minimum
        if A < 0:
            A = 0
        if B < 0:
            B = 0

        # check steps <= maximum
        if A > self._stageAmax:
            A = self._stageAmax
        if B > self._stageBmax:
            B = self._stageBmax
        
        return A, B
    
    def format_msg(self, A, B):
        """Take A and B positions (in motor steps) and format for the arduino"""
        A, B = self.verify_positions(A, B)
        print("{\"stepsA\": " + str(A) + ", \"stepsB\": " + str(B) + "}")
        return "{\"stepsA\": {0}, \"stepsB\": {1}}".format(A,B)

    def update_positions(self, A, B):
        "update the positions of A and B"
        A, B = self.verify_positions(A, B)

        self._Apos = A
        self._Bpos = B

    def read_output(self):
        """clear output buffer from the arduino """
        # read_until -> check for enotyt string or timeout -> continue.
        return None

    def move(self, A, B):
        """Take absolute positions to move the device to. (steps of motor)"""
        self.send(self.format_msg(A, B))
        self.update_positions(A, B)
        self.read_output()

    def move_rel(self, A, B, dirA='left', dirB='up'):
        """Move the motors by a relative amount. (steps of motor)
        :inputs: 
        self
        A, B - number of steps to move
        dirA, dirB - Which direction to move.
        
        :NOTE: Need to find out if left/right up/down is on A or B and is + or -
        
        return None
        """
        if dirA == 'left':
            newA = self._Apos + A
        else: 
            newA = self._Apos - A
        
        if dirB == 'up':
            newB = self._Bpos + B
        else: 
            newB = self._Bpos - B

        self.send(self.format_msg(newA, newB))
        self.update_positions(newA, newB)
        self.read_output()
