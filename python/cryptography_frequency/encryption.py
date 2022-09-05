import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
ERNDTAS = 'ERNDTASILGOMKVFHUBPJÅÆØYCZXWQ'

def encrypt(text,key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += encryptChar(char,key)
    return result

def encryptChar(char, key):
    pos = LETTERS.find(char.upper())
    if pos == -1:
        return char
    else:
        return key[pos]

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

def convert(string):
    list1 = []
    list1[:0] = string
    return list1

def deconvert(list):
    mystring = ''
    for x in list:
        mystring += ''+ x
    return mystring

s = convert(LETTERS)
for i in range(3):
    random.shuffle(s)
key = deconvert(s)
print("Your key " + key)

nameInput = input("Name input txt file: ")
nameOutput = input("Name output txt file: ")
outputFile = open("txt/" + nameOutput,'w', encoding='utf-8')
file = open("txt/" + nameInput, 'r', encoding='utf-8')

while 1:
    char = file.read(1)
    if not char:
        break
    encryptedChar = encryptChar(char, key)
    outputFile.write(encryptedChar)