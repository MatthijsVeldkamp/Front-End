from errors import *
#-------------------------------------------------
prijzen = {
    "hoorntje": 1.25,
    "bakje": 0.75,
    "bolletje": 0.95,
    "slagroom": 0.50,
    "sprinkels": 0.30,
    "caramelb": 0.90,
    "caramelh": 0.60,
    "liter": 9.80,
}


aantallen = {
    "hoorntje": 0,
    "bakje": 0,
    "bolletje": 0,
    "liter": 0,
}


smakenaantal = {
    "a": 0,
    "c": 0,
    "v": 0,
    "la": 0,
    "lc": 0,
    "lv": 0,
}

toppingaantal = {
    "a": 0,
    "b": 0,
    "c": 0,
    "db": 0,
    "dh": 0,
}
#-------------------------------------------------

def Bolletjes():
    doorgaan = True
    while doorgaan:
        try:
            nummer = int(input("Hoeveel bolletjes wilt u bestellen? "))
            if nummer > 8:
                tegroot()
            elif nummer <= 0:
                sorry()
            elif nummer in range(1,9):
                doorgaan = False
            else:
                sorry()
        except:
            sorry()
    return nummer

#-------------------------------------------------

def ZakelijkBolletjes():
    doorgaan = True
    while doorgaan:
        try:
            nummer = int(input("Hoeveel Liter ijs wilt u? "))
            if nummer > 8:
                tegroot()
            elif nummer <= 0:
                sorry()
            elif nummer in range(1,9):
                doorgaan = False
            else:
                sorry()
        except:
            sorry()
    return nummer

#-------------------------------------------------

def smaken(aantal:int, Zakelijk):
    if Zakelijk == False:
        for a in range(1, aantal+1):
            while True:
                smaak = input("Welke smaak wilt u voor de "+str(a)+"e bol? U kunt kiezen uit (a)ardbei, (c)hocolade en (v)anille ").lower()
                if smaak == "a":
                    smakenaantal["a"] += 1
                    break
                elif smaak == "c":
                    smakenaantal["c"] += 1
                    break
                elif smaak == "v":
                    smakenaantal["v"] += 1
                    break
                else:
                    sorry()
    else:
        for a in range(1, aantal+1):
            while True:
                LiterSmaak = input("Welke smaak wilt u voor de "+str(a)+"e liter? U kunt kiezen uit (a)ardbei, (c)hocolade en (v)anille ").lower()
                if LiterSmaak == "a":
                    smakenaantal["la"] += 1
                    break
                elif LiterSmaak == "c":
                    smakenaantal["lc"] += 1
                    break
                elif LiterSmaak == "v":
                    smakenaantal["lv"] += 1
                    break
                else:
                    sorry()
    return smakenaantal


# -------------------------------------------------
def toppings(aantal:int, verpakking):
        while True:
            topping = input("Welke topping wilt u? U kunt kiezen uit (a)geen, (b)slagroom, (c)sprinkels of (d)caramel saus ").lower()
            if topping == "a":
                toppingaantal["a"] += 1
                break
            elif topping == "b":
                toppingaantal["b"] += 1
                break
            elif topping == "c":
                toppingaantal["c"] += aantal
                break
            elif topping == "d" and verpakking == "bakje":
                toppingaantal["db"] += 1
                break
            elif topping == "d" and verpakking == "hoorntje":
                toppingaantal["dh"] += 1
                break
            else:
                sorry()

#--------------------------------------------------

def Verpakking(nummer):
    doorgaan = True
    while doorgaan:
        if nummer <= 3:
            verpakking = input(f"Wilt u de {nummer} bolletje(s) in een hoorntje of bakje? ")
            if verpakking == "hoorntje":
                doorgaan = False
            elif verpakking == "bakje":
                doorgaan = False
            elif nummer > 8:
                tegroot()
            else:
                sorry()
        elif nummer > 3 and nummer < 9:
            verpakking = "bakje"
            doorgaan = False
        else:
            sorry()
            break
    return verpakking

#-------------------------------------------------


def NogEenKeer():
    repeat = True
    while repeat:
        nogmeer = input("Wilt u nog meer bestellen? ")
        if nogmeer == "ja":
            repeat = True
            return repeat
        elif nogmeer == "nee":
            repeat = False
            return repeat
        else:
            sorry()

# -------------------------------------------------


