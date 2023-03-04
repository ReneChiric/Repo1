'''
1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea dacaor jcuatul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vr sa ieml schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python”
'''


lista_jucatori_teren = ['Xavi', 'Iniesta', 'Messi', 'David Villa', 'Ronaldinho']
lista_jucatori_rezerva = ['Ronaldo', 'Hagi', 'Cristiano Ronaldo', 'Rivaldo', 'Adi Mutu']
lista_jucatori_scosi = []
schimbari_max = 3


schimbare = input(f' Introdu jucatorul pe care il vrei in teren din urmatorii: {lista_jucatori_rezerva}')
schimbare_scos = input(f'Specifica pe cine scoti din teren din urmatorii: {lista_jucatori_teren}')
if schimbare_scos not in lista_jucatori_teren:
    print(f'nu se poate efectua schimbarea deoarece jucatorul x nu e in teren')
assert schimbare_scos in lista_jucatori_teren, "Incearca sa introduci un datele corect"
assert schimbare in lista_jucatori_rezerva, "Incearca sa introduci datele corect"
if schimbare in lista_jucatori_rezerva and schimbare_scos in lista_jucatori_teren:
    print(f'Ai ales corect!')

    print(f'A iesit {schimbare_scos} si intra {schimbare}')
    print(f'Mai aveti {schimbari_max - 1} schimbari')
    lista_jucatori_teren.remove(schimbare_scos)
    lista_jucatori_scosi.append(schimbare_scos)
    lista_jucatori_teren.append(schimbare)
    lista_jucatori_rezerva.remove(schimbare)
    print(f' Joci in teren acum cu: {lista_jucatori_teren}')
    print(f' Ii mai ai ca rezerve pe: {lista_jucatori_rezerva}')
    print(f' Ai scos pe : {lista_jucatori_scosi}')

schimbarex = input(f'Doresti sa efectuezi o noua schimbare? Raspunde cu da/nu! *Orice alt raspuns inafara de da duce automat la inchierea meciului')

assert schimbarex == "da", "Meciul s-a terminat!"


schimbare2 = input(f' Introdu jucatorul pe care il vrei in teren din urmatorii: {lista_jucatori_rezerva}')
schimbare_scos2 = input(f'Specifica pe cine scoti din teren din urmatorii: {lista_jucatori_teren}')
assert schimbare2 in lista_jucatori_rezerva, "Incearca sa introduci datele corect"
assert schimbare_scos2 in lista_jucatori_teren, "Incearca sa introduci un datele corect"

if schimbare_scos2 not in lista_jucatori_teren:
    print(f'nu se poate efectua schimbarea deoarece jucatorul x nu e in teren')
assert schimbare_scos2 in lista_jucatori_teren, "Incearca sa introduci un datele corect"
if schimbare2 in lista_jucatori_rezerva and schimbare_scos2 in lista_jucatori_teren:
    print(f'Ai ales corect!')
    print(f'A iesit {schimbare_scos2} si intra {schimbare2}')
    print(f'Mai aveti {schimbari_max - 2} schimbari')
    lista_jucatori_teren.remove(schimbare_scos2)
    lista_jucatori_scosi.append(schimbare_scos2)
    lista_jucatori_teren.append(schimbare2)
    lista_jucatori_rezerva.remove(schimbare2)
    print(f' Joci in teren acum cu: {lista_jucatori_teren}')
    print(f' Ii mai ai ca rezerve pe: {lista_jucatori_rezerva}')
    print(f' Ai scos pe : {lista_jucatori_scosi}')

schimbarey = input(f'Doresti sa efectuezi o noua schimbare? Raspunde cu da/nu! *Orice alt raspuns inafara de da duce automat la inchierea meciului')
assert schimbarey == "da", "Meciul s-a terminat!"


if schimbarey.lower() == "da":
    print(f'Te rugam continua cu introducerea datelor')


schimbare3 = input(f' Introdu jucatorul pe care il vrei in teren din urmatorii: {lista_jucatori_rezerva}')
schimbare_scos3 = input(f'Specifica pe cine scoti din teren din urmatorii: {lista_jucatori_teren}')
assert schimbare3 in lista_jucatori_rezerva, "Incearca sa introduci datele corect"
assert schimbare_scos3 in lista_jucatori_teren, "Incearca sa introduci un datele corect"
if schimbare_scos3 not in lista_jucatori_teren:
    print(f'nu se poate efectua schimbarea deoarece jucatorul x nu e in teren')
if schimbare3 in lista_jucatori_rezerva and schimbare_scos3 in lista_jucatori_teren:
    print(f'Ai ales corect!')
    print(f'A iesit {schimbare_scos3} si intra {schimbare3}')
    lista_jucatori_teren.remove(schimbare_scos3)
    lista_jucatori_scosi.append(schimbare_scos3)
    lista_jucatori_teren.append(schimbare3)
    lista_jucatori_rezerva.remove(schimbare3)
    print(f' Joci in teren acum cu: {lista_jucatori_teren}')
    print(f' Ii mai ai ca rezerve pe: {lista_jucatori_rezerva}')
    print(f' Ai scos pe : {lista_jucatori_scosi}')
    print(f'Nu mai aveti alte schimbari!')
    print(f'Meciul s-a terminat!')
