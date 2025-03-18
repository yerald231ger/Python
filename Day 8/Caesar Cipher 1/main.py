alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += letter
    print(f"The encoded text is {encrypted_text}")


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += letter
    print(f"The decoded text is {decrypted_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid input")