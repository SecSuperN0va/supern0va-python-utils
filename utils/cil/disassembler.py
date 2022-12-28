from .il_stream import ILStream
from .instruction import BaseInstruction


class NoInstructionRemainingException(BaseException):
    pass


class CodeBlock(object):

    def __init__(self, code_bytes, base_address=0, decode_token_key=None):
        """
        _instructions contains a list of tuples each containing a relative-address and the instruction instance.
        """
        self._code_bytes = code_bytes
        self._instructions = []
        self._ptr = 0
        self._decode_token_key = decode_token_key
        self.base_address = base_address
        self.load()
        return

    def next_instruction(self):
        if self._ptr >= len(self._instructions):
            raise NoInstructionRemainingException('No instructions remaining')
        ins = self._instructions[self._ptr]
        self._ptr += 1
        return ins

    def load(self):
        self._instructions.clear()
        self._ptr = 0

        assert self._code_bytes, 'cannot load invalid bytes'
        stream = ILStream(self._code_bytes)
        try:
            while True:
                relative_address = stream.tell()
                instruction = BaseInstruction(il_stream=stream, decode_token_key=self._decode_token_key)
                self._instructions.append((relative_address, instruction))
        except ILStream.IncompleteOpcodeException as e:
            pass

    def save(self, stream):
        for _, instruction in self._instructions:
            instruction.save(stream)
