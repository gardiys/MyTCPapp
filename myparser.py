import inspect
import sys


class Parser:
    """Class for finding the correct type of incoming data"""

    def __init__(self):
        pass

    def encode(self, response):
        """Translating answer for the socket"""
        return response

    def decode(self, stream):

        id = stream.read_uint16()
        self.packages = {cls(stream).id: cls for name, cls in inspect.getmembers(sys.modules['packages'], inspect.isclass)}
        package = self.packages[id](stream)
        package.read_stream()
        return package


