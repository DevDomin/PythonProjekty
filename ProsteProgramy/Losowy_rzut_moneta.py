# Rzucamy moneta 100 razy, a program podaje nam ile razy wypadla reszka, a ile orzeł.

input("Program rzuci teraz moneta 100 razy. Naciśnij ENTER i trzymaj się:")

import random

# losuje z dwoch wartosci

kod = 0
kod2 = 0
licznik = 0

while True:
    licznik += 1

    rzut = random.randint(1, 2)

    if rzut == 1:    
        print("orzel")
        kod += 1
        
    elif rzut == 2:
        print("reszka")
        kod2 += 1

    if licznik == 100:
        break

print("Orłow wypadło: ", kod, "\nA reszek: ", kod2)

input("\nNacisnij ENTER aby sie pożegnać :)")
    
          

    
