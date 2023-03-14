# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

from abc import ABC, abstractmethod


class FormaGeometrica(ABC):


    @property
    def pi(self):
        pi = 3.14



    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print(f'Cel mai probabil am colturi')



# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
#
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)


class Patrat(FormaGeometrica, ABC):
    __latura = None

    def __init__(self, __latura):
        self.__latura = __latura


    def get_latura(self, __latura):
        print(f'Latura este {self.__latura}')
        return self.__latura



    def set_latura(self, latura):
        print(f'Noua dimensiune a laturii este : {latura}')
        self.__latura = latura


    def delete_latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None


    def aria(self):
        aria = self.__latura * self.__latura
        print(f'Aria este {aria}')

FormaGeometrica.descrie(ABC)
Patrat.descrie(ABC)
Patrat.set_latura(ABC, 9)
Patrat.get_latura(ABC, "")
Patrat.delete_latura(ABC)
Patrat.get_latura(ABC, "")
Patrat.set_latura(ABC, 7)
Patrat.aria(ABC)



# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)



class Cerc(FormaGeometrica, ABC):
    __raza = None

    def __init__(self, __raza):
        self.__raza = __raza

    def get_raza(self, __raza):
        print(f'Raza este {self.__raza}')
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza



    def delete_raza(self):
        self.__raza = None

    def aria(self):
        aria = self.pi * (self.__raza ** 2)
        print(f'Aria cercului este {aria}')


    def descrie(self):
        print(f'Cel mai probabil nu am colturi')

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui



Cerc.set_raza(FormaGeometrica, 6)
Cerc.get_raza(FormaGeometrica, "")
Cerc.delete_raza(ABC, )
Cerc.descrie(ABC)
Cerc.get_raza(ABC, "")
Cerc.set_raza(ABC, "9")
Cerc.get_raza(ABC, "")
# Cerc.aria(FormaGeometrica) # aici nu am stiut cum sa fac sa mearga aria pt cerc

Cerc.descrie(FormaGeometrica)


cerc1 = Cerc(6)
cerc1.descrie()
cerc1.set_raza(4)
cerc1.get_raza(Cerc)
cerc1.delete_raza()
cerc1.get_raza(Cerc)


patrat1 = Patrat(9)
patrat1.set_latura(5)
patrat1.get_latura(Patrat)
patrat1.aria()
