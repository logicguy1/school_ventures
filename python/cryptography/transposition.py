import math

def encryptMessage(key, message):
    ciphertext = [''] * key
    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key

    return ''.join(ciphertext)

def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1  # Point to next column.
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == "__main__":
    print("\nEncryption: \n")
    myMessage = str(input('Enter message you would like to encrypt: '))
    myKey = int(input('Enter key you would like to encrypt with: '))

    ciphertext = encryptMessage(myKey, myMessage)

    print("\nDecryption: \n")
    myMessage = str(input('Enter encrypted message you would like to encrypt: '))
    myKey = int(input('Enter key you would like to decrypt with: '))

    plaintext = decryptMessage(myKey, myMessage)
