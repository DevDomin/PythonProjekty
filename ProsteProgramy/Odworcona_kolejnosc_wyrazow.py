# Program odwraca kolejność liter w słowie podanym przez użytkownika.

word = input("Wpisz coś kolego: ")

print(word + "?" "\nW języku arabskim będzie to wyglądało tak:")

high = len(word)
low = -len(word)
for i in word:
    while high != 0:
        high -= 1
        print(word[high], end= " ")

