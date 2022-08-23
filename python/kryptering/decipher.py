file = "txt/chiffer.txt"

with open(file, encoding="utf8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())