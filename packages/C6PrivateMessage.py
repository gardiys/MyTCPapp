from packages.Package import Package


class C6PrivateMessage(Package):
    """Package for private messages"""

    id = 6

    recipient_user_id = None
    message = None

    def read_stream(self):
        self.recipient_user_id = self.stream.read_uint32()
        self.message = self.stream.read_string_unicode()

    def write_stream(self):
        raise NotImplementedError