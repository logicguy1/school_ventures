ERNDTAS = 'ERNDTASILGOMKVFHUBPJÅÆØYCZXWQ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

def convert(string):
    list1 = []
    list1[:0] = string
    return list1

def deconvert(list):
    mystring = ''
    for x in list:
        mystring += ''+ x
    return mystring

nameInput = input("Name file to decrypt: ")
inputFile = open("txt/" + nameInput, 'r', encoding='utf-8')
inputTxt = inputFile.read()

key = input("Input crypto key: ")

while True:
    output = ''
    for letter in inputTxt.upper():
        pos = key.find(letter)
        if pos == -1:
            output += letter
        else:
            output += ERNDTAS[pos]

    file = open("txt/decryptFile.txt", "w", encoding='utf-8')
    file.write(output)
    file.close()

    exchangeLetter = input("Name letter to change: ")
    changeLetter = input("Name letter to replace: ")

    if exchangeLetter == '':
        break
    pos = ERNDTAS.find(exchangeLetter.upper())
    letterToChange = key[pos]
    pos2 = ERNDTAS.find(changeLetter.upper())
    letterToChange2 = key[pos2]
    list = convert(key)
    list[pos] = letterToChange2
    list[pos2] = letterToChange
    key = deconvert(list)
    print("New key is " + key)

