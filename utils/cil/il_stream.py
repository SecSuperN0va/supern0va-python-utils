import struct
from main.utils.stream import Stream


class ILStream(Stream):

    class IncompleteOpcodeException(BaseException):
        pass

    def read_opcode(self):
        try:
            b = self.read_byte()
            c = 1
        except:
            raise ILStream.IncompleteOpcodeException('failed to read initial opcode byte')
        if b == 0xFE:
            try:
                b2 = self.read_byte()
                c += 1
            except:
                raise ILStream.IncompleteOpcodeException('failed to read secondary opcode byte')
            b = (b << 8) | b2
        return b, c

    def write_opcode(self, opcode):
        if opcode & 0xFF00:
            return self.write(struct.pack('>H', opcode))
        return self.write(struct.pack('>B', opcode))

    def read_token(self):
        return self.read_dword()

    def read_type(self):
        return self.read_dword()