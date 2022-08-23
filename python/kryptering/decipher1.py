file = "txt/chiffer.txt"

#with open("txt/chiffer.txt", encoding="utf8") as file:
#    data = file.read()

def cipher(file, k):
    cipherkey = 4
    if k < 0:
        k = len(cipherkey) + k

decrypt = [cipher(file, -i) for i in range(1,26)]