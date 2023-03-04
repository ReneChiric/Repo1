## Tema obligatorie 2
'''
1. Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# if else - if else este un conditional folosit in cazul in care mai multe conditii sunt adevarate, pentru a "bifurca" codul

de exemplu:

if marul este specia golden = pretul este 20 de lei/kg
elif: marul este specia ionatan = pretul este 15 lei/kg


'''

'''  2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
 daca este numar intreg mai mare ca 0)
'''

x = (int(input(f'Va rugam introduceti un numar X din tastatura'))) #declaram si initializam variabila numar ca int
if x > 0: #conditionam prin "if" rezultatul, daca numarul introdus este mai mare ca 0 este un numar natural
    print(f'Numarul ales este numar natural (mai mare ca 0)')
else:
    print(f'Numarul ales nu este un numar natural')

'''
3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

'''

if x > 0: #conditionam cazul in care numarul introdus este pozitiv
    print(f'Numarul ales este numar pozitiv')
if x == 0: #conditionam cazul in care numarul introdus este neutru
        print(f'Numarul ales este numar neutru')
if x < 0: #conditionam cazul in care numarul introdus este negativ
        print(f'Numarul ales este numar negativ')

'''
4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval)
'''

if x >= -2 and x <= 13:
    print(f'Numarul introdus se afla in intervalul [-2..13]')
else:
    print(f'Numarul introdus nu se afla in intervalul [-2...13]')

'''
 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs

'''
y = int(input(f'Va rugam introduceti alt numar Y: ')) #declaram variabila int y si o citim de la tastatura
diferenta = abs(x-y) #declaram si initializam variabila diferenta, care afiseaza cate numere sunt intre valoarea lui x si lui y
print(f"Intre valorile lui x si y sunt {diferenta} numere")

'''6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
'''
if not x > 5 and x < 27: #inversam prin conditionarea cu if not valoarea de adevar a propozitiei
    print(f'Valoarea numarului ales NU este intre [5...27]')
else:
    print(f'Valoarea numarului ales este intre [5...27]')


'''
7. Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
daca nu, afiseaza care din ele este mai mare
'''

y = int(input('Va rugam introduceti o noua valoare pentru Y')) #declaram, initializam si suprascriem Y de la tastatura
if y == x:
    print(f"Valoarea lui 'Y' este egala cu valoarea lui 'X'")
elif y < x:
        print(f"Numarul mai mare este {x}")
else:
        print(f'Valoare lui y este mai mare decat valoarea lui {y}')


'''
8. Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).
'''

z = int(input('Va rugam introduceti un numar Z: '))
if z == x == y:
    print(f'Triunghiul este echilateral')
elif z == x or x == y or y == z:
    print(f'Triunghiul este isoscel')
else:
    print(f'Triunghiul este oarecare')

'''
9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
'''

litera = input('Va rugam introduceti o litera')
if(litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u' or litera == 'A' or litera == 'E' or litera == 'I' or litera == 'O' or litera == 'U'):
    print(f'Este vocala!')
else:
    print(f'Este consoana!')

'''
 10.   Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
'''

nota = float(input(f'Introduceti nota dvs'))
if nota > 9.01 and nota <10.01:
    print(f'Notatia in sistem american pentru nota dvs. este "A"')
if nota < 9 and nota > 8.01:
    print(f'Notatia in sistem american pentru nota dvs. este "B"')
if nota < 8 and nota > 7.01:
    print(f'Notatia in sistem american pentru nota dvs. este "C"')
if nota < 7 and nota > 6.01:
    print(f'Notatia in sistem american pentru nota dvs. este "D"')
if nota < 6 and nota > 5.01:
    print(f'Notatia in sistem american pentru nota dvs. este "E"')
if nota < 5 and nota > 1:
    print(f'Notatia in sistem american pentru nota dvs. este "F"')
elif nota > 10.01:
    print(f'Nu exista nota mai mare decat 10. ')
else:
    print(f"Va rugam introduceti o nota cuprinsa in sistemul de notare")