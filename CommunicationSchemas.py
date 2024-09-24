from HMAC import HMAC
from Cyphers import ColumnTranspositionSubstitutionEncryption, ColumnTranspositionSubstitutionDecryption
from CommunicationParty import CommunicationParty
from DiffieHellman import DiffieHellman


class CommunicationSchemas:

    def __init__(self):
        self.dh = DiffieHellman()


    def HMACauthenticationOfPlainTextMessage(self, message, alice: CommunicationParty, bob: CommunicationParty):
        hmac = HMAC()
        shift_amount = 3

        # alices side
        hmac_encryption = hmac.HMACComputation(message, alice.shared_secret_key, "sha256")
        message_hmac = message + "." + hmac_encryption
        encrypted_message = ColumnTranspositionSubstitutionEncryption (message_hmac, alice.shared_secret_key, shift_amount)

        # bobs side
        decrypted_message_hmac = ColumnTranspositionSubstitutionDecryption(encrypted_message, bob.shared_secret_key, shift_amount)
        split_message = decrypted_message_hmac.split(".")
        decrypted_message = split_message[0]
        decrypted_hmac = split_message[1]
        new_message_hmac = hmac.HMACComputation(decrypted_message, bob.shared_secret_key, "sha256")

        print(f"decrypted message: {decrypted_message}, original message: {message}")
        if new_message_hmac == decrypted_hmac:
            print("HMAC is correct #1")
        else:
            print("HMAC is incorrect #1")

    def HMACauthenticationOfCipherText(self, message, alice: CommunicationParty, bob: CommunicationParty):

        # alices side
        message = 'oh no another secret message'
        shift_amount = 3
        hmac = HMAC()
        encrypted_message = ColumnTranspositionSubstitutionEncryption (message, alice.shared_secret_key, shift_amount)
        message_hmac = hmac.HMACComputation(encrypted_message, alice.shared_secret_key, "sha256")
        encrypted_message_hmac = encrypted_message + "." + message_hmac

        # bobs side
        split_message_hmac = encrypted_message_hmac.split(".")
        sent_message = split_message_hmac[0]
        sent_hmac = split_message_hmac[1]
        new_message_hmac = hmac.HMACComputation(sent_message, bob.shared_secret_key, "sha256")
        decrypted_message = ColumnTranspositionSubstitutionDecryption(sent_message, bob.shared_secret_key, shift_amount)

        print(f"decrypted message: {decrypted_message}, original message: {message}")
        if new_message_hmac == sent_hmac:
            print("HMAC is correct #2")
        else:
            print("HMAC is incorrect #2")

    def initDiffieHellmanDoubleRatchet(self, alice: CommunicationParty, bob: CommunicationParty):
        self.generateKeyPair(alice, 1, 50)
        self.generateKeyPair(bob, 51, 99)
        self.publicKeyExchange(alice, bob)
        self.generateSharedSecretKey(alice, bob)

        # init root key from shared secret key
        alice.resetKeyChain()
        bob.resetKeyChain()

    def SingleRatchet(self, alice: CommunicationParty, bob: CommunicationParty):

        self.initDiffieHellmanDoubleRatchet(alice, bob)

        encrypted_message = alice.sendMessage('Hello this is a secret message')
        decrypted_message = bob.receiveMessage( encrypted_message)
        print(f"decrypted message: {decrypted_message}")

        encrypted_message = bob.sendMessage('Hello this is a second secret message')
        decrypted_message = alice.receiveMessage( encrypted_message)
        print(f"decrypted message: {decrypted_message}")

        encrypted_message = bob.sendMessage('Hello this is a third secret message')
        decrypted_message = alice.receiveMessage( encrypted_message)
        print(f"decrypted message: {decrypted_message}")

        encrypted_message = alice.sendMessage('Hello this is a fourth secret message')
        decrypted_message = bob.receiveMessage( encrypted_message)
        print(f"decrypted message: {decrypted_message}")

    def generateKeyPair(self, party: CommunicationParty, min: int = 1, max: int = 50):
        party.setPrivateKey(min, max)
        party.public_key = party.computeSharedKey(self.dh.prime, self.dh.generator)

    def publicKeyExchange(self, alice: CommunicationParty, bob: CommunicationParty):
        alice.friends_key = bob.public_key
        bob.friends_key = alice.public_key

    def generateSharedSecretKey(self, alice: CommunicationParty, bob: CommunicationParty):
        alice.shared_secret_key = alice.computeSharedKey(self.dh.prime, alice.friends_key)
        alice.root_key = alice.shared_secret_key #set initial root key
        bob.shared_secret_key = bob.computeSharedKey(self.dh.prime, bob.friends_key)
        bob.root_key = bob.shared_secret_key #set initial root key

    def DoubleRatchetHardcodeDemo(self, alice: CommunicationParty, bob: CommunicationParty):
        self.initDiffieHellmanDoubleRatchet(alice, bob)
        print('alice shared secret key: ', alice.shared_secret_key)
        print('bob shared secret key: ', bob.shared_secret_key)
        print('alice current chain key: ', alice.current_chain_key)
        print('bob current chain key: ', bob.current_chain_key)

        encrypted_message = alice.sendMessage('Hello this is a secret message')
        decrypted_message = bob.receiveMessage(encrypted_message)
        print(f"decrypted message: {decrypted_message}")

        encrypted_message = bob.sendMessage('Hello this is a second secret message')
        decrypted_message = alice.receiveMessage(encrypted_message)
        print(f"decrypted message: {decrypted_message}")

        self.initDiffieHellmanDoubleRatchet(alice, bob)
        print('alice shared secret key: ', alice.shared_secret_key)
        print('bob shared secret key: ', bob.shared_secret_key)
        print('alice current chain key: ', alice.current_chain_key)
        print('bob current chain key: ', bob.current_chain_key)

        encrypted_message = bob.sendMessage('Hello this is a third secret message')
        decrypted_message = alice.receiveMessage( encrypted_message)
        print(f"decrypted message: {decrypted_message}")

        encrypted_message = alice.sendMessage('Hello this is a fourth secret message')
        decrypted_message = bob.receiveMessage( encrypted_message)
        print(f"decrypted message: {decrypted_message}")

    def DoubleRatchetInteractive(self, alice: CommunicationParty, bob: CommunicationParty):
        self.initDiffieHellmanDoubleRatchet(alice, bob)

        counter = 0
        period = 4

        while True:
            alice_msg = input("Alice msg: ")

            encrypted_message = alice.sendMessage(alice_msg)
            counter += 1
            if counter % period == 0:
                self.initDiffieHellmanDoubleRatchet(alice, bob)
                print('Keys were reset')

            decrypted_message = bob.receiveMessage(encrypted_message)
            print(f"Bob received message: {decrypted_message}")

            bob_msg = input("Bob msg: ")


            encrypted_message = bob.sendMessage(bob_msg)
            counter += 1
            decrypted_message = alice.receiveMessage(encrypted_message)
            print(f"Alice received message: {decrypted_message}")

            if counter % period == 0:
                self.initDiffieHellmanDoubleRatchet(alice, bob)
                print('Keys were reset')


