from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = prijs - (prijs * korting)
    kortingsprijs = format(kortingsprijs,".2f") # Dit om twee cijfers achter de komma te krijgen (opgezocht op internet)  
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs} euro.")
def inkomsten_totaal(inkomsten,btw):
    totaal=0
    for bedrag in inkomsten:
        totaal += bedrag
    btw_bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer
def laag_en_hoog(mijn_lijst):
    a = max(mijn_lijst)
    b = min(mijn_lijst)
    return a,b
def gemiddelde(mijn_lijst):
    a = sum(mijn_lijst)/len(mijn_lijst)
    a = format(a,".2f")
    return (f"De gemiddelde inkomsten deze week zijn {a} euro")
def meervoudig(invoer_lijst):
    a,b = laag_en_hoog(invoer_lijst)
    return a,b
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer







    



