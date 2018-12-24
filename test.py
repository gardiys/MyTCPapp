import unittest
import struct
from DataStream import DataStream


class TestDataStreamClass(unittest.TestCase):

    def test_read_int16(self):
        data = struct.pack('>h', 56)
        stream = DataStream(data)
        self.assertEqual(56, stream.read_int16())

    def test_read_int16_and_int32(self):
        data = struct.pack('>hi', 32_000, 2_140_000_000)
        stream = DataStream(data)
        self.assertEqual(32_000, stream.read_int16())
        self.assertEqual(2_140_000_000, stream.read_int32())


if __name__ == '__main__':
    unittest.main()
