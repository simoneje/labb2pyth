import json

def meny():
    print("1.Läs in originalfil")
    print("2.Visa json-data")
    print("3.Lägg till person")
    print("4.Ta bort person")
    print("5.Spara fil")
    print("6.exit")
    val = 0
    val = int(input(val))
    if val == 1:
        ReadFileMeny('personer.csv')
    elif val == 2:
        hej()



def ReadFileMeny(filename):
    listan = []
    filen = filename
    try:
        with open(filen, encoding="utf-8") as f_obj:
            for line in f_obj:
                listan.append(line)
    except FileNotFoundError:
        print(FileNotFoundError)
    for line in listan:
         print(line.rstrip("\n"))

    listan = [x.split(";")[0] for x in listan]
    for y in listan:
        users = {
            "name": y
        }
    listan = [x.split(";")[1] for x in listan]
    for y in listan:
        users = {
            "eftername": y
        }
        print(users)
def hej():
    print("hej")

meny()