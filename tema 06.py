# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    raza = 6
    culoare = "verde"


#constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f'Raza cercului este {self.raza}, iar culoarea este {self.culoare}')


    def aria(self):
        aria = raza ** 2 * pi
        print(f'aria cercului este {self.aria}')
        pi = 3.14

    def diametru(self,):
        diametru = raza * 2
        return diametru
        print(f'Diametrul cercului este {self.diametru}')


    def circumferinta(self, circumferinta):
        circumferinta = pi * diametru
        return circumferinta
        print(f'Circumferinta cercului este {self.circumferinta}')



cerc = Cerc(12, "albastru")
cerc.descrie_cerc()

