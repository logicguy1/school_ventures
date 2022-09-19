
import detectDanish, transpositionDecrypt

def main():
    detectDanish.loadDictionary()
    myMessage = "drmbdbkee meelrtteesreytnlk vpe ieeet hgdrteee    r"
    
    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None :
         print('Failed to hack encryption.')
    else:
        print('Message is decrypted :')
        print(hackedMessage)

def hackTransposition(message):
    print('Hacking...')

    # Brute-force by looping though every possible key:
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)
        
        if detectDanish.isDanish(decryptedText,50):
            # Ask user if this is the correct decryption:
            print()
            print('Danish percentage: '+ (str(100*detectDanish.getDanishCount(decryptedText))))
            for w in decryptedText.split():
                if w.upper() in detectDanish.DANISH_WORDS:
                    print("Word found: "+w)
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()