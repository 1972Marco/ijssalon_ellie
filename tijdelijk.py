from helper import decoreer

def print_aanbieding(): 
    prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
    }
    aanbieding = prijzen["vanille"] * 0.8
    reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}"
    reclame_tekst2 = reclame_tekst[:62] # aanbieding heeft de waarde 3.2 en heeft geen nullen achter de komma gegeven bij mij.
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split(" ")
    for el in reclame_tekst4:
        lengte = len(el)
        if lengte<5:
            print(el.lower())
        else:
            print(el)

decoreer ("Aanbieding")
print_aanbieding()




