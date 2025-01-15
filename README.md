## Digital Signatures
The main objective is to implement protocols for secure communication between two parties.
The protocols implemented are:
1. Diffie-Hellman Key Exchange
2. HMAC
3. Single ratchet
4. Double ratchet

The code is implemented in python and the code is tested on python 3.12.
All the additional libraries used in the code are included in the requirements.txt file.

The code is implemented in the following files:
1. DiffieHellman.py
- responsible for getting the prime and generator, basic key exchange and encryption and decryption of the message.
2. HMAC.py
- responsible for generating the HMAC of the message for authentication, XOR hashing function
3. app.py
- running each task of the assignment
4. ColumnarTransposition.py
- cipher used for encryption and decryption using transposition
5. CommunicationParty.py
- represents the communication party (Alice and Bob), responsible for sending and receiving messages
6. CommunicationSchemas.py
- represents the communication schemas required in assignment, addition function for double and single ratchet
7. Ciphers
- contains the ciphers used in the assignment for encryption and decryption
8. KeyGenerator.py
- generates key for transposition cipher
9. KeyRatcheting.py
- responsible for ratcheting the keys
10. Substitution.py
- substitution cipher used for encryption and decryption
