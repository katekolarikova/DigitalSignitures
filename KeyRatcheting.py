import hmac
import hashlib
import secrets

class KeyRatcheting:


    def derive_ratchein_key(self, kchain, ratchet_label="ratchet"):
        """Derives a new chain key using HMAC-based PRNG."""
        if type(kchain) != bytes:
            kchain = kchain.to_bytes(2, 'big')
        new_key_chain = hmac.new(kchain, ratchet_label.encode(), hashlib.sha256).digest()

        return new_key_chain

    def derive_message_key(self, kchain,  ratchet_label="message"):
        if type(kchain) != bytes:
            kchain = kchain.to_bytes(2, 'big')
        message_key = hmac.new(kchain, ratchet_label.encode(), hashlib.sha256).hexdigest()
        message_key = "".join(c for c in message_key if c.isdecimal())
        result = 0
        for c in message_key:
            result = result + int(c)

        message_key = str(result)
        return message_key

# def encrypt_message(message, kchain):
#     """Encrypts a message using the derived message key."""
#     message_key = derive_message_key(kchain)
#     # use derived message key to encrypt the message
#     ciphertext = "to-do"
#
#     return ciphertext
#
# def decrypt_message(ciphertext, kchain):
#     """Decrypts a message using the derived message key."""
#     message_key = derive_message_key(kchain)
#
#    # decrypt the message using the derived message key
#     plaintext = "to-do"
#     return plaintext
#
# def single_ratchet_exchange(initial_chain_key, message):
#     # Alice's side
#     chain_key = initial_chain_key
#     encrypted_message = encrypt_message(message, chain_key)
#     chain_key = derive_ratchein_key(chain_key)
#
#     # Bob's side
#     received_message = encrypted_message
#     message_key = derive_message_key(chain_key)
#     decrypted_message = decrypt_message(received_message, message_key)
#     chain_key = derive_ratchein_key(chain_key)
#
#     return decrypted_message
#
# def double_ratchet_exchange(initial_chain_key, message):
#     # Alice's side
#     chain_key = initial_chain_key
#     encrypted_message = encrypt_message(message, chain_key)
#     chain_key = derive_ratchein_key(chain_key)
#
#     # Bob's side
#     received_message = encrypted_message
#     message_key = derive_message_key(chain_key)
#     decrypted_message = decrypt_message(received_message, message_key)
#
#     # generate a new chain key
#     new_chain_key = "to-do"
#
#     # Alice's side
#     chain_key = new_chain_key
#     encrypted_message = encrypt_message(message, chain_key)
#     chain_key = derive_ratchein_key(chain_key)
#
#     # Bob's side
#     received_message = encrypted_message
#     message_key = derive_message_key(chain_key)
#     decrypted_message = decrypt_message(received_message, message_key)
#
#     return decrypted_message

# Example usage:

# Generate an initial chain key
# initial_kchain = secrets.token_bytes(32) # use diffie hellman to generate a random key later
# single_ratchet_exchange(initial_kchain, "Hello, world!")

# Send a message
# kchain = initial_kchain
# encrypted_message = encrypt_message("Hello, world!", kchain)
# kchain = derive_ratchein_key(initial_kchain)
#
# # Receive and decrypt the message
# decrypted_message = decrypt_message(encrypted_message, kchain)
# print(decrypted_message)  # Output: Hello, world!
#
# # Send another message
# encrypted_message = encrypt_message("How are you?", kchain)
# kchain = derive_chain_key(kchain)

# ... continue sending and receiving messages ...