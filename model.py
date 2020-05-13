import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "+"
PONOVLJENA_CRKA = "O"
NAPACNA_CRKA = "-"

ZMAGA = "W"
PORAZ= "X"

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(crka in self.crke for crka in self.geslo)

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def pravilni_del_gesla(self):
        delni=""
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + " "
            else:
                delni += "_ "
        return delni[:-1]
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, ugib):
        crka = ugib.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA

with open("C:\\Users\\Timotej\\GIT\\vislice\\besede.txt", "r", encoding="utf_8") as datoteka:
    bazen_besed = [vrstica.strip().upper() for vrstica in datoteka]

def nova_igra():
    return Igra(random.choice(bazen_besed))