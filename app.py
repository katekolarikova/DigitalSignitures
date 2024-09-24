from DiffieHellman import DiffieHellman
from CommunicationParty import CommunicationParty
from HMAC import HMAC
from CommunicationSchemas import CommunicationSchemas
# task 1
print("-----------------TASK 1-----------------")
alice = CommunicationParty("Alice")
bob = CommunicationParty("Bob")
dh = DiffieHellman()
dh.keyExchange(alice, bob)


# task 2
print("-----------------TASK 2-----------------")
hmac = HMAC()
message_hmac = hmac.HMACComputation( 'example of the message',alice.shared_secret_key, "sha256")
print(f"message hmac: {message_hmac}")

# task 3
print("-----------------TASK 3-----------------")
communication_schemas = CommunicationSchemas()
communication_schemas.HMACauthenticationOfPlainTextMessage('Hello this is a secret message', alice, bob)
communication_schemas.HMACauthenticationOfCipherText('Hello this is a secret message', alice, bob)


# task 4
print("-----------------TASK 4-----------------")
communication_schemas.SingleRatchet(alice, bob)

# task 5
print("-----------------TASK 5-----------------")
communication_schemas.DoubleRatchetHardcodeDemo(alice, bob)
communication_schemas.DoubleRatchetInteractive(alice, bob)

