from functions import *
repeat = True
Welkom()
Zakelijk = IsKlantZakelijk()
if Zakelijk == True:
        aantal = ZakelijkBolletjes()
        aantallen['liter'] += aantal
        smaken(aantal, Zakelijk)
        BonnetjeZakelijk()
        totZiens()
else:
        while repeat == True:
                aantal = Bolletjes()
                aantallen["bolletje"] += aantal
                smaken(aantal, Zakelijk)
                verpakking = Verpakking(aantal)
                aantallen[verpakking] += 1
                toppings(aantal, verpakking)

                if verpakking == "hoorntje":
                        print("U krijgt een hoorntje met "+str(aantal)+" bolletje(s)")
                elif verpakking == "bakje":
                        print("U krijgt een bakje met "+str(aantal)+" bolletje(s)")
                repeat = NogEenKeer()

        Bonnetje(aantallen, smakenaantal, toppingaantal, Zakelijk)
        totZiens()
