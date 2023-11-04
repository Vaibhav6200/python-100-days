alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount)%26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)


def Decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = (position - shift_amount)%26
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(plain_text)



if "__main__" == __name__:
    while True:
        direction = input("Type 'encode' to Encrypt, type 'decode' to Decrypt: ").lower()
        if direction == "encode":
            text = input("Type your message: ").lower()
            shift = int(input("Type the Shift Number: "))
            Encrypt(text, shift)
        elif direction == "decode":
            text = input("Type your message: ").lower()
            shift = int(input("Type the Shift Number: "))
            Decrypt(text, shift)
        else:
            print("Enter Valid Direction")

