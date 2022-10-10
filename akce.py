from pojistenci import *

akce = ("""
Vyberte akci: 
1 - Pridat noveho pojisteneho
2 - Vypsat vsechny pojistene
3 - Vyhledat pojisteneho
4 - Editace pojisteneho
5 - Smazani pojisteneho
6 - Ukoncit evidenci
""")

seznam_pojistenych = []

def overeni_prazdneho_pole():
    if len(seznam_pojistenych) <= 0:
        print("Seznam je prazdny. Nejsou pridani zadni pojistenci.")
        return False
    else:
        return True

def evidence_pojistenych():
    id_uzivatele = len(seznam_pojistenych) > 0 and seznam_pojistenych[len(seznam_pojistenych)-1].id_uzivatele + 1 or 1
    jmeno = input("Zadejte jmeno: ").title()
    prijmeni = input("Zadejte prijmeni: ").title()
    vek = kontrola("Zadejte vek: ", "Zadejte prosim ciselnou hodnotu. ")
    mobil = kontrola("Zadejte telefonni cislo: ", "Zadejte prosim cislo bez mezer. ")
    seznam_pojistenych.append(Pojistenci(id_uzivatele, jmeno, prijmeni, vek, mobil))
    print("\nUlozeno.")

def hledani_pojistenych():
    hledane_jmeno = input("Hledane jmeno: ").title()
    hledane_prijmeni = input("Hledane prijmeni: ").title()
    vysledky = []
    for seznam in seznam_pojistenych:
        if seznam.jmeno == hledane_jmeno and seznam.prijmeni == hledane_prijmeni:
            vysledky.append(seznam)
    if (len(vysledky)>0):
        for vysledek in vysledky:
            print(vysledek.__str__())
    else:
        print(f"Zadny zaznam nenalezen. Zadali jste {hledane_jmeno} {hledane_prijmeni}. ")

def editace_pojistenych():
    editace_id = kontrola("Pro upravu udaju zadejte ID pojisteneho: ", "Zadejte prosim cislo. ")
    editovano = False
    for item in seznam_pojistenych:
        if item.id_uzivatele == editace_id:
            item.jmeno = input("Zadejte nove jmeno: ").title()
            item.prijmeni = input("Zadejte nove prijmeni: ").title()
            item.vek = kontrola("Zadejte vek: ", "Zadejte prosim ciselnou hodnotu. ")
            item.mobil = kontrola("Zadejte telefonni cislo: ", "Zadejte prosim cislo bez mezer. ")
            print("Udaje byly zmeneny. ")
            editovano = True
    if not editovano:
        print("Zadane ID neexistuje. ")

def smazani_pojistenych():
    hledane_id = kontrola("Zadejte ID pojistence: ", "Zadejte prosim cislo. ")
    smazano = False
    for item in seznam_pojistenych:
        if item.id_uzivatele == hledane_id:
            seznam_pojistenych.remove(item)
            print("Pojistenec byl smazan. ")
            smazano = True    
    if not smazano:
        print("Zadane ID neexistuje. ")
                
def kontrola(zadani, chyba):
    while True:
        try:
            cislo = int(input(zadani))
        except ValueError:
            print(chyba)
        else:
            return cislo