def Bonnetje(aantallen, smakenaantal, toppingaantal, Zakelijk):
    aantal1 = 0
    aantal2 = 0
    aantal3 = 0
    aantal4 = 0
    aantal5 = 0
    aantal6 = 0
    aantal7 = 0
    print(smakenaantal)
    print(toppingaantal)
    print("=-=-=-=-=-=-=-=-[Papi Gelatto]-=-=-=-=-=-=-=-=")
    print("")
    if aantallen['bolletje'] >= 1:
        if smakenaantal['a'] >= 1:
            print(f" B.Aardbei      {smakenaantal['a']} X €0,95 = €{format(round(smakenaantal['a'] * prijzen['bolletje'],2), '.2f')}")
        if smakenaantal['c'] >= 1:
            print(f" B.Chocolade    {smakenaantal['c']} X €0,95 = €{format(round(smakenaantal['c'] * prijzen['bolletje'],2), '.2f')}")
        if smakenaantal['v'] >= 1:
            print(f" B.Vanille      {smakenaantal['v']} X €0,95 = €{format(round(smakenaantal['v'] * prijzen['bolletje'],2), '.2f')}")
        aantal1 = aantallen["bolletje"] * prijzen["bolletje"]


    if aantallen["hoorntje"] >= 1:
        print(f" Hoorntjes      {aantallen['hoorntje']} X €1,25 = €{format(round(aantallen['hoorntje'] * prijzen['hoorntje'],2), '.2f')}")
        aantal2 = aantallen["hoorntje"] * prijzen["hoorntje"]
    if aantallen["bakje"] >= 1:
        print(f" Bakjes         {aantallen['bakje']} X €0,75 = €{format(round(aantallen['bakje'] * prijzen['bakje'],2), '.2f')}")
        aantal3 = aantallen["bakje"] * prijzen["bakje"]


    if aantallen["bolletje"] >= 1:
        if toppingaantal["b"] >= 1:
            print(f" Topping        {toppingaantal['b']} X €0,50 = €{format(round(toppingaantal['b'] * prijzen['slagroom'],2), '.2f')}")
            aantal4 = toppingaantal['b'] * prijzen['slagroom']
        if toppingaantal["c"] >= 1:
            print(f" Topping        {toppingaantal['c']} X €0,30 = €{format(round(toppingaantal['c'] * prijzen['sprinkels'],2), '.2f')}")
            aantal5 = toppingaantal['c'] * prijzen['sprinkels']
        if toppingaantal['db'] >= 1:
            print(f" Topping        {toppingaantal['db']} X €0,90 = €{format(round(toppingaantal['db'] * prijzen['caramelb'],2), '.2f')}")
            aantal6 = toppingaantal['db'] * prijzen['caramelb']
        if toppingaantal['dh'] >= 1:
            print(f" Topping        {toppingaantal['dh']} X €0,60 = €{format(round(toppingaantal['dh'] * prijzen['caramelh'],2), '.2f')}")
            aantal7 = toppingaantal['dh'] * prijzen['caramelh']
    totaalbedrag = aantal1 + aantal2 + aantal3 + aantal4 + aantal5 + aantal6 + aantal7
    print(f"                           --------------- +")
    print(f"Het totale bedrag          = €{format(round(totaalbedrag,2), '.2f')}")
    print("=-=-=-=-=-=-=-=-[Papi Gelatto]-=-=-=-=-=-=-=-=")


#-------------------------------------------------

def BonnetjeZakelijk():
    print("=-=-=-=-=-=-=-=-[Papi Gelatto]-=-=-=-=-=-=-=-=")
    if aantallen['liter'] >= 1:
        if smakenaantal['la'] >= 1:
            print(f" L.Aardbei      {smakenaantal['la']} X €9,80 = €{format(round(smakenaantal['la'] * prijzen['liter'],2), '.2f')}")
        if smakenaantal['lc'] >= 1:
            print(f" L.Chocolade    {smakenaantal['lc']} X €9,80 = €{format(round(smakenaantal['lc'] * prijzen['liter'],2), '.2f')}")
        if smakenaantal['lm'] >= 1:
            print(f" L.Munt         {smakenaantal['lm']} X €9,80 = €{format(round(smakenaantal['lm'] * prijzen['liter'],2), '.2f')}")
        if smakenaantal['lv'] >= 1:
            print(f" L.Vanille      {smakenaantal['lv']} X €9,80 = €{format(round(smakenaantal['lv'] * prijzen['liter'],2), '.2f')}")
        aantal8 = aantallen['liter'] * prijzen['liter']
        print(f"                           --------------- +")
        totaalbedragZakelijk = aantal8
        print(f"Het totale bedrag          = €{format(round(totaalbedragZakelijk, 2), '.2f')}")
        print(f"BTW   (6%)                 = €{format(round(totaalbedragZakelijk/100*6, 2), '.2f')}")
        print("=-=-=-=-=-=-=-=-[Papi Gelatto]-=-=-=-=-=-=-=-=")


#-----------------------------------------------
def totZiens():
    print("Bedankt voor het bestellen bij Papi Gelatto, Hopelijk tot ziens!")
def Welkom():
    print("Welkom bij Papi Gelatto!")

#-------------------------------------------------

def IsKlantZakelijk():
    repeat = True
    while repeat == True:
        try:
            pofz = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ").lower()
            if pofz == "1":
                Zakelijk = False
                break
            if pofz == "2":
                Zakelijk = True
                break
            else:
                sorry()
        except:
            sorry()
    return Zakelijk