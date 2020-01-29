import module

def meny():
    print("1.Läs in originalfil")
    print("2.Visa json data")
    print("3.Lägg till person")
    print("4.Ta bort person")
    print("5.Spara fil")
    print("6.exit")
    val = ''
    val = int(input(val),10)
    if val == 1:
        module.ReadFileMeny('./hej/personer.csv')
        meny()
    elif val == 2:
        visa = module.VisaJsonData('personer.json')
        print(visa)
        meny()        
    elif val == 3:
        module.CreateHuman()
        meny()
    elif val == 4:
        module.RemoveHuman()
        meny()
    elif val == 5:
        module.SparaHuman('personer.json')
        meny()


meny()
