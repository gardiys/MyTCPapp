from packages.Package import Package


class MessageC5(Package):

    """Package for simple messages"""

    id = 5

    message = None

    def read_stream(self):
        self.message = self.stream.read_string_unicode()

    def write_stream(self):
        raise NotImplementedError
