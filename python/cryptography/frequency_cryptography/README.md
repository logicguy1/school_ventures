# Cryptography - Frequency Analysis


The folder Cryptography contains three seperate programs:
- encryption.py (for encryption of a text string)
- frequency.py (for getting a text string of the most frequent used letters)
- frequencyAnalysis.py (for analyzing an unknown message with the text string of the most used letter)

*It also contains a txt folder where txt files will go*

## encryption.py
1. First, you have the name the input file when asked by the prompt: (`Name input txt file`), where your named txt file has to be present in the txt folder.
2. Second, you have to name the output file when asked by the prompt: (`Name output txt file`), where your named file will be inserted into the txt folder. The terminal could for example look like:
```bash
Name input txt file: fileToEncrypt.txt
Name output txt file: encryptedText.txt
```

## frequency.py
With the `frequency.py` program you can insert a txt file and a txt of the cryptography key will be returned. In Danish an example of a crypto key could look like `ERNDTASILGOMKVFHUBPJÅÆØYCZXWQ`. This will be used later in the next program to decrypt the program.
An example of a output from a encrypted file could look like:
```bash
{'A': 0, 'B': 691, 'C': 238, 'D': 0, 'E': 1143, 'F': 0, 'G': 136, 'H': 2201, 'I': 234, 'J': 273, 'K': 253, 'L': 139, 'M': 0, 'N': 172, 'O': 378, 'P': 147, 'Q': 695, 'R': 832, 'S': 67, 'T': 591, 'U': 144, 'V': 461, 'W': 1, 'X': 622, 'Y': 730, 'Z': 738, 'Æ': 359, 'Ø': 852, 'Å': 1132}
HEÅØRZYQBXTVOÆJKCINPULGSWFMAD
```

## frequencyAnalysis.py
Finally, with the `frequencyAnalysis.py` file you can decrypt a substitution encrypted txt file. First you will be asked for a file to decrypt. Afterwards you will be asked for a crypto key. The output will be a txt file to decrypt called `decryptFile.txt`, with this file you can substitute letters until the text is deciphered and readable, which will take some time and patience. The terminal could for example look like this:
```bash
Name file to decrypt: encryptedText.txt
Input crypto key: HEÅØRZYQBXTVOÆJKCINPULGSWFMAD
Name letter to change: g
Name letter to replace: i'
```
which will go on until the txt file is decrypted.
