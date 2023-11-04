alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def Caesar_Cipher(text, shift, direction):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = (position + shift)%26
        else:
            new_position = (position - shift)%26
        new_letter = alphabet[new_position]
        new_text += new_letter
    print(new_text)


if "__main__" == __name__:
    while True:
        direction = input("Type 'encode' to Encrypt, type 'decode' to Decrypt: ").lower()
        text = input("Type your message: ").lower()
        shift = int(input("Type the Shift Number: "))
        Caesar_Cipher(text=text, shift=shift, direction=direction)
