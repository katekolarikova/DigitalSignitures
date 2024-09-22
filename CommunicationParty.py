from random import randint


class CommunicationParty:
    def __init__(self, name):
        self.name = name
        self.private_key = None
        self.public_key = None

    def __str__(self):
        return self.name

    def setPrivateKey(self, min: int, max: int):
        self.private_key = randint(min, max)

    def computeSharedKey(self, prime: int, generator: int) -> int:
        return (generator ** self.private_key) % prime