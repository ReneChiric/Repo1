
# 1. Funcție care primește o lună din an și returnează câte zile are acea luna



def luna(**kwargs):
    for key, value in kwargs.items():
        if tastatura == key :
            print(f'Luna {key} are {value} zile')


dictionar_luni = {
    'ianuarie' : 31,
    'februarie' : 28,
    'martie' : 31,
    'aprilie' : 30,
    'mai' : 31,
    'iunie' : 30,
    'iulie' : 31,
    'august' : 31,
    'septembrie' : 30,
    'octombrie' : 31,
    'noiembrie' : 30,
    'decembrie' : 31
}

tastatura = input(f'Va rugam introduceti luna')


# print(f"Suma: {a}")
#     print("Diferenta: ", b)
#     print("Inmultirea: ", c)


luna(**dictionar_luni)

# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.

# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
#
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)


def calculatorul(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    print(f"Suma: {a}")
    print("Diferenta: ", b)
    print("Inmultirea: ", c)
    print("Impartirea: ", d)
    return a,b,c,d



print(calculatorul(10, 2))


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def cifre():



numere = [1, 3, 1, 5, 9, 7, 7, 5, 5]