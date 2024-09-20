from DiffieHellman import computeKey

# how to compute the shared parameters?
alicePrivateKey = 4
bobPrivateKey = 3
prime = 23
generator = 5

# Diffie-Hellman key exchange
aliceFirstKey = computeKey(prime, generator, alicePrivateKey)
bobFirstKey = computeKey(prime, generator, bobPrivateKey)
aliceSecondKey = computeKey(prime, bobFirstKey, alicePrivateKey)
bobSecondKey = computeKey(prime, aliceFirstKey, bobPrivateKey)
print(f"Alice: {aliceSecondKey}, Bob: {bobSecondKey}")

