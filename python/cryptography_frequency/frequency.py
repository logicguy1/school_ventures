danishLetterFreq = {'A': 6.01, 'B': 1.41, 'C': 0.29, 'D': 7.24, 'E': 16.7, 'F': 2.27, 
                    'G': 4.56, 'I': 5.55, 'J': 1.11, 'K': 3.07, 'L': 4.85, 'M': 3.40, 
                    'N': 7.55, 'O': 4.14, 'P': 1.33, 'Q': 0.01, 'R': 7.61, 'S': 5.67, 
                    'T': 7.03, 'U': 1.85, 'V': 2.88, 'W': 0.02, 'X': 0.02, 'Y': 0.72, 
                    'Z': 0.02, 'Æ': 0.93, 'Ø': 0.84, 'Å': 1.03}

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
ERNDTAS = 'ERNDTASILGOMKVFHUBPJÅÆØYCZXWQ'

def getLetterCount(message):
    letterCount = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 
                    'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 
                    'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'Æ': 0, 
                    'Ø': 0, 'Å': 0 }
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

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
    freqPairs.sort(reverse=True)
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    freqOrder = frequencyOrder(message)

    matchscore = 0
    for commonLetter in ERNDTAS[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1

    for uncommonLetter in ERNDTAS[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1
    
    return matchScore

nameInput = input("Name input text: ")

inputFile = open("txt/"+ nameInput, 'r', encoding="utf-8")
message = inputFile.read()
print(getLetterCount(message))
print(frequencyOrder(message))