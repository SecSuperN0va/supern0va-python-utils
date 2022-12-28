import io
import struct

LITTLE_ENDIAN = 'little'
BIG_ENDIAN = 'big'
DEFAULT_ENDIAN = LITTLE_ENDIAN


class Stream(io.BytesIO):

    def __init__(self, *args, **kwargs):
        super(Stream, self).__init__(*args, **kwargs)
        self.endian = kwargs.pop('endian', DEFAULT_ENDIAN)

    @property
    def __endian_sign(self):
        return '<' if self.endian == LITTLE_ENDIAN else '>'

    def set_endianness(self, endianness):
        assert endianness in [BIG_ENDIAN, LITTLE_ENDIAN], f'invalid endianness: {endianness}'
        self.endian = endianness

    def read_byte(self, signed=False):
        return struct.unpack(f'{self.__endian_sign}{"b" if signed else "B"}', self.read(1))[0]

    def write_byte(self, value, signed=False):
        return self.write(struct.pack(f'{self.__endian_sign}{"b" if signed else "B"}', value))

    def read_word(self, signed=False):
        return struct.unpack(f'{self.__endian_sign}{"h" if signed else "H"}', self.read(2))[0]

    def write_word(self, value, signed=False):
        return self.write(struct.pack(f'{self.__endian_sign}{"h" if signed else "H"}', value))

    def read_dword(self, signed=False):
        return struct.unpack(f'{self.__endian_sign}{"l" if signed else "L"}', self.read(4))[0]

    def write_dword(self, value, signed=False):
        return self.write(struct.pack(f'{self.__endian_sign}{"l" if signed else "L"}', value))

    def read_qword(self, signed=False):
        return struct.unpack(f'{self.__endian_sign}{"q" if signed else "Q"}', self.read(8))[0]

    def write_qword(self, value, signed=False):
        return self.write(struct.pack(f'{self.__endian_sign}{"q" if signed else "Q"}', value))

    def read_float32(self):
        return struct.unpack(f'{self.__endian_sign}f', self.read(4))[0]

    def write_float32(self, value):
        return self.write(struct.pack(f'{self.__endian_sign}f', value))

    def read_float64(self):
        return struct.unpack(f'{self.__endian_sign}d', self.read(8))[0]

    def write_float64(self, value):
        return self.write(struct.pack(f'{self.__endian_sign}d', value))

    def read_pascal_string(self, encoding='latin1'):
        l = self.read_byte()
        s = self.read(l)
        if encoding is not None:
            try:
                s = s.decode(encoding)
            except Exception as e:
                s = None
        return s
