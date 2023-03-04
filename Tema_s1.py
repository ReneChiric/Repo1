# I. Exercitii obligatorii
# 1. # O variabila este o adresa de memorie in care se pot stoca informatii

# 2. declara si initializeaza cate o variabila
nume_elev = 'Andrei' # String
nota_elev = 10 # integer
apt_sport = True #boolean
medie_generala = 9.14 # float


# 3. Functia type
print(type(nume_elev))
print(type(nota_elev))
print(type(apt_sport))
print(type(medie_generala))

# 4. Rotunjire float cu functia round

print(round(medie_generala))

# suprascriere
medie_generala = round(medie_generala)
print(medie_generala)

# 5. 4 propozitii folosind print si fiecare variabila

print(f' Numele elevului este: {nume_elev}')
print(f' Nota elevului este: {nota_elev}')
print(f' Elevul este apt pentru sport: {apt_sport}')
print(f' Media generala rotunjita a elevului este: {medie_generala}')

# 6. Citeste de la tastatura
numele = input("Va rugam introduceti numele dvs")
prenumele = input("Va rugam introduceti prenumele dvs")
print(f'Numele complet are {len(numele + prenumele)} caractere')

# 7. Citeste de la tastatura
lungimea = int(input("va rugam sa introduceti lungimea"))
latimea = int(input("va rugam sa introduceti latimea"))
print(f'Aria dreptunghiului este {lungimea * latimea}')


# 8. Avand stringul : "Coral is either the stupidest animal or the smartest rock"

text = "Coral is either the stupidest animal or the smartest rock"
print(text.count(" the "))

# 9. Inlocuieste cuvantul "the" cu cuvantul "THE"
print(text.replace(" the ", " THE "))


# 10. Folositi assert ca sa verificati daca string-ul contine doar numere
assert text.isdigit() == False, "Textul nu contine doar numere"
print (f' Textul nu contine doar numere')