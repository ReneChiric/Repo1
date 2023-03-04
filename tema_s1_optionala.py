# # # Tema optionala
# #
# # # 1. Citeste de la tastatura un string de dimensiune impara
# # # - afiseaza caracterul din mijloc
# #
#
# ## La acest exercitiu am avut nevoie de Google, nu l-am rezolvat complet deoarece nu am reusit sa returnez o eroare la introducerea unui cuvant par, folosind operatorii if/else
#
def middle_char(txt):
  return txt[(len(txt)-1)//2]
text = input("va rugam introduceti un cuvant impar")
print("Cuvantul ales este ",text)
print("Litera din mijloc este:  ",middle_char(text))
#
#
#    #2. Folosind un assert verifica daca un string e palindrom
#
text2 = input('Introduceti un cuvant')
#    #cuvantul scris normal este text2 = [:]
#    #cuvantul scris invers este text2 = [::-1]
#
palindrom = text2[:] == text2[::-1]
assert palindrom == True, "Cuvantul nu este un palindrom!"
#
#   #3.  Folosind o singură linie de cod :
# # - citește un string de la tastatură (ex: 'alabala portocala');
# # - salvează fiecare cuvânt într-o variabilă;
# # - printează ambele variabile pentru verificare.

cuvant1, cuvant2 = input("Va rugam introduceti doua cuvinte cu spatiu intre ele").split()
print(f'Primul cuvant este: {cuvant1}, iar cel de-al doilea este {cuvant2}')


## 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.
text3 = input("Va rugam introduceti textul: ")
primul_caracter = text3[0]
print(primul_caracter)
al_doilea_caracter = text3[1]
print(al_doilea_caracter)
fara_primul_si_ultimul = text3[1:-1]
print(fara_primul_si_ultimul)
fara_primul_si_ultimul = fara_primul_si_ultimul.replace(primul_caracter, primul_caracter.upper())
text_nou = primul_caracter + al_doilea_caracter + fara_primul_si_ultimul
print(text_nou)

##5. - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input('Introduceti numele utilizatorului')
parola = input('Introduceti parola')
dimensiune_parola = len(parola) * "*"
print(f' Parola pt. user {user} este {dimensiune_parola} si are {len(parola)} caractere')