class Pojistenci:

    def __init__(self, id_uzivatele, jmeno, prijmeni, vek, mobil):
        self.id_uzivatele = id_uzivatele
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.mobil = mobil

    def __str__(self):
        return ("{:<2} {:<15} {:<15} {:<10} {:<}".format(self.id_uzivatele,self.jmeno,self.prijmeni,self.vek,self.mobil))
        