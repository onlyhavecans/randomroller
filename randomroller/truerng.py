import sys
from serial import Serial
from serial.tools import list_ports


class TrueRNG:
    def __init__(self, com_port=None):
        self._rng_com_port = None
        self.set_port(com_port)
        self._pool = bytearray()

    def __repr__(self):
        return "TrueRNG({})".format(self._rng_com_port)

    def set_port(self, port=None):
        if port:
            self._rng_com_port = port
        else:
            port = self.find_port()
            if port is None:
                raise ValueError("None is not a valid com port. No device found")
            else:
                self._rng_com_port = self.find_port()

    @staticmethod
    def find_port():
        ports_avaiable = list(list_ports.comports())
        for temp in ports_avaiable:
            if temp[1].startswith("TrueRNG"):
                return str(temp[0])  # always chooses the 1st TrueRNG found
        return None

    def get_rng(self, byte_count=102400):
        """
        Return randomess
        :param byte_count: int number of bytes to return
        :return: random data in bytes
        """
        with Serial(port=self._rng_com_port, timeout=10) as serial:
            serial.setDTR(True)
            serial.flushInput()
            data = serial.read(byte_count)
        return data

    def get_int(self, byte_count=64):
        """
        Return a very random int
        :return: int
        """
        return int.from_bytes(self.get_rng(byte_count), byteorder=sys.byteorder, signed=False)

    def choice(self, sequence):
        if not sequence:
            raise IndexError
        num = len(sequence)
        choice = self.get_int() % num
        return sequence[choice]
