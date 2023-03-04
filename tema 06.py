# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    raza = None
    culoare = None

    #constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def aria(self):
        pi  = 3.14
        aria = self.raza ** 2 * pi
        print(f'Aria cercului este {aria}')
        return aria




    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza} cm, iar culoarea este {self.culoare}')





    def diametru(self):
        diametru = self.raza * 2
        print(f'Diametrul cercului este {diametru}')
        return diametru



    def circumferinta(self):
        pi = 3.14
        circumferinta = 2 * pi * self.raza
        print(f'Circumferinta cercului este {circumferinta}')
        return circumferinta




cerc = Cerc(6, "Verde")


cerc.descrie_cerc()
cerc.aria()
cerc.circumferinta()
cerc.diametru()


# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
#
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None


    #constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare


    def descrie(self):
        print(f'Lungimea dreptunghiului este: {self.lungime}')
        print(f'Latimea dreptunghiului este: {self.latime}')
        print(f'Culoarea dreptunghiului este: {self.culoare}')

    def aria(self):
        aria = self.lungime * self.latime
        print(f'Aria dreptunghiului este: {aria}')
        return aria

    def perimetrul(self):
        perimetrul = 2 * (self.lungime + self.latime)
        print(f'Perimetrul dreptunghiului este {perimetrul}')
        return perimetrul

    def schimba_culoarea(self, noua_culoare):
        noua_culoare = input(f'Va rugam introduceti o noua culoare')
        self.culoare = noua_culoare #suprascriere atribut/field



dreptunghi1 = Dreptunghi(6, 3, "Rosu")

dreptunghi1.descrie()
dreptunghi1.aria()
dreptunghi1.perimetrul()

dreptunghi1.schimba_culoarea("Verde")
dreptunghi1.descrie()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)

class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu


    def descrie(self):
        print(f'Nume: {self.nume}')
        print(f'Prenume: {self.prenume}')
        print(f'Salariu: {self.salariu}')

    def nume_complet(self):
        print(f'Numele complet este {self.nume}  {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul lunar este {self.salariu}')


    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariul anual este: {salariu_anual}')
        return salariu_anual

    def marire_salariu(self):
        marire_salariu_procent = int(input(f'Va rugam introduceti procentul maririi de salariu'))
        salariu_lunar = self.salariu + (marire_salariu_procent / 100 * self.salariu)
        print(f'Noul salariu lunar este: {salariu_lunar}')
        return marire_salariu_procent


angajat1 = Angajat("Chiric", "Rene-Adrian", 6000)
angajat1.descrie()
angajat1.nume_complet()
angajat1.salariu_lunar()
angajat1.salariu_anual()
angajat1.marire_salariu()


# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None


    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in cont suma de {self.sold}')


    def debitare_cont(self):
        debitare_cont = int(input(f'Va rugam introduceti suma de debitat'))
        self.sold = self.sold - debitare_cont
        print(f'Noul sold este {self.sold}')


    def creditare_cont(self):
        creditare_cont = int(input(f'Va rugam introduceti suma de creditat'))
        self.sold = self.sold + creditare_cont
        print(f'Noul sold este {self.sold}')


client = Cont(1232145123, "Chiric Rene-Adrian", 4000)
client.afisare_sold()
client.debitare_cont()
client.creditare_cont()

