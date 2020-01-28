import json

def meny():
    print("1.Läs in originalfil")
    print("2.Visa json-data")
    print("3.Lägg till person")
    print("4.Ta bort person")
    print("5.Spara fil")
    print("6.exit")
    val = ''
    val = int(input(val))
    if val == 1:
        ReadFileMeny('personer.csv')
    elif val == 2:
        hej()



def ReadFileMeny(filename):
    listan = []
    dicken = []
    filen = filename
    try:
        with open(filen, encoding="utf-8") as f_obj:
            for line in f_obj:
                listan.append(line)
    except FileNotFoundError:
        print(FileNotFoundError)   
    for y in listan:
        info = y.rstrip('\n').split(";")
        dicken.append({"name": info[0], "efternamn": info[1], "användarnamn": info[2], "email": info[3]})
    for a in dicken:
        print(a)


def SaveDictTillJson():
    print("yo")

def hej():
    print("hej")

meny()