import struct

from main.utils.stream import Stream


OP_TYPE_BASE = -1
OP_TYPE_BYTE = 0
OP_TYPE_WORD = 1
OP_TYPE_DWORD = 2
OP_TYPE_QWORD = 3
OP_TYPE_TOKEN = 4
OP_TYPE_TYPE = 5
OP_TYPE_SWITCH = 6
OP_TYPE_SBYTE = 7
OP_TYPE_SWORD = 8
OP_TYPE_SDWORD = 9
OP_TYPE_SQWORD = 10
OP_TYPE_FLOAT32 = 11
OP_TYPE_FLOAT64 = 12


class BaseOperand(object):
    __TYPE__ = OP_TYPE_BASE

    def __init__(self, stream):
        assert issubclass(type(stream).__class__, Stream.__class__), 'required `stream` to be instance of `Stream`'
        self.value = None
        self.load(stream)

    @property
    def type(self):
        return self.__TYPE__

    @property
    def string(self):
        return str(self.value)

    def load(self, stream):
        pass

    def save(self, stream):
        raise NotImplementedError

    def __repr__(self):
        return self.string


class ByteOperand(BaseOperand):
    __TYPE__ = OP_TYPE_BYTE

    def load(self, stream):
        self.value = stream.read_byte()

    def save(self, stream):
        stream.write_byte(self.value)

    @property
    def string(self):
        return f'0x{self.value:02x}'


class SignedByteOperand(BaseOperand):
    __TYPE__ = OP_TYPE_SBYTE

    def load(self, stream):
        self.value = stream.read_byte(signed=True)

    @property
    def string(self):
        return f'0x{self.value & 0xFF:02x}'

    def save(self, stream):
        stream.write_byte(self.value, signed=True)


class WordOperand(BaseOperand):
    __TYPE__ = OP_TYPE_WORD

    def load(self, stream):
        self.value = stream.read_word()

    @property
    def string(self):
        return f'0x{self.value:04x}'

    def save(self, stream):
        stream.write_word(self.value)


class SignedWordOperand(BaseOperand):
    __TYPE__ = OP_TYPE_SWORD

    def load(self, stream):
        self.value = stream.read_word(signed=True)

    @property
    def string(self):
        return f'0x{self.value & 0xFFFF:04x}'

    def save(self, stream):
        stream.write_word(self.value, signed=True)


class DwordOperand(BaseOperand):
    __TYPE__ = OP_TYPE_DWORD

    def load(self, stream):
        self.value = stream.read_dword()

    @property
    def string(self):
        return f'0x{self.value:08x}'

    def save(self, stream):
        stream.write_dword(self.value)


class SignedDwordOperand(BaseOperand):
    __TYPE__ = OP_TYPE_SDWORD

    def load(self, stream):
        self.value = stream.read_dword(signed=True)

    @property
    def string(self):
        return f'0x{self.value & 0xFFFFFFFF:08x}'

    def save(self, stream):
        stream.write_dword(self.value, signed=True)


class Float32Operand(BaseOperand):
    __TYPE__ = OP_TYPE_FLOAT32

    def load(self, stream):
        self.value = stream.read_float32()

    @property
    def string(self):
        return f'{self.value:f}'

    def save(self, stream):
        stream.write_float32(self.value)


class QwordOperand(BaseOperand):
    __TYPE__ = OP_TYPE_QWORD

    def load(self, stream):
        self.value = stream.read_qword()

    @property
    def string(self):
        return f'0x{self.value:016x}'

    def save(self, stream):
        stream.write_qword(self.value)


class SignedQwordOperand(BaseOperand):
    __TYPE__ = OP_TYPE_SQWORD

    def load(self, stream):
        self.value = stream.read_qword(signed=True)

    @property
    def string(self):
        return f'0x{self.value & 0xFFFFFFFFFFFFFFFF:016x}'

    def save(self, stream):
        stream.write_qword(self.value, signed=True)


class Float64Operand(BaseOperand):
    __TYPE__ = OP_TYPE_FLOAT64

    def load(self, stream):
        self.value = stream.read_float64()

    @property
    def string(self):
        return f'{self.value:f}'

    def save(self, stream):
        stream.write_float64(self.value)


class TokenOperand(DwordOperand):
    __TYPE__ = OP_TYPE_TOKEN

    @property
    def string(self):
        return f'Token<{super(TokenOperand, self).string}>'


class TypeOperand(DwordOperand):
    __TYPE__ = OP_TYPE_TYPE

    @property
    def string(self):
        return f'Token<{super().string}>'


class SwitchOperand(BaseOperand):
    __TYPE__ = OP_TYPE_SWITCH

    def load(self, stream):
        self.n_cases = stream.read_dword()
        self.value = []
        for i in range(self.n_cases):
            self.value.append(stream.read_dword(signed=True))

    def save(self, stream):
        stream.write_dword(self.n_cases)
        for i, v in enumerate(self.value):
            stream.write_dword(v)

    @property
    def string(self):
        return '<' + ' | '.join([f'0x{x:x}' for x in self.value]) + '>'