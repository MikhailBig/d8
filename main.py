import images
import string
import sys

alphabet = list(string.ascii_lowercase)
digits = list(string.digits)
specials = list(string.punctuation)

print(images.logo)


def start_operations():
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while operation not in ['encode', 'decode']:
        operation = input("Wrong input, try again:\n")
    if operation == 'encode':
        encode_text()
    elif operation == 'decode':
        decode_text()


def continue_operations():
    next_operation = input(
        "Continue text operations? Type Y to continue, type N to exit:\n")
    while next_operation not in ['Y', 'yes', 'y', 'N', 'no', 'n']:
        next_operation = input("Type Y to continue, type N to exit:\n")
    if next_operation in ['Y', 'yes', 'y']:
        start_operations()
    elif next_operation in ['N', 'no', 'n']:
        exit()


def encode_text():
    text = input(
        "Enter desired message for the encryption(excluding digits):\n")
    while check_for_digits(text):
        text = input("Wrong input, exclude digits:\n")
    shift = input("Set encryption shift number:\n")
    while check_for_chars(shift):
        shift = input("Shift must be a number:\n")

    encoded_alphabet = alphabet.copy()
    i = 0
    while i < int(shift):
        encoded_alphabet.insert(0, encoded_alphabet.pop())
        i += 1

    encoded_message = ""
    for ch in text.lower():
        if ch not in specials and ch != " ":
            for s in alphabet:
                if s == ch:
                    index = alphabet.index(s)
            ch = encoded_alphabet[index]
        encoded_message += ch

    print("Result:",encoded_message)
    return continue_operations()


def decode_text():
    text = input(
        "Enter message to decrypt:\n")
    while check_for_digits(text):
        text = input("Invalid input, must not contain digits:\n")
    shift = input("Shift number:\n")
    while check_for_chars(shift):
        shift = input("Shift must be a number:\n")
    
    encoded_alphabet = alphabet.copy()
    i = 0
    while i < int(shift):
        encoded_alphabet.insert(0, encoded_alphabet.pop())
        i += 1
    
    decoded_message = ""
    for ch in text.lower():
        if ch not in specials and ch != " ":
            for s in encoded_alphabet:
                if s == ch:
                    index = encoded_alphabet.index(s)
            ch = alphabet[index]
        decoded_message += ch

    print("Result:",decoded_message)
    return continue_operations()

def check_for_chars(string):
    bad_shift = False
    for ch in alphabet:
        if string.find(ch) != -1:
            bad_shift = True
    return bad_shift


def check_for_digits(string):
    contain_digits = False
    for n in digits:
        if string.find(n) != -1:
            contain_digits = True
    return contain_digits


start_operations()
