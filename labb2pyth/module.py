import json

#from json import JSONEncoder
listan = []
dicken = []



def ReadFileMeny(filename):
    filen = filename
    try:
        with open(filen, encoding="utf-8") as f_obj:
            for line in f_obj:
                listan.append(line)
    except FileNotFoundError:
        print(FileNotFoundError)   
    for y in listan:
        info = y.rstrip('\n').split(";")
        dicken.append({"name": info[0],"efternamn": info[1],"användarnamn": info[2],"email": info[3]})
    for a in dicken:
        print(a)
    return dicken
        
    # print("Vill du spara denna dict till en json-fil? Y/N")
    # val = ''
    # val = str(input(val))
    # if val == 'y':
    #     SaveDictTillJson(dicken)
    
    

def SaveDictTillJson(list):
    listan = list
    try:
        with open('./hej/personer.json', 'w', encoding="utf-8") as json_dicken:
            json.dump(listan, json_dicken,ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(FileNotFoundError)

def VisaJsonData(filename):
    try:
        with open(filename, "r", encoding="utf-8") as sJson:
            return json.load(sJson)
    except FileNotFoundError as error:
        print(error)

def SparaHuman(filename):
    try:
        with open(filename, "w", encoding="utf-8") as sHuman:
            json.dump(dicken, sHuman, ensure_ascii=False, indent=4)
    except FileNotFoundError as error:
        print(error)

def CreateHuman():
    namn = input("Skriv in nytt namn: ")
    enamn = input("Skriv in efternamn: ")
    user = input("Skriv in nytt användarnamn: ")
    mejl = input("Skriv in nytt mejl: ")
    dicken.append({
        "name": namn,
        "efternamn": enamn,
        "användarnamn": user,
        "email": mejl
    })

def RemoveHuman():
    human = input("Skriv in efternamn på den du vill ta bort: ")
    for i in range(len(dicken)):
        if human == dicken[i]["efternamn"]:
            del dicken[i]
            break


# def SaveObjectTillJson(object):
#     personen = object
#     with open('./hej/personer.json', 'w') as json_person:
#         json.append(personen, json_person)
  
# class skapaPerson():
#     def __init__(self, name, lastname, username, email):
#         self.name = name
#         self.lastname = lastname
#         self.username = username
#         self.email = email
#     def presenteraName(self):
#         return self.name + ' ' + self.lastname + ' ' + self.username + ' ' + self.email
#     #def info(self):
#     #    print(f'din person heter{self.name.title}, har efternamn {self.lastname}')
