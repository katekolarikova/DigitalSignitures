def pad_to_bytes(number, num_bytes):
    """Pads a number to the specified number of bytes."""
    binary_representation = bin(number)[2:]
    required_bits = binary_representation.zfill(num_bytes * 8)
    padded_binary = binary_representation.rjust(required_bits, '0')
    return int(padded_binary, 2)

number = 123
padded_number = pad_to_bytes(number, 32)  # Pad to 2 bytes (16 bits)
print(padded_number)