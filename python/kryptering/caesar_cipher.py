with open("txt/chiffer.txt", encoding="utf-8") as file:

   ord = file.read()

alfabetet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result = []

def kryptering():
    offset = 8 
    ifKrypter = int(input("0=krypter | 1=dekrypter: "))
    alfabetCount = 0

    alfabetCount = 0
    for x in ord:
        if(x.upper() in alfabetet):
            for y in range(len(alfabetet)):
                if (alfabetet[y] == x.upper()):
                    alfabetCount = y
            if(ifKrypter == 0):
                if(y+offset>=26):
                    result.append(alfabetet[(alfabetCount+offset)-26])
                else:
                    result.append(alfabetet[alfabetCount+offset])
            elif (ifKrypter == 1):
                if(y-offset<=0):
                    result.append(alfabetet[(alfabetCount-offset)+26])
                else:
                    result.append(alfabetet[alfabetCount-offset])
        else:
            result.append(x)

kryptering()

for i in result:
    print(str(i), end = '')