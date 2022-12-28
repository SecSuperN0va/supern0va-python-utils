import string


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def hexdump(data, block_size=0x10):
    """
    Create a pretty-printed hexdump of the input data.
    :param data: `bytearray` to hexdump
    :param block_size: size of each row of the hexdump (defaults to 0x10)
    :return: the formatted string representation of the hexdump
    """
    n_blocks = 0 if not len(data) else int(((len(data) / block_size) + 1))
    output = str()

    output += bcolors.HEADER + '          {:50s}    {:16s}\n'.format(
        ' '.join(['{:02x}'.format(x) for x in range(block_size)]),
        ' '.join(['{:01x}'.format(x) for x in range(block_size)]),
    )
    output += '-' * len(output)
    output += bcolors.ENDC + '\n'
    for i in range(n_blocks):
        block = data[(i * block_size): ((i + 1) * block_size)]
        hex_str = ' '.join(['{:02x}'.format(b) for b in block])
        ascii_str = ' '.join(chr(b) if chr(b).isalnum() else '.' for b in block)
        output += bcolors.HEADER + '{:08x}: '.format(i * block_size) + bcolors.ENDC
        output += bcolors.OKBLUE + '{:50s}    {:16s}\n'.format(hex_str, ascii_str) + bcolors.ENDC
    return '\n' + output
