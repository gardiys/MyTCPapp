from DataStream import DataStream
from myparser import Parser

class Receiver:
    """Class for receiving data"""

    data = b''

    def __init__(self, data):
        self.data += data
        self.stream = DataStream(self.data)
        self.length = self.stream.read_uint16()
        self.parser = Parser()

    def decode(self):
        """Decoding incoming byte-string"""
        if self.length <= self.stream.length():
            """Парсим пакет на составляющие по id"""
            return self.parser.decode(self.stream)
        return
