from .operand import *
from .il_stream import ILStream

INSTRUCTION_SET = {
    0x00: ('nop', []),
    0x01: ('break', []),
    0x02: ('ldarg.0', []),
    0x03: ('ldarg.1', []),
    0x04: ('ldarg.2', []),
    0x05: ('ldarg.3', []),
    0x06: ('ldloc.0', []),
    0x07: ('ldloc.1', []),
    0x08: ('ldloc.2', []),
    0x09: ('ldloc.3', []),
    0x0a: ('stloc.0', []),
    0x0b: ('stloc.1', []),
    0x0c: ('stloc.2', []),
    0x0d: ('stloc.3', []),
    0x0e: ('ldarg.s <uint8 (num)>', [ByteOperand]),
    0x0f: ('ldarga.s <uint8 (argNum)>', [ByteOperand]),

    0x10: ('starg.s <uint8 (num)>', [ByteOperand]),
    0x11: ('ldloc.s <uint8 (indx)>', [ByteOperand]),
    0x12: ('ldloca.s <uint8 (indx)>', [ByteOperand]),
    0x13: ('stloc.s <uint8 (indx)>', [ByteOperand]),
    0x14: ('ldnull', []),
    0x15: ('ldc.i4.m1', []),
    0x16: ('ldc.i4.0', []),
    0x17: ('ldc.i4.1', []),
    0x18: ('ldc.i4.2', []),
    0x19: ('ldc.i4.3', []),
    0x1a: ('ldc.i4.4', []),
    0x1b: ('ldc.i4.5', []),
    0x1c: ('ldc.i4.6', []),
    0x1d: ('ldc.i4.7', []),
    0x1e: ('ldc.i4.8', []),
    0x1f: ('ldc.i4.s <int8 (num)>', [SignedByteOperand]),

    0x20: ('ldc.i4 <int32 (num)>', [SignedDwordOperand]),
    0x21: ('ldc.i8 <int64 (num)>', [QwordOperand]),
    0x22: ('ldc.r4 <float32 (num)>', [Float32Operand]),
    0x23: ('ldc.r8 <float64 (num)>', [Float64Operand]),

    0x25: ('dup', []),
    0x26: ('pop', []),
    0x27: ('jmp <method>', [TokenOperand]),
    0x28: ('call <method>', [TokenOperand]),
    0x29: ('calli <callsitedescr>', [TokenOperand]),
    0x2a: ('ret', []),
    0x2b: ('br.s <int8 (target)>', [SignedByteOperand]),
    0x2c: ('brfalse.s <int8 (target)>', [SignedByteOperand]),  # a.k.a. brnull.s brzero.s
    0x2d: ('brtrue.s <int8 (target)>', [SignedByteOperand]),  # a.k.a. brinst.s
    0x2e: ('beq.s <int8 (target)>', [SignedByteOperand]),
    0x2f: ('bge.s <int8 (target)>', [SignedByteOperand]),

    0x30: ('bgt.s <int8 (target)>', [SignedByteOperand]),
    0x31: ('ble.s <int8 (target)>', [SignedByteOperand]),
    0x32: ('blt.s <int8 (target)>', [SignedByteOperand]),
    0x33: ('bne.un.s <int8 (target)>', [SignedByteOperand]),
    0x34: ('bge.un.s <int8 (target)>', [SignedByteOperand]),
    0x35: ('bgt.un.s <int8 (target)>', [SignedByteOperand]),
    0x36: ('ble.un.s <int8 (target)>', [SignedByteOperand]),
    0x37: ('blt.un.s <int8 (target)>', [SignedByteOperand]),
    0x38: ('br <int32 (target)>', [SignedDwordOperand]),
    0x39: ('brfalse <int32 (target)>', [SignedDwordOperand]),  # brnull/brzero
    0x3a: ('brtrue <int32 (target)>', [SignedDwordOperand]),  # brinst
    0x3b: ('beq <int32 (target)>', [DwordOperand]),
    0x3c: ('bge <int32 (target)>', [DwordOperand]),
    0x3d: ('bgt <int32 (target)>', [DwordOperand]),
    0x3e: ('ble <int32 (target)>', [DwordOperand]),
    0x3f: ('blt <int32 (target)>', [DwordOperand]),

    0x40: ('bne.un <int32 (target)>', [DwordOperand]),
    0x41: ('bge.un <int32 (target)>', [DwordOperand]),
    0x42: ('bgt.un <int32 (target)>', [DwordOperand]),
    0x43: ('bl3.un <int32 (target)>', [DwordOperand]),
    0x44: ('blt.un <int32 (target)>', [DwordOperand]),
    0x45: ('switch', [SwitchOperand]),
    0x46: ('ldind.i1', []),
    0x47: ('ldind.u1', []),
    0x48: ('ldind.i2', []),
    0x49: ('ldind.u2', []),
    0x4a: ('ldind.i4', []),
    0x4b: ('ldind.u4', []),
    0x4c: ('ldind.u8', []),  # ldind.i8
    0x4d: ('ldind.i', []),
    0x4e: ('ldind.r4', []),
    0x4f: ('ldind.r8', []),

    0x50: ('ldind.ref', []),
    0x51: ('stind.ref', []),
    0x52: ('stind.i1', []),
    0x53: ('stind.i2', []),
    0x54: ('stind.i4', []),
    0x55: ('stind.i8', []),
    0x56: ('stind.r4', []),
    0x57: ('stind.r8', []),
    0x58: ('add', []),
    0x59: ('sub', []),
    0x5a: ('mul', []),
    0x5b: ('div', []),
    0x5c: ('div.un', []),
    0x5d: ('rem', []),
    0x5e: ('rem.un', []),
    0x5f: ('and', []),

    0x60: ('or', []),
    0x61: ('xor', []),
    0x62: ('shl', []),
    0x63: ('shr', []),
    0x64: ('shr.un', []),
    0x65: ('neg', []),
    0x66: ('not', []),
    0x67: ('conv.i1', []),
    0x68: ('conv.i2', []),
    0x69: ('conv.i4', []),
    0x6a: ('conv.i8', []),
    0x6b: ('conv.r4', []),
    0x6c: ('conv.r8', []),
    0x6d: ('conv.u4', []),
    0x6e: ('conv.u8', []),
    0x6f: ('callvirt <method>', [TokenOperand]),

    0x70: ('cpobj <typeTok>', [TokenOperand]),
    0x71: ('ldobj <typeTok>', [TokenOperand]),
    0x72: ('ldstr <string>', [TokenOperand]),
    0x73: ('newobj <ctor>', [TokenOperand]),
    0x74: ('castclass <class>', [TokenOperand]),
    0x75: ('isinst <class>', [TokenOperand]),
    0x76: ('conv.r.un', []),

    0x79: ('unbox <valuetype>', [TokenOperand]),
    0x7a: ('throw', []),
    0x7b: ('ldfld <field>', [TokenOperand]),
    0x7c: ('ldflda <field>', [TokenOperand]),
    0x7d: ('stfld <field>', [TokenOperand]),
    0x7e: ('ldsfld <field>', [TokenOperand]),
    0x7f: ('ldsflda <field>', [TokenOperand]),

    0x80: ('stsfld <field>', [TokenOperand]),
    0x81: ('stobj <typeTok>', [TokenOperand]),
    0x82: ('conv.ovf.i1.un', []),
    0x83: ('conv.ovf.i2.un', []),
    0x84: ('conv.ovf.i4.un', []),
    0x85: ('conv.ovf.i8.un', []),
    0x86: ('conv.ovf.u1.un', []),
    0x87: ('conv.ovf.u2.un', []),
    0x88: ('conv.ovf.u4.un', []),
    0x89: ('conv.ovf.u8.un', []),
    0x8a: ('conv.ovf.i.un', []),
    0x8b: ('conv.ovf.u.un', []),
    0x8c: ('box <typeTok>', [TokenOperand]),
    0x8d: ('newarr <etype>', [TokenOperand]),
    0x8e: ('ldlen', []),
    0x8f: ('ldelema <class>', [TokenOperand]),

    0x90: ('ldelem.i1', []),
    0x91: ('ldelem.u1', []),
    0x92: ('ldelem.i2', []),
    0x93: ('ldelem.u2', []),
    0x94: ('ldelem.i4', []),
    0x95: ('ldelem.u4', []),
    0x96: ('ldelem.iu8', []),
    0x97: ('ldelem.i', []),
    0x98: ('ldelem.r4', []),
    0x99: ('ldelem.r8', []),
    0x9a: ('ldelem.ref', []),
    0x9b: ('stelem.i', []),
    0x9c: ('stelem.i1', []),
    0x9d: ('stelem.i2', []),
    0x9e: ('stelem.i4', []),
    0x9f: ('stelem.i8', []),

    0xa2: ('stelem.ref', []),
    0xa3: ('ldelem <typeTok>', [TokenOperand]),
    0xa4: ('stelem <typeTok>', [TokenOperand]),

    0xd0: ('ldtoken <token>', [TokenOperand]),
    0xd1: ('conv.u2', []),
    0xd2: ('conv.u1', []),
    0xd3: ('conv.i', []),
    0xd4: ('conv.ovf.i', []),
    0xd5: ('conv.ovf.u', []),
    0xd6: ('add.ovf', []),
    0xd7: ('add.ovf.un', []),
    0xd8: ('mul.ovf', []),
    0xd9: ('mul.ovf.un', []),
    0xda: ('sub.ovf', []),
    0xdb: ('sub.ovf.un', []),
    0xdc: ('endfinally|endfault', []),
    0xdd: ('leave <int32 (target)>', [SignedDwordOperand]),
    0xde: ('leave.s <int8 (target)>', [SignedByteOperand]),
    0xdf: ('stind.i', []),

    0xe0: ('conv.u', []),

    0xfe00: ('arglist', []),
    0xfe01: ('ceq', []),
    0xfe02: ('cgt', []),
    0xfe03: ('rethrow', []),
    0xfe04: ('clt', []),
    0xfe05: ('clt.un', []),
    0xfe06: ('ldftn <method>', [TokenOperand]),
    0xfe07: ('ldvirtftn <method>', [TokenOperand]),

    0xfe09: ('ldarg <uint16 (num)>', [WordOperand]),
    0xfe0a: ('ldarga <uint16 (argNum)>', []),
    0xfe0b: ('starg <uint16 (num)>', [WordOperand]),
    0xfe0c: ('ldloc <uint16 (indx)>', [WordOperand]),
    0xfe0d: ('ldloca <uint16 (indx)>', [WordOperand]),
    0xfe0e: ('stloc <uint16 (indx)>', [WordOperand]),
    0xfe0f: ('localloc', []),

    0xfe11: ('endfilter', []),
    0xfe12: ('unaligned.', []),
    0xfe13: ('volatile.', []),
    0xfe14: ('tail.', []),
    0xfe15: ('initobj <typeTok>', [TokenOperand]),
    0xfe16: ('constrained. <thisType>', [TokenOperand]),
    0xfe17: ('cpblk', []),
    0xfe18: ('initblk', []),
    0xfe19: ('no.{typecheck,rangecheck,nullcheck}', []),
    0xfe1a: ('rethrow', []),

    0xfe1c: ('sizeof <typeTok>', [TokenOperand]),
    0xfe1d: ('refanytype', []),
    0xfe1e: ('readonly.', []),
}


