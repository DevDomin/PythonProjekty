# Gold Digger to program który pobiera cenę 1 uncji złota z wybranej strony internetowej i zwraca ją użytkownikowi w postaci prostego GUI.

from tkinter import *


class GlowneOkno(Frame):

    def __init__(self, master):
        super(GlowneOkno, self).__init__(master)
        self.grid()
        self.dodatki_okna()


    def dodatki_okna(self):

        self.okno_wyniku = Text(self, width=35, height=5, wrap=WORD, font='arial 50')
        self.okno_wyniku.grid(row=3, column=0, columnspan=2, sticky=W)
        self.CenaZlota()

        self.tekst_powitania = Label(self, text="Aktualna cena 1 uncji złota:", font='arial 20', command=self.CenaZlota())
        self.tekst_powitania.grid(row=2, column=0, sticky=W)

    def CenaZlota(self):
        from bs4 import BeautifulSoup
        import requests
        strona_zrodlowa = requests.get(
            'https://mennicakapitalowa.pl/product-pol-201-Sztabki-zlota-CertiCard-1-uncja-24h.html').text
        soup = BeautifulSoup(strona_zrodlowa, "lxml")
        cala_strona = soup.find("strong", class_="projector_price_value")
        sama_cena = cala_strona.text
        print(sama_cena)
        message = sama_cena

        self.okno_wyniku.delete(0.0, END)
        self.okno_wyniku.insert(0.0, message)


root = Tk()
root.title("Gold digger")
root.geometry("350x180")
uruchom = GlowneOkno(root)
root.mainloop()