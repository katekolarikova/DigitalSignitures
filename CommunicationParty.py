from random import randint

from KeyRatcheting import KeyRatcheting
from Cyphers import ColumnTranspositionSubstitutionEncryption, ColumnTranspositionSubstitutionDecryption

class CommunicationParty:
    def __init__(self, name):
        self.name = name
        self.private_key = None
        self.shared_key = None
        self.key_ratcheting = KeyRatcheting()
        self.friends_key = None

    def __str__(self):
        return self.name

    def setPrivateKey(self, min: int, max: int):
        self.private_key = randint(min, max)

    def computeSharedKey(self, prime: int, generator: int) -> int:
        return (generator ** self.private_key) % prime

    def sendMessage(self, message: str):
        # derive message key
        message_key = self.key_ratcheting.derive_message_key(self.shared_key)
        # encrypt message
        encrypted_message = ColumnTranspositionSubstitutionEncryption(message, message_key, 3)
        # derive new chain key
        self.shared_key = self.key_ratcheting.derive_ratchein_key(self.shared_key)

        return encrypted_message

    def receiveMessage(self, message: str):
        message_key = self.key_ratcheting.derive_message_key(self.shared_key)
        # encrypt message
        encrypted_message = ColumnTranspositionSubstitutionDecryption(message, message_key, 3)
        # derive new chain key
        self.shared_key = self.key_ratcheting.derive_ratchein_key(self.shared_key)

        return encrypted_message