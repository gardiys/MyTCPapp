import struct


class DataReadException(Exception):
    pass


class DataStream:

    def __init__(self, data=None):
        self.data = data
        self._offset = 0
        self._resp_buffer = b''

    def reset(self):
        self._offset = 0

    def length(self):
        return len(self.data) - 2 # тк длину храним в uint

    def _super_reader(self, byte_len, pattern):
        if self._offset + byte_len > len(self.data):
            raise DataReadException
        response = struct.unpack_from(pattern, self.data, offset=self._offset)
        self._offset += byte_len
        return response[0]

    def read_int16(self):
        byte_len, pattern = 2, '>h'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_uint16(self):
        byte_len, pattern = 2, '>H'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_int32(self):
        byte_len, pattern = 4, '>i'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_uint32(self):
        byte_len, pattern = 4, '>I'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_int64(self):
        byte_len, pattern = 8, '>q'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_uint64(self):
        byte_len, pattern = 8, '>Q'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_string_unicode(self):
        byte_len = self.read_string_length()
        pattern = '>' + str(byte_len) +'s'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_float(self):
        byte_len, pattern = 4, '>f'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_double(self):
        byte_len, pattern = 8, '>d'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_char_unicode(self):
        byte_len, pattern = 1, '>c'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_byte(self):
        byte_len, pattern = 1, '>b'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_ubyte(self):
        byte_len, pattern = 1, '>B'
        response = self._super_reader(byte_len, pattern)
        return response

    def read_string_length(self):
        response = self.read_uint16()
        return response

    def _insert(self, byte_line):
        self._resp_buffer += byte_line

    def write_int16(self, write_data):
        byte_line = struct.pack('>h', write_data)
        self._insert(byte_line)

    def write_uint16(self, write_data):
        byte_line = struct.pack('>H', write_data)
        self._insert(byte_line)

    def write_int32(self, write_data):
        byte_line = struct.pack('>i', write_data)
        self._insert(byte_line)

    def write_uint32(self, write_data):
        byte_line = struct.pack('>I', write_data)
        self._insert(byte_line)

    def write_int64(self, write_data):
        byte_line = struct.pack('>q', write_data)
        self._insert(byte_line)

    def write_uint64(self, write_data):
        byte_line = struct.pack('>Q', write_data)
        self._insert(byte_line)

    def write_string_unicode(self, write_data):
        self.write_string_length(len(write_data))
        byte_line = struct.pack('>'+str(len(write_data))+'s', write_data)
        self._insert(byte_line)

    def write_float(self, write_data):
        byte_line = struct.pack('>f', write_data)
        self._insert(byte_line)

    def write_double(self, write_data):
        byte_line = struct.pack('>d', write_data)
        self._insert(byte_line)

    def write_char_unicode(self, write_data):
        byte_line = struct.pack('>c', write_data)
        self._insert(byte_line)

    def write_byte(self, write_data):
        byte_line = struct.pack('>b', write_data)
        self._insert(byte_line)

    def write_ubyte(self, write_data):
        byte_line = struct.pack('>B', write_data)
        self._insert(byte_line)

    def write_string_length(self, length):
        self.write_uint16(length)

    def send(self):
        byte_line = struct.pack('>h', len(self._resp_buffer))
        return byte_line + self._resp_buffer








