# Gracz wybiera liczbe z przedzialu 1-100, a komputer stara się odgadnać jaka to liczba :)


print("Witaj użytkowniku. Po podaniu przez Ciebie liczby komputer postara się ją odgadnąć, może mu się uda :)")

# Użytkownik wybiera liczbę

wybrana_liczba = input("\nWybierz liczbę z przedziału od 1 do 100: ")

# Zabezpiecznie przed wprowadzeniem innej wartości niż liczba lub liczby wyższej od 100

try:
    wybrana_liczba = int(wybrana_liczba)

except ValueError:
    print("Podana wartość musi być liczbą! :)")
    exit()

if wybrana_liczba >= 100:
    print("Wybrana liczba musi być z zakresu od 1 do 100! Nie umiesz się bawić, do widzenia.")

# Komputer filtruje informację i podaje wynik

y = wybrana_liczba
for x in range(1, 101):
    if x == y:
        print("Komputer zgadł! To było do przewidzenia, Twoja liczba to: ", x)

