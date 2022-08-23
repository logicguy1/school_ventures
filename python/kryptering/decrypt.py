alfabetet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def krypterbogstav(b,i):
    p = alfabetet.index(b)
    p2 = (p + i) % 26
    return alfabetet[p2]

def kryptertekst(i, txt):
    ciffertekst = ""
    for b in txt:
        if b in alfabetet:
            ciffertekst += krypterbogstav(b,i)
        else:
            ciffertekst += b
        return ciffertekst

klartekst = "txt/chiffer.txt"
klartekst = klartekst.upper()
for key in range(25):
    print(str(key) + ": " + kryptertekst(-1 * key, klartekst))