def xor(data, key):
    """
    :param data: `bytearray` containing the data to XOR
    :param key: `bytearray` containing the bytes of the XOR key.
    :return: `bytearray` containing the decoded data
    """
    return bytearray([data[i] ^ key[i % len(key)] for i in range(len(data))])
