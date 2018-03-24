from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # tekst powitania
        self.etykieta = Label(self, text = "Witaj w programie liczącym kwoty podatku VAT!")
        self.etykieta.grid(row = 0, column = 1, columnspan = 2, sticky = W)

        # etykieta do wprowadzanego tekstu
        self.pw_lbl = Label(self, text="Wprowadź kwotę brutto: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        # widżet do przyjęcia kwoty
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        # przycisk akceptuj
        self.przycisk_akceptacji = Button(self, text = "Oblicz", command = self.reveal)
        self.przycisk_akceptacji.grid(row = 2, column = 0, sticky = W)

        # pole do wyświetlenia komunikatu
        self.kwota = Text(self, width = 35, height = 5, wrap = WORD)
        self.kwota.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def brutto():
        brutto_input = float(input("Podaj kwotę Brutto: "))
        vat_brutto = float(((brutto_input / 1.23) * 0.23))
        kwota_netto = float(brutto_input - vat_brutto)
        print("\nPodatek vat od kwoty ", round(brutto_input, 2), "wynosi: ", round(vat_brutto, 2), "PLN")
        print("Wartość netto dla kwoty", round(brutto_input, 2), "wynosi: ", round(kwota_netto, 2))

    def reveal(self):
        # wyświetl kwotę podatku VAT
        contents = self.pw_ent.get()
        contents = float(contents)
        message = round(((contents / 1.23) * 0.23), 2)

        self.kwota.delete(0.0, END)
        self.kwota.insert(0.0, message)


root = Tk()
root.title("Kalkulator VAT")
root.geometry("500x300")
app = Application(root)
root.mainloop()