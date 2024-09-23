import random

from KeyGenerator import createKey
from ColumnTransposition import encryptColumnTransposition, decryptColumnTransposition
from Substitution import encryptSubstitution, decryptSubstitution



def ColumnTranspositionSubstitutionEncryption(text, key_transpostion, shift_amount):
    text = text.replace(" ", "")
    desired_order = createKey(key_transpostion)
    transposition = encryptColumnTransposition(text, desired_order)
    transposition_substitution:str = encryptSubstitution(transposition, shift_amount)

    return transposition_substitution


def ColumnTranspositionSubstitutionDecryption(text, key_transpostion, shift_amount):
    text = text.replace(" ", "")
    desired_order = createKey(key_transpostion)
    decrypt_substitution:str = decryptSubstitution(text, shift_amount)
    decrypt_transposition = decryptColumnTransposition(decrypt_substitution, desired_order)

    decrypt_transposition = decrypt_transposition.replace("-", "")

    return decrypt_transposition
