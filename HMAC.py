import math
from hashlib import sha256
import sys
import binascii



# https://medium.com/@short_sparrow/how-hmac-works-step-by-step-explanation-with-examples-f4aff5efb40e


# what shoudl be a hash function? some two versions of hash functions
def HMACSHA256(message: str, key:int) ->str :
    # Step 1: Padding key
    block_size = sha256().block_size # in bytes
    key_length = len(str(key)) # in bytes, 1 digit = 1 byte
    print(f"key_length: {key_length}")
    if len(str(key)) < block_size:
        key = str(key) + '0' * ((block_size - key_length) )
        if key_length % 2 != 0:
            key = key + '0'
    else:
        key = str(key)[:block_size]
    print(f"key: {key}")
    hex_key = binascii.hexlify(key.encode('utf-8')).decode('utf-8')

    ipad = '36' * block_size
    opad = '5c' * block_size

    opad_XOR = int(hex_key, 16) ^ int(opad, 16)
    ipad_XOR = int(hex_key, 16) ^ int(ipad, 16)

    inner = hex(ipad_XOR)[2:].encode() + message.encode()
    outer = sha256(hex(opad_XOR)[2:].encode() + inner).hexdigest()

    hash = sha256(outer.encode()).hexdigest()
    print(f"hash: {hash}")
    return hash


HMACSHA256('hello', 1335567787)
