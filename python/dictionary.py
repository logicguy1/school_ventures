import pickle

dictionary_words = {}

def newWord():
    for i in range(1):
        word = str(input("Enter new word: "))
        word_definition = str(input("Enter definition of word: "))
        if word not in dictionary_words:
            dictionary_words[word] = word_definition
    menu()

def udskriv():
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

def delete():
    del_word = input("What word would you like to delete from dictionary?: ")
    if del_word  in dictionary_words:
        del dictionary_words[del_word]
        print(del_word + "has been deleted from dictionary")
        menu()
    else: 
        print(del_word + "is not in dictionary")
    menu()

def menu():
    choice = str(input("Enter your choice (1 for new word, 2 for print dictionary, 3 to delete word, 0 to end >"))
    if choice == "1":
        newWord()
    if choice == "2":
        udskriv()
    if choice == "3":
        delete()
    if choice == "0":
        pickle.dump(dictionary_words, open("save.pkl", "wb"))        
        print("Goodbye")
    if choice == "search":
        search()

try:
    data = pickle.load(open("save.p", "rb"))
except (EOFError, FileNotFoundError):
    data = {}

menu()
