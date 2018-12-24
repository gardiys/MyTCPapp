from packages.Package import Package


class S1Authorization(Package):

    id = 1

    def __init__(self, stream, status_code, message):
        super().__init__(stream)
        self.status_code = status_code
        self.message = message

    def read_stream(self):
        raise NotImplementedError

    def write_stream(self):
        self.stream.write_byte(self.status_code)
        self.stream.write_string_unicode(self.message)

