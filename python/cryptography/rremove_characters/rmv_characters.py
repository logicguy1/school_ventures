# Remove characters from string

nameFile = input("Name input text: ")
char = str(input("Remove character: "))

inputFile = open('txt/', nameFile, 'r', encoding='utf-8')
inputText = inputFile.read() #input file cis onverted to string

remove = inputText.replace(char, '')
outputFile = open('txt/danishDict.txt', 'w', encoding='utf-8')

newFile = outputFile.write(remove)
