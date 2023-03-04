import random



dice_roll = (random.randint(0,6))
y = int(input(f'Va rugam introduceti un numar de la 0 la 6'))
if y < 1:
    print(f'Va rugam introduceti un numar de la 0 la 6')
elif y > 6:
    print(f'Va rugam introduceti un numar de la 0 la 6')
else:
    print(f'Numarul introdus este {y}')

if y == dice_roll:
    print(f'Ai ghicit numarul! Numarul tau a fost {y}, iar numarul zarului {dice_roll}!')
elif y < dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {y} dar a fost {dice_roll}')
else:
    print(f'Ai castigat. Ai pierdut. Ai ales un numar mai mare. Ai ales {y} dar a fost {dice_roll}')