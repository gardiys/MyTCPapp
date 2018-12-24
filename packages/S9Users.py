from packages.Package import Package

class S9Users(Package):

    id = 9

    def __init__(self, stream, user_list:list):
        super().__init__(stream)
        self.user_list = user_list

    def read_stream(self):
        raise NotImplementedError

    def write_stream(self):
        self.stream.write_uint16(len(self.user_list)) # количество пользователей
        for user in self.user_list:
            #TODO
