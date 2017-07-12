# Program Kalkulator VAT oblicza stawkę podatku w podanej kwocie



def netto():
    netto_input = float(input("Podaj kwotę Netto: "))
    netto_vat = float((netto_input * 0.23) + netto_input)
    sam_vat_netto = float(netto_input * 0.23)
    print("\nKwota z podatkiem wynosi:", netto_vat, "PLN")
    print("Podatek vat wynosi: ", sam_vat_netto)

def brutto():
    brutto_input = float(input("Podaj kwotę Brutto: "))
    vat_brutto = float(((brutto_input / 1.23) * 0.23))
    kwota_netto = float(brutto_input - vat_brutto)
    print("\nPodatek vat od kwoty ", brutto_input, "wynosi: ", vat_brutto, "PLN")
    print("Wartość netto dla kwoty", brutto_input, "wynosi: ", kwota_netto)

print("Witam w programie do liczenie podatku VAT, wybierz jaką kwotę chcesz policzyć:")

choice = None

while choice != "0":
    print(
        """
        0 - Zakończ
        1 - Netto
        2 - Brutto
        """
        )
    choice = input("Wybierz: ")
    print()

    if choice == "0":
        print("Do widzenia! :)")

    elif choice == "1":
        netto()

    elif choice == "2":
        brutto()

input("Aby zakończyć naciśnij Enter")
