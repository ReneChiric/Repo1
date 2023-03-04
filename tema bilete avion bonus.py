'''
Vrem sa cream o aplicatie pentru achizitionare bilete de avion care sa primeasca drept
inputuri urmatoarele informatii:
a. Varsta
b. Insotit de mama
c. Insotit de tata
d. Pasaport
e. Act permisiune mama
f. Act permisiune tata
Conditii de imbarcare:
1. Daca pers are varsta peste 18 ani si are pasaport
2. Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
3. Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte
si are permisiune in scris de la celalat parinte

'''

varsta = int(input(f'Va rugam introduceti varsta dvs'))
insotit_mama = input(f' 1. Sunteti insotit de mama? Raspundeti cu Da/Nu.')
insotit_tata = input(f' 2. Sunteti insotit de tata? Raspundeti cu Da/nu.')
pasaport = input(f' 3. Aveti pasaport? Raspundeti cu da/nu.')
act_mama = input(f' 4. Aveti permisiunea mamei? Raspundeti cu Da/nu.')
act_tata = input(f' 5. Aveti permisiunea tatalui? Raspundeti cu Da/nu.')

#eliminare posibilate raspuns gresit si convertire in case insensitive
if insotit_mama.lower() != ("da" or "nu"):
    print(f' 1. Va rugam raspundeti cu da/nu.')
elif insotit_tata.lower() != ("da" or "nu"):
    print(f' 2. Va rugam raspundeti cu da/nu.')
elif pasaport.lower() != ("da" or "nu"):
    print(f' 3. Va rugam raspundeti cu da/nu.')
elif act_mama.lower() != ("da" or "nu"):
    print(f' 4. Va rugam raspundeti cu da/nu.')
elif act_tata.lower() != ("da" or "nu"):
    print(f' 5. Va rugam raspundeti cu da/nu.')
else:
    print(f' Felicitari! Ati introdus datele corect!')



#Conditiile imbarcarii
if varsta >= 18 and pasaport.lower() == "da":
    print(f'Va puteti imbarca la bordul aeronavei!')
elif pasaport.lower() == "nu":
    print(f'Unde pleci fara pasaport???')
elif varsta < 18 and pasaport.lower() == ("da") and insotit_mama.lower() == ("da") and insotit_tata.lower() == ("da"):
    print(f'Va puteti imbarca la bordul aeronavei!')
elif varsta < 18 and pasaport.lower() == ("da") and insotit_mama.lower() == ("da") and act_tata.lower() == ("da"):
    print(f'Va puteti imbarca la bordul aeronavei!')
elif varsta < 18 and pasaport.lower() == ("da") and insotit_tata.lower() == ("da") and act_mama.lower() == ("da"):
    print(f'Va puteti imbarca la bordul aeronavei!')
elif varsta < 18 and pasaport.lower() == "da" and (insotit_mama.lower() == "nu" or insotit_tata.lower() == "nu") and act_mama.lower() == "nu" and act_tata.lower() == "nu":
    print(f'Nu va puteti imbarca fara minim unul din parinti sau fara acceptul celuilalt!')
elif varsta < 18 and pasaport.lower() == "da" and insotit_mama.lower() == "nu" and insotit_tata.lower() == "nu":
    print (f'Ce cauti singur pe aeroport??')
