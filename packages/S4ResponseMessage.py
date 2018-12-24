from packages.Package import Package
from DataStream import DataStream


class ResponseMessage(Package):
    """Translating exceptions class"""
    id = 4

    response = None

    def __init__(self, stream, status, message):
        super().__init__(stream)
        self.status = status
        self.message = message

    def read_stream(self):
        raise NotImplementedError

    def write_stream(self):
        self.stream.write_byte(self.status)
        self.stream.write_string_unicode(bytes(self.message, encoding='utf-8'))
        self.response = self.stream.send()
