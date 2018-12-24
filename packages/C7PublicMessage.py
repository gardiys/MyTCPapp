from packages.Package import Package


class C7PublicMessage(Package):

    id = 7

    message = None

    def read_stream(self):

        self.message = self.stream.read_string_unicode()

    def write_stream(self):
        raise NotImplementedError
