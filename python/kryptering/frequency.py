danishLetterFreq = {'A': 6.01, 'B': 1.41, 'C': 0.29, 'D': 7.24, 'E': 16.7, 'F': 2.27, 
                    'G': 4.56, 'I': 5.55, 'J': 1.11, 'K': 3.07, 'L': 4.85, 'M': 3.40, 
                    'N': 7.55, 'O': 4.14, 'P': 1.33, 'Q': 0.01, 'R': 7.61, 'S': 5.67, 
                    'T': 7.03, 'U': 1.85, 'V': 2.88, 'W': 0.02, 'X': 0.02, 'Y': 0.72, 
                    'Z': 0.02, 'Æ': 0.93, 'Ø': 0.84, 'Å': 1.03}

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
ERNDTAS = 'ERNDTASILGOMKVFHUBPJÅÆØYCZXWQ'

def menu():
    choice = str(input("Press '1' for encryption, '2' for decryption and '0' to end program: "))
    if choice == "1":
        s = 4
        outputFile = open('output.txt','w', encoding='utf-8')
        file = open('test.txt', 'r', encoding='utf-8')
        while 1:
            char = file.read(1)
            if not char:
                break
            encryptedChar = encryptChar(char, s)
            outputFile.write(encryptedChar)
        menu()
    if choice == "2":
        decrypt()
    if choice == "0":
        print("Goodbye")

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += encryptChar(char,s)
    return result

def encryptChar(char, s):
    if (char.isupper()):
        result = chr((ord(char) + s - 65) % 26 + 65)
    else:
        result = chr((ord(char) + s - 97) % 26 + 97)
    return result

def getLetterCount(message):
    letterCount = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 
                    'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 
                    'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 
                    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
                    'Y': 0, 'Z': 0, 'Æ': 0, 'Ø': 0, 'Å': 0 }
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
        return letterCount

def decrypt():
    inputFile = open('random.txt', 'r')
    message = inputFile.read()
    getLetterCount(message)
    frequencyOrder(message)

def frequencyOrder(message):
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)
    
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ERNDTAS.find,reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(reverese=True)
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

menu()