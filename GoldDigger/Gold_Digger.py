# Gold Digger to program który pobiera cenę 1 uncji złota z wybranej strony internetowej i co 20 minut zwraca ją użytkownikowi.


def main():
    from bs4 import BeautifulSoup
    import requests
    import time

    strona_zrodlowa = requests.get('https://mennicakapitalowa.pl/product-pol-201-Sztabki-zlota-CertiCard-1-uncja-24h.html').text

    soup = BeautifulSoup(strona_zrodlowa, "lxml")

    cala_strona = soup.find("strong", class_="projector_price_value")

    sama_cena = cala_strona.text

    print(sama_cena)

    time.sleep(60 * 20)
    main().refresh()

main()
