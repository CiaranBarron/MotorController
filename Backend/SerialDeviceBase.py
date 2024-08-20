import time
import serial

from serial.tools import list_ports 

class SerialDevice:
    '''
    Base Class for serial devices defining a context manager enter and exit which enables open/close with usage of comm port. 
    '''

    def __init__(self, port='COM1', baud_rate=9600):
        self._port     = port
        self._baudrate = baud_rate
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

    def __enter__(self, **kwargs):
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

    @staticmethod
    def connected_com_devices():
        """Loop over all connected devices and list out what information they have"""
        for d in list_ports.comports():
            print(d.__dict__)

    @staticmethod
    def find_device_comport(attr, attr_value):
        """find the comport the motors are connected to """
        for d in list_ports.comports():
            if hasattr(d, attr):
                if getattr(d, attr) == attr_value:
                    print(f"found device: {attr_value} at port {d.device}")
                    return d.device
            else:
                print(f"Device {d} had no attribute {attr}.")

if __name__ == "__main__":

    SD = SerialDevice(port='COM5', baud_rate=115200)

    device_port = SerialDevice.find_device_comport("serial_number", "FE9AF43E51514746324B2020FF0C3822")
    print(device_port)

