from hashlib import sha256
import sys
import binascii
import re

# https://medium.com/@short_sparrow/how-hmac-works-step-by-step-explanation-with-examples-f4aff5efb40e
class HMAC:
    def stringBitwiseXor(self, s1, s2):
        result = ""
        for bit1, bit2 in zip(s1, s2):
            if bit1 == bit2:
                result += "0"
            else:
                result += "1"

        return result


    def hashXOR(self, block_size: int, message) -> str:

        # add padding to message to match block size
        message = message.decode("utf-8")
        key_length = len(str(message))
        diff = key_length % block_size
        if diff != 0:
            message = str(message) + '0' * ((block_size - diff))  # add padding
            if key_length % 2 != 0:  # if odd number of digits
                message = message + '0'

        blocks = []

        # split text into blocks
        message = str(message)
        for i in range(0, len(message)-1, block_size):
            blocks.append(message[i:i + block_size])

        # XOR all blocks
        previous_block = ''.join(format(ord(i), '08b') for i in blocks[0])
        for i in range(1, len(blocks)):
            current_block = ''.join(format(ord(i), '08b') for i in blocks[i])
            previous_block = self.stringBitwiseXor(previous_block, current_block)

        # Convert the binary string to bytes
        bytes_list = [int(previous_block[i:i + 8], 2) for i in range(0, len(previous_block), 8)]
        byte_string = bytes(bytes_list)

        # Decode the byte string to utf-8
        utf8_string = byte_string.decode("utf-8")

        # Remove non-printable characters
        printable_utf8_string = re.sub(r'[^\x20-\x7E]', '0', utf8_string)

        return printable_utf8_string

    def HMACComputation(self, message: str, key:int, hash_function:str) ->str :

        message = message.replace(" ", "")
        # define block size of hash function
        block_size = sha256().block_size # in bytes
        key_length = len(str(key)) # in bytes, 1 digit = 1 byte

        # add padding to key to match block size
        if len(str(key)) < block_size:
            # '0' - 1 byte
            key = str(key) + '0' * ((block_size - key_length)) # add padding
            if key_length % 2 != 0: # if odd number of digits
                key = key + '0'
        else: # if key is longer than block size
            key = str(key)[:block_size]

        # convert key to hex
        hex_key = binascii.hexlify(key.encode('utf-8')).decode('utf-8')

        # create ipad and opad
        ipad = '36' * block_size # 0x36 - 1 byte
        opad = '5c' * block_size

        # XOR key with ipad and opad
        opad_XOR = int(hex_key, 16) ^ int(opad, 16)
        ipad_XOR = int(hex_key, 16) ^ int(ipad, 16)

        # use hash function
        if hash_function == 'sha256':
            inner = sha256(hex(ipad_XOR)[2:].encode() + message.encode()).hexdigest()
            outer = sha256(hex(opad_XOR)[2:].encode() + inner.encode()).hexdigest()
        elif hash_function == 'xor':
            inner = self.hashXOR(64, hex(ipad_XOR)[2:].encode() + message.encode())
            outer = self.hashXOR(64, hex(opad_XOR)[2:].encode() + inner.encode())
        else:
            sys.exit("Invalid hash function")

        return outer