class InvalidOpcodeException(BaseException):
    pass


class BaseInstruction(object):

    def __init__(self, il_stream, decode_token_key=None):
        assert type(il_stream) is ILStream, 'required `il_stream` to be instance of `ILStream`'
        self._decode_token_key = decode_token_key
        self.opcode = None
        self.opcode_size = 0
        self.operands = []
        self.instruction_length = 0
        self.load(il_stream)

    @property
    def mnemonic(self):
        return INSTRUCTION_SET.get(self.opcode, ['<unknown>', None])[0]

    @property
    def string(self):
        return f'{self.mnemonic.split(" ")[0]:15s} {" ".join([str(x) for x in self.operands])}'

    def load_opcode(self, il_stream):
        self.opcode, self.opcode_size = il_stream.read_opcode()
        if self.opcode not in INSTRUCTION_SET.keys():
            raise InvalidOpcodeException(f'opcode `0x{self.opcode:x}` not in defined instruction set.')

    def save_opcode(self, il_stream):
        il_stream.write_opcode(self.opcode)

    def load_operands(self, il_stream):
        instruction_description = INSTRUCTION_SET.get(self.opcode, None)
        if instruction_description is None:
            raise InvalidOpcodeException(f'opcode `{self.opcode:0x:x}` not in defined instruction set.')

        instruction_name, operand_types = instruction_description

        self.operands.clear()
        for operand_cls in operand_types:
            assert issubclass(operand_cls.__class__, BaseOperand.__class__), \
                'operand class must inherit from `BaseOperand`'
            operand = operand_cls(il_stream)
            if operand.type == OP_TYPE_TOKEN and self._decode_token_key:
                operand.value ^= self._decode_token_key
            self.operands.append(operand)

    def save_operands(self, il_stream):
        for operand in self.operands:
            operand.save(il_stream)

    def load(self, il_stream):
        instruction_start = il_stream.tell()
        self.load_opcode(il_stream)
        self.load_operands(il_stream)
        self.instruction_length = il_stream.tell() - instruction_start

    def save(self, il_stream):
        instruction_start = il_stream.tell()
        self.save_opcode(il_stream)
        self.save_operands(il_stream)
        return il_stream.tell() - instruction_start

    def __repr__(self):
        return self.string
