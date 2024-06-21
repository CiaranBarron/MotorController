import SerialDeviceBase
import numpy as np



class Motors(SerialDeviceBase.SerialDevice):
    """ Control motors moving stage on LMA310 lithography set up"""

    def __init__(self):

        super.__init__()

        self._baudrate = 115200
        self._description

        # A and B positions. The motors will home when switched on. 
        self._Apos = 0
        self._Bpos = 0

        # :NOTE: These need to be set in the lab.
        self._stageAmax = 10000
        self._stageBmax = 10000

    def __enter__(self):
        """Enter function for context manager"""
        print("Connecting to Motors...")
        super().__enter__()
        print("Connected.")

    def __exit__(self):
        """Exit function for context manager. """
        print("Motors disconnected.")
        super().__exit__()

    def verify_positions(self, A,B):
        """Make sure that the values of A and B are within movement limits for the stage. """

        # check minimum
        if A < 0:
            A = 0
        if B < 0:
            B = 0

        # check maximum
        if A > self._stageAmax:
            A = self._stageAmax
        if B > self._stageBmax:
            B = self._stageBmax
        
        return A, B
    
    def format_msg(self, A, B):
        """Take A and B positions (in motor steps) and format for the arduino"""
        A, B = self.verify_positions(A, B)       
        return "{\"stepsA\": {0}, \"stepsB\": {1}\}".format(A,B)

    def update_positions(self, A, B):
        "update the positions of A and B"
        A, B = self.verify_postiions(A, B)

        self._Apos = A
        self._Bpos = B

    def move(self, A, B):
        """Take absolute positions to move the device to. (steps of motor)"""
        self.send(self.format_msg(A, B))
        self.update_positions(A, B)

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

        
            
