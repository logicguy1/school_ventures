
UPPERLETTERS = 'ABCDEFGHIJKLMONPQRSTUVWXYZÆØÅ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
    dictionaryFile = open('dictionary.txt', encoding="utf-8")
    danishWords = {}
    for word in dictionaryFile.read().split('\n'):
        word = word.upper()
        danishWords[word] = None
    dictionaryFile.close()
    return danishWords

DANISH_WORDS = loadDictionary()

def getDanishCount(message):
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()

    if possibleWords == [] :
        return 0.0 # No words at all, so return 0.0

    matches = 0
    for word in possibleWords:
        if word in DANISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    lettersOnly = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)

def isDanish(message, wordPercentage=20, letterPerchentage=85 ):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).

    wordsMatch = getDanishCount(message) * 100 >= wordPercentage
    numLetters = len(removeNonLetters(message))
    messageLettersPercentage = float(numLetters) / len(message) * 100
    lettersMatch = messageLettersPercentage >= letterPerchentage
    return wordsMatch and lettersMatch