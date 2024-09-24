import random
from sympy.ntheory.factor_ import  factorint
from CommunicationParty import CommunicationParty


class DiffieHellman:
    def __init__(self):
        self.prime = self.getPrime()
        self.generator = self.getGenerator(self.prime)


    def getPrime(self) -> int:
        prime = -1
        start = random.randint(1000, 2000)
        end = start+1000
        for i in range(start, end):
            for j in range(2, i):
                if i % j == 0:
                    break
                if j == i-1:
                    prime = i
                    break
            if prime != -1:
                break
        return prime


    # https://www.geeksforgeeks.org/primitive-root-of-a-prime-number-n-modulo-n/
    def getGenerator(self, prime: int) -> int:
        generator = -1
        phi = prime-1 # pocet nesoudelnych cisel - Eulerova funkce

        prime_factors = factorint(phi) # prime factors of phi - number which divides phi
        for g in range(2, phi + 1): # 1 is not a generator and generator cannot be greater than phi
            flag = False
            for it in prime_factors:
                # i^(φ(n)/p) modulo n cannot be 1 for any i in prime factors
                if (g ** (phi // it)) % prime == 1: # cannot be 1
                    flag = True
                    break

            if flag == False:
                generator = g
                break

        # primitive root modulo p
        return generator % self.prime

    def keyExchange(self, alice: CommunicationParty, bob: CommunicationParty) -> tuple:

        #initial setup, generating private and public keys
        alice.setPrivateKey(1, 50)
        bob.setPrivateKey(51, 99)
        alice.public_key = alice.computeSharedKey(self.prime, self.generator)
        bob.public_key = bob.computeSharedKey(self.prime, self.generator)

        #exchange public keys
        bob.friends_key = alice.public_key
        alice.friends_key = bob.public_key

        #generate shared secret key
        alice.shared_secret_key = alice.computeSharedKey(self.prime)
        bob.shared_secret_key = bob.computeSharedKey(self.prime)
        print("Successfully exchanged keys")
