dictionary_words = {}

def newWord():
    for i in range(1):
        word = str(input("Enter new word: "))
        word_definition = str(input("Enter definition of word: "))
        if word not in dictionary_words:
            dictionary_words[word] = word_definition
    menu()

def output():
    for key, value in dictionary_words.items():
        print(key, ' : ', value)
    menu()

def search():
    entry = input("Enter search word: ")
    if entry in dictionary_words:
        print ("\n" + "Word: " + entry + "\n")
        print ("Definition: " + str(dictionary_words[entry]))
    else:
        print("Your word is not in dictionary")
    menu()
    
def menu():
    choice = str(input("Enter your choice (1 for new word, 2 for print dictionary, 0 to end >"))
    if choice == "1":
        newWord()
    if choice == "2":
        output()
    if choice == "0":
        print("Goodbye")
    if choice == "search":
        search()

menu()
