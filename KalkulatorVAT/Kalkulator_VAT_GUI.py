from tkinter import *

class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # tekst powitania
        self.etykieta = Label(self, text = "Witaj w programie liczącym kwotę podatku VAT!", font= 'arial 16')
        self.etykieta.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # etykieta do wprowadzanego tekstu
        self.pw_lbl = Label(self, text="Wprowadź kwotę brutto:", font= 'arial 14')
        self.pw_lbl.grid(row=3, column=0, sticky=W)

        # widżet do przyjęcia kwoty
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=3, column=1, sticky=W)

        # przycisk akceptuj
        self.przycisk_akceptacji = Button(self, text = "Oblicz", font='arial 15', command = self.reveal)
        self.przycisk_akceptacji.grid(row = 4, column = 0, sticky = W)

        # pole do wyświetlenia komunikatu
        self.kwota = Text(self, width=35, height = 5, wrap = WORD, font= 'arial 17')
        self.kwota.grid(row=5, column=0, columnspan = 2, sticky = W)

    def reveal(self):
        # wyświetl kwotę podatku VAT
        contents = self.pw_ent.get()
        contents = float(contents)
        message = round(((contents / 1.23) * 0.23), 2)

        self.kwota.delete(0.0, END)
        self.kwota.insert(0.0, message)


root = Tk()
root.title("Kalkulator VAT")
root.geometry("460x200")
app = Application(root)
root.mainloop()