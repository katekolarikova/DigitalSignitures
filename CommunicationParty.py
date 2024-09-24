from random import randint

from KeyRatcheting import KeyRatcheting
from Cyphers import ColumnTranspositionSubstitutionEncryption, ColumnTranspositionSubstitutionDecryption

class CommunicationParty:
    private_key = None
    shared_secret_key = None
    public_key = None
    current_chain_key = None
    friends_key = None
    root_key = None


    def __init__(self, name):
        self.name = name

        self.key_ratcheting = KeyRatcheting()

    def __str__(self):
        return self.name

    def setPrivateKey(self, min: int, max: int):
        self.private_key = randint(min, max)

    def computeSharedKey(self, prime: int, generator = None) -> int:
        if generator == None:
            generator = self.friends_key
        return (generator ** self.private_key) % prime

    def sendMessage(self, message: str):
        # derive message key
        self.current_chain_key = self.key_ratcheting.derive_ratcheting_key(self.current_chain_key)

        message_key = self.key_ratcheting.derive_message_key(self.current_chain_key)
        # encrypt message
        encrypted_message = ColumnTranspositionSubstitutionEncryption(message, message_key, 3)
        # derive new chain key
        self.current_chain_key = self.key_ratcheting.derive_ratcheting_key(self.current_chain_key)

        return encrypted_message

    def receiveMessage(self, message: str):
        self.current_chain_key = self.key_ratcheting.derive_ratcheting_key(self.current_chain_key)

        message_key = self.key_ratcheting.derive_message_key(self.current_chain_key)
        # encrypt message
        encrypted_message = ColumnTranspositionSubstitutionDecryption(message, message_key, 3)
        # derive new chain key
        self.current_chain_key = self.key_ratcheting.derive_ratcheting_key(self.current_chain_key)

        return encrypted_message

    def resetKeyChain(self):
        self.root_key  = self.key_ratcheting.derive_root_key(self.shared_secret_key, self.root_key)
        self.current_chain_key = self.key_ratcheting.derive_ratcheting_key(self.root_key)
