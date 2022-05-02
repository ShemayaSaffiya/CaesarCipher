ALPHABET_START = ord('A')
ALPHABET_END = ord('Z')


def encrypt(plain_text, key) -> str:

    if key >= 26:
        key %= 26

    cipher_text = ''

    for char in plain_text:
        if ord(char) >= ALPHABET_START and ord(char) <= ALPHABET_END:
            if (key + ord(char)) > ALPHABET_END:
                encoded_character = key + ord(char) - 26
                encoded_character = chr(encoded_character)
            else:
                encoded_character = chr(key + ord(char))

        else:
            encoded_character = chr(ord(char))

        cipher_text += encoded_character

    return cipher_text
plain_text = input("Enter the message to be encrypted: ")
key = int(input("Enter cipher key: "))  

cipher_text = encrypt(plain_text,key)

blocks = 0
spaces = 0

for char in cipher_text:
    if spaces > 4:
        print(" ", end="")
        blocks +=1
        spaces = 0 
        if blocks == 10:
            print(" ")
            blocks = 0 
    print(char, end = "")
    spaces +=1
