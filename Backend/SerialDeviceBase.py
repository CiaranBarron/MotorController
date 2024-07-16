import time
import serial

from serial.tools import list_ports 

class SerialDevice:
    '''
    Base Class for serial devices defining a context manager enter and exit which enables open/close with usage of comm port. 
    '''

    def __init__(self):
        self._port     = 'COM1'
        self._baudrate = 9600
        self._bytesize = serial.EIGHTBITS
        self._parity   = serial.PARITY_NONE
        self._stopbits = serial.STOPBITS_ONE
        self._timeout  = 1
        self._xonxoff  = False
        self._rtscts   = False
        self._dsrstr   = False
        self._write_timeout = None
        self._inter_byte_timeout = None
        self.conn = False

    def __enter__(self, *args):
        """run on open in using the with keyword - context management"""
        try:
            self.conn = serial.Serial(
                port     = self._port, 
                baudrate = self._baudrate, 
                bytesize = self._bytesize,
                parity   = self._parity,
                stopbits = self._stopbits,
                timeout  = self._timeout,
                xonxoff  = self._xonxoff, 
                rtscts   = self._rtscts, 
                dsrdtr   = self._dsrstr, 
                write_timeout=None,
                inter_byte_timeout=None,
                exclusive=None
            )
        except Exception as e:
            print(f"Failed to connect to serial device.\n{'='*50}")
            print(repr(e))

    def __exit__(self, *args):

        if self.conn:
            self.conn.close()
        else:
            print("Connection closed.")
            print(self.conn)

    def find_device_comport(self):
        # Given a unique serial_number added to a subclass, find which com port it is on and return it.  
        # loop over serial devices (sd) and check if id matches.
        for sd in list_ports.comports():
                        
            if hasattr(self, 'serial_id'):
                if sd.serial_number == self.serial_id:
                    print(f"Port: {sd.device} -> ID: {self.serial_id}")
                    return sd.device # unique serial_number, for agilent this value is AH01FH4QA
            
            # Avoiding the case where the arduino doesn't have a serial identifier. 
            # Using a portion of the description instead.
            if hasattr(self, 'description_id'):
                if self.description_id in sd.description:
                    print(f"Port: {sd.device} -> ID: {self.description_id}")
                    return sd.device
                
            if hasattr(self, 'description'):
                if self.descrption in sd.description:
                    return sd.device

            else: continue
        
        return False
    
    def func_timer_ms(func):
        def wrap_func(*args, **kwargs):
            start = time.time_ns()
            results = func(*args, **kwargs)
            end = time.time_ns()

            # !r converts to a repr of the preceding statement/function/var
            runtime = round(1e-6*(end-start), 2)
            print(f"Function {func.__name__!r} \t->\t{runtime} ms")
            return results
        return wrap_func