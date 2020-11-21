import images
import string

alphabet = list(string.ascii_lowercase)
digits = list(string.digits)
specials = list(string.punctuation)

print(images.logo)

def start_operations():
    operation = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while operation not in ['encode', 'decode']:
        operation = input("Wrong input, try again:\n")

    if operation == 'encode':
        text = input(
        "Enter desired message for the encryption:\n")
    elif operation == 'decode':
        text = input(
        "Enter message to decrypt:\n")

    shift = input("Set encryption shift number:\n")
    while check_for_chars(shift):
        shift = input("Shift must be a number:\n")

    caesar(text, shift, operation)

def continue_operations():
    next_operation = input(
        "Continue text operations? Type Y to continue, type N to exit:\n")
    while next_operation not in ['Y', 'yes', 'y', 'N', 'no', 'n']:
        next_operation = input("Type Y to continue, type N to exit:\n")
    if next_operation in ['Y', 'yes', 'y']:
        start_operations()
    elif next_operation in ['N', 'no', 'n']:
        exit()

def check_for_chars(string):
    bad_shift = False
    for ch in alphabet:
        if string.find(ch) != -1:
            bad_shift = True
    return bad_shift

def caesar(text, shift, operation):
    encoded_alphabet = alphabet.copy()
    i = 0
    while i < int(shift):
        encoded_alphabet.insert(0, encoded_alphabet.pop())
        i += 1
    result_message = ""
    for ch in text.lower():
        if ch not in specials and ch != " " and ch not in digits:
            if operation == 'encode':
                # encode
                for s in alphabet:
                    if s == ch:
                        index = alphabet.index(s)
                ch = encoded_alphabet[index]
            elif operation == 'decode':
                # decode
                for s in encoded_alphabet:
                    if s == ch:
                        index = encoded_alphabet.index(s)
                ch = alphabet[index]
        result_message += ch
    print("Result:", result_message)
    return continue_operations()

start_operations()