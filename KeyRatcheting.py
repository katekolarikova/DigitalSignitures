import hmac
import hashlib
import secrets

class KeyRatcheting:

    def derive_ratcheting_key(self, kchain, ratchet_label="ratchet"):

        if type(kchain) != bytes:
            kchain = kchain.to_bytes(2, 'big')
        new_key_chain = hmac.new(kchain, ratchet_label.encode(), hashlib.sha256).digest()

        return new_key_chain

    def derive_root_key(self, kchain, root, ratchet_label="ratchet"):
        if type(kchain) != bytes:
            kchain = kchain.to_bytes(2, 'big')
        if type(root) != bytes:
            root = root.to_bytes(2, 'big')

        kchain = kchain + root
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




