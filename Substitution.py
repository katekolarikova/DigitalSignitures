import random

def encryptSubstitution(text, shift_amount):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ""
    for char in text:
        if char in alphabet:
            char = char.upper()
            result += alphabet[(alphabet.index(char) + shift_amount) % 26]
        else:
            result += char

    return result

def decryptSubstitution(text:str, shift: int):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = ""
    for char in text:
        if char in alphabet:
            result += alphabet[(alphabet.index(char) - shift) % 26]
        else:
            result += char

    return result

