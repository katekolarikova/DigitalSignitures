import random
from sympy.ntheory.factor_ import smoothness_p, factorint


def getPrime() -> int:
    prime = 0
    start = random.randint(1000, 2000)
    end = start+1000
    for i in range(end, start):
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i-1:
                prime = i
                break
        if prime != 0:
            break
    return prime


# https://www.geeksforgeeks.org/primitive-root-of-a-prime-number-n-modulo-n/
def getGenerator(prime: int) -> int:
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

    print(f"generator{ generator}")

    return generator

def computeKey(prime: int, generator: int, privateKey: int) -> int:
    return (generator ** privateKey) % prime

getGenerator(761)