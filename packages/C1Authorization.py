from packages.Package import Package


class Authorization(Package):
    """class for Authorization"""
    id = 1
    login = None #string
    password = None #string

    def read_stream(self):
        self.login = self.stream.read_string_unicode()
        self.password = self.stream.read_string_unicode()

    def write_stream(self):
        raise NotImplementedError