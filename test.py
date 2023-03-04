


#
# def pozitive(numere):
#     for numar in numere:
#         if numar < 0:
#             numere.remove(numar)
#             print(numere)
#
#
#
#
# numere = [5, 7, 3, 9, 3, 3, -1, 0, -4, 3]
#
# pozitive(numere)




# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False





def scoate(setul):
    if numar not in setul:
        print(f'Am adaugat numarul nou in set')
        setul.add(numar)
        return True
    if numar in setul:
        print(f'nu am adaugat numarul in set. Acesta exista deja')
    return False


numar = int(input(f'Introdu un numar'))



setul = {1, 3, 5, 6, 12, 20}


print(scoate(setul))


class Cerc:
    raza = 6
    culoare = "verde"


    def descrie_cerc(self):

