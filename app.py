from DiffieHellman import DiffieHellman
from CommunicationParty import CommunicationParty
from HMAC import HMAC

# how to compute the shared parameters?
# alicePrivateKey = 4
# bobPrivateKey = 3
# prime = 23
# generator = 5

# Diffie-Hellman key exchange
# aliceFirstKey = computeKey(prime, generator, alicePrivateKey)
# bobFirstKey = computeKey(prime, generator, bobPrivateKey)
# aliceSecondKey = computeKey(prime, bobFirstKey, alicePrivateKey)
# bobSecondKey = computeKey(prime, aliceFirstKey, bobPrivateKey)
# print(f"Alice: {aliceSecondKey}, Bob: {bobSecondKey}")

# task 1
alice = CommunicationParty("Alice")
bob = CommunicationParty("Bob")
dh = DiffieHellman()
dh.keyExchange(alice, bob)

# task 2
hmac = HMAC()
hmac.HMACComputation( 'messagetjjohash',alice.public_key, "sha256")

# task 3

