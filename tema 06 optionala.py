# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
#
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000

from datetime import date


class Factura:
    seria = "Seria 123/ nr. 345"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc


    def schimba_cantitate(self):
        schimba_cantitate = int(input(f'Va rugam introduceti cantitatea'))
        self.cantitate = schimba_cantitate


    def schimba_pretul(self):
        schimba_pretul = int(input(f'Va rugam introduceti noul pret'))
        self.pret_buc = schimba_pretul



    def schimba_nume(self):
        schimba_nume = input(f'Va rugam introduceti noul nume')
        self.nume_produs = schimba_nume

    def genereaza_factura(self):
        calcul_factura = self.cantitate * self.pret_buc
        print(f'Factura {self.seria} \n'
              f'Data: {date.today()} \n'
              f'Produs     | Cantitate | Pret Bucata | TOTAL \n'
              f'{self.nume_produs}  | {self.cantitate}         | {self.pret_buc}        | {calcul_factura}')



iphone = Factura(13, "Iphone 13", 2, 5000)

iphone.genereaza_factura()
iphone.schimba_nume()
iphone.schimba_cantitate()
iphone.schimba_pretul()
iphone.genereaza_factura()

# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Masina:
    marca = 'Mercedes'
    model = None
    Viteza_max = None
    viteza_actuala = 0
    culoare = "Gri"
    culori_disp = {'Verde', 'Rosu', 'Gri', 'Albastru', 'Negru'}
    inmatriculata = False

    def __init__(self, model, viteza_max):
        self.model = model
        self.viteza_max = viteza_max


    def descrie(self):
        print(f'Marca: {self.marca} \n'
              f'Model: {self.model} \n'
              f'Viteza maxima: {self.viteza_max} \n'
              f'Viteza actuala: {self.viteza_actuala} \n'
              f'Culoare: {self.culoare} \n'
              f'Inmatriculata: {self.inmatriculata}')


    def inmatriculare(self):
        self.inmatriculata = True


    def vopseste(self):
        vopseste = input(f'Va rugam sa precizati ce culoare vreti pt. masina. Alegeti din lista urmatoare: {self.culori_disp}')


e220 = Masina('E220', 280)
e220.inmatriculare()
e220.descrie()










