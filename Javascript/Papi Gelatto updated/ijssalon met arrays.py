# Defineer prijzen als een dictionary
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

# Initializeer de aantallen als een dictionary
aantallen = {
    "hoorntje": 0,
    "bakje": 0,
    "bolletje": 0,
    "liter": 0,
}

# Defineer smakenaantal en toppingaantal als dictionaries
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

# Welkomstbericht functie
def Welkom():
    print("Welkom bij Papi Gelatto!")

# Functie om te controleren of de klant zakelijk is
def IsKlantZakelijk():
    repeat = True
    while repeat:
        try:
            pofz = input("Bent u 1) een particuliere klant of 2) een zakelijke klant? ").lower()
            if pofz == "1":
                Zakelijk = False
                break
            elif pofz == "2":
                Zakelijk = True
                break
            else:
                sorry()
        except:
            sorry()
    return Zakelijk

# Functie om het aantal bolletjes te vragen voor particuliere klanten
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

# Functie om het aantal liter ijs te vragen voor zakelijke klanten
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

# Functie om smaken bij te houden
def smaken(aantal:int, Zakelijk):
    if not Zakelijk:
        for a in range(1, aantal+1):
            while True:
                smaak = input(f"Welke smaak wilt u voor de {a}e bol? U kunt kiezen uit (a)ardbei, (c)hocolade en (v)anille ").lower()
                if smaak in ("a", "c", "v"):
                    smakenaantal[smaak] += 1
                    break
                else:
                    sorry()
    else:
        for a in range(1, aantal+1):
            while True:
                LiterSmaak = input(f"Welke smaak wilt u voor de {a}e liter? U kunt kiezen uit (a)ardbei, (c)hocolade en (v)anille ").lower()
                if LiterSmaak in ("a", "c", "v"):
                    smakenaantal["l" + LiterSmaak] += 1
                    break
                else:
                    sorry()

# Functie om toppings bij te houden
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

# Functie om de verpakking te kiezen
def Verpakking(nummer):
    doorgaan = True
    while doorgaan:
        if nummer <= 3:
            verpakking = input(f"Wilt u de {nummer} bolletje(s) in een hoorntje of bakje? ")
            if verpakking in ("hoorntje", "bakje"):
                doorgaan = False
            elif nummer > 8:
                tegroot()
            else:
                sorry()
        elif 3 < nummer < 9:
            verpakking = "bakje"
            doorgaan = False
        else:
            sorry()
            break
    return verpakking

# Functie om te vragen of de klant nog meer wil bestellen
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

# Functie om het bonnetje af te drukken voor particuliere klanten
def Bonnetje(aantallen, smakenaantal, toppingaantal, Zakelijk):
    # Logic om bonnetje af te drukken voor particuliere klanten
    pass

# Functie om het bonnetje af te drukken voor zakelijke klanten
def BonnetjeZakelijk():
    # Logic om bonnetje af te drukken voor zakelijke klanten
    pass

# Functie om afscheid te nemen van de klant
def totZiens():
    print("Bedankt voor het bestellen bij Papi Gelatto, Hopelijk tot ziens!")

# Het hoofdprogramma
def main():
    repeat = True
    Welkom()
    Zakelijk = IsKlantZakelijk()

    if Zakelijk:
        aantal = ZakelijkBolletjes()
        aantallen['liter'] += aantal
        smaken(aantal, Zakelijk)
        BonnetjeZakelijk()
        totZiens()
    else:
        while repeat:
            aantal = Bolletjes()
            aantallen["bolletje"] += aantal
            smaken(aantal, Zakelijk)
            verpakking = Verpakking(aantal)
            aantallen[verpakking] += 1
            toppings(aantal, verpakking)
            repeat = NogEenKeer()

        Bonnetje(aantallen, smakenaantal, toppingaantal, Zakelijk)
        totZiens()

if __name__ == "__main__":
    main()