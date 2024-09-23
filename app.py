from os.path import split

from pyexpat.errors import messages

from DiffieHellman import DiffieHellman
from CommunicationParty import CommunicationParty
from HMAC import HMAC
from Cyphers import ColumnTranspositionSubstitutionDecryption, ColumnTranspositionSubstitutionEncryption

# task 1
# alice = CommunicationParty("Alice")
# bob = CommunicationParty("Bob")
# dh = DiffieHellman()
# dh.keyExchange(alice, bob)

# task 2
# hmac = HMAC()
# hmac.HMACComputation( 'messagetjjohash',alice.shared_key, "sha256")
#
# # task 3
# # as a key for HMAC we should use the shared key derived from diffie hellman
# message = 'Hello this is a secret messageqwer'
# key_transpostion = "04058"
# shift_amount = 3


# # SCHEMA 1
# # alices side
# message_hmac = hmac.HMACComputation(message, alice.shared_key, "sha256")
# message = message + "." + message_hmac
# encrypted_message = ColumnTranspositionSubstitutionEncryption (message, key_transpostion, shift_amount)
#
#
# # bobs side
# decrypted_message = ColumnTranspositionSubstitutionDecryption(encrypted_message, key_transpostion, shift_amount)
# decrypted_message = decrypted_message.split(".")
# decrypted_message_hmac = hmac.HMACComputation(decrypted_message[0], bob.shared_key, "sha256")
# print(f"decrypted message: {decrypted_message[0]}, original message: {message}")
#
# print(f"decrypted message hmac: {decrypted_message_hmac}, original message hmac: {decrypted_message[1]}")
# if decrypted_message_hmac == decrypted_message[1]:
#     print("HMAC is correct")
#
# # SCHEMA 2
# # alices side
# message = 'Hello this is a secret messageqwer'
# key_transpostion = "04058"
# shift_amount = 3
# encrypted_message = ColumnTranspositionSubstitutionEncryption (message, key_transpostion, shift_amount)
# message_hmac = hmac.HMACComputation(encrypted_message, alice.shared_key, "sha256")
# encrypted_message = encrypted_message + "." + message_hmac
#
# # bobs side
# split_message = encrypted_message.split(".")
# hmac_bob = hmac.HMACComputation(split_message[0], bob.shared_key, "sha256")
# decrypted_message = ColumnTranspositionSubstitutionDecryption(split_message[0], key_transpostion, shift_amount)
# print(f"decrypted message: {decrypted_message}, original message: {message}")
# if hmac_bob == split_message[1]:
#     print("HMAC is correct 2")

# task 4
# muzu provest to harakiri s klicem?
# encrypted_message = alice.sendMessage('Hello this is a secret message')
# decrypted_message = bob.receiveMessage( encrypted_message)
# print(f"decrypted message: {decrypted_message}")
#
# encrypted_message = bob.sendMessage('Hello this is a second secret message')
# decrypted_message = alice.receiveMessage( encrypted_message)
# print(f"decrypted message: {decrypted_message}")
#
# encrypted_message = bob.sendMessage('Hello this is a third secret message')
# decrypted_message = alice.receiveMessage( encrypted_message)
# print(f"decrypted message: {decrypted_message}")
#
# encrypted_message = alice.sendMessage('Hello this is a fourth secret message')
# decrypted_message = bob.receiveMessage( encrypted_message)
# print(f"decrypted message: {decrypted_message}")

# task 5
alice = CommunicationParty("Alice")
alice.setPrivateKey(1, 50)
bob = CommunicationParty("Bob")
bob.setPrivateKey(51, 100)
alice_shared_key = alice.computeSharedKey(23, 5)
bob_shared_key = bob.computeSharedKey(23, 5)
alice.friends_key = bob_shared_key
alice.shared_key = alice.computeSharedKey(23, alice.friends_key)
message = 'Hello this is a secret message'
encrypted_message = alice.sendMessage(message)

bob.friends_key = alice_shared_key
bob.shared_key = bob.computeSharedKey(23, bob.friends_key)
decrypted_message = bob.receiveMessage(encrypted_message)
print(decrypted_message)

# bob will generate new key
bob.setPrivateKey(101, 150)
bob_shared_key = bob.computeSharedKey(23, alice_shared_key)
message2 = 'Hello this is a second secret message'
encrypted_message = bob.sendMessage(message2)

alice.friends_key = bob_shared_key
alice.shared_key = alice.computeSharedKey(23, alice.friends_key)
decrypted_message = alice.receiveMessage(encrypted_message)
print(decrypted_message)
