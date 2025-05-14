import string
letters=list(string.ascii_lowercase)
print(letters)
running=True


def encode_Message(message,shiftPos):
    encryptedText = ""


    for idx, char in enumerate(messageToEncrypt):
        letterpos = letters.index(char)
        encryptedChar = letters[letterpos + shiftPos]
        char = encryptedChar

        encryptedText += char
    return encryptedText


def decode_message(messageToDecode,shiftPos):
    decryptedText = ""
    for idx, char in enumerate(messageToDecode):
        letterpos = letters.index(char)
        decryptedChar = letters[letterpos - shiftPos]
        char = decryptedChar
        decryptedText += char
    return decryptedText


while running:
    encodeOrEncrypt=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if encodeOrEncrypt=='encode':
        messageToEncrypt = input("Type the message to encrypt:\n")
        shiftPos = int(input("Enter shift position:"))
        encryptedText = encode_Message(messageToEncrypt,shiftPos)
        print(f"Here's the encoded result: {encryptedText}")

    elif encodeOrEncrypt=='decode':
        messageToDecrypt = input("Type the message to decrypt:\n")
        shiftPos = int(input("Enter shift position:"))
        decryptedText = decode_message(messageToDecrypt, shiftPos)
        print(f"Here's the decoded result: {decryptedText}")



    doItAgain=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if doItAgain=='no':
        print("Goodbye")
        running=False






