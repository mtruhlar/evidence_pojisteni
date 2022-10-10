from akce import *
from pojistenci import *
import os

print("""
----------------------------------
EVIDENCE POJISTENYCH
----------------------------------
""")

vyber_akce = True
while vyber_akce:
    print(akce)
    vyberte_operaci = kontrola("Zadejte cislo akce: ", "Zadejte prosim cislo 1 az 6. ")
    os.system('cls')
    if vyberte_operaci == 1:
        pokracuj = True
        while pokracuj:
            evidence_pojistenych()
            pokracuj = False

    elif vyberte_operaci == 2:
        if overeni_prazdneho_pole():
            for seznam in seznam_pojistenych:
                print(seznam.__str__())

    elif vyberte_operaci == 3:
        if overeni_prazdneho_pole():
            hledani_pojistenych()

    elif vyberte_operaci == 4:
        if overeni_prazdneho_pole():
            editace_pojistenych()

    elif vyberte_operaci == 5:
        if overeni_prazdneho_pole():
            smazani_pojistenych()

    elif vyberte_operaci == 6:
        vyber_akce = False
        input("Program byl ukoncen. Stisknete libovolnou klavesu...")

    else:
        print("Zadejte prosim cislo 1 az 6. ")
        
        

