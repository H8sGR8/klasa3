from tkinter import Tk, Label, Button, Entry, END, IntVar
from random import randint

class Gierka:

    def __init__(self, master):

        self.master = master
        master.title("Losowanie gierka")

        self.losuj = randint(1, 100)

        self.total = 0

        self.total_label_text = IntVar()
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.total_label.grid(row=1, column=1)
        self.proby_ = Label(master, text="ilosc prob")
        self.proby_.grid(row=1, column=0)

        self.przedział = Label(master, text="podaj liczbe od 1 do 100")
        self.przedział.grid(row=2, column=0)

        self.entry = Entry(master)
        self.entry.grid(row=3, column=0)

        self.przycisk_sprwadz = Button(master, text="sprawdz", command=self.klikniecie)
        self.przycisk_sprwadz.grid(row=4, column=0)

        self.label2 = Label(text=" ")
        self.label2.grid(row=5, column=0)

        self.label2 = Label(text=" ")
        self.label2.grid(row=7, column=0)

        self.przycisk_losuj = Button(master, text="losuj od nowa", command=self.losowanie)
        self.przycisk_losuj.grid(row=6, column=0)

    def losowanie(self):
        self.total = 0
        self.total_label_text.set(self.total)
        self.losuj = randint(1, 100)
        self.label2 = Label(text="                                  ")

    def klikniecie(self):
        self.total += 1
        self.label2 = Label(text="                                  ")
        self.label2.grid(row=5, column=0)
        self.podaj = int(self.entry.get())

        if (self.podaj >= 1 and self.podaj <= 100):
            if (self.losuj > self.podaj):
                self.label2 = Label(text="za malo")
                self.label2.grid(row=5, column=0)
            elif (self.losuj < self.podaj):
                self.label2 = Label(text="za duzo")
                self.label2.grid(row=5, column=0)
            elif (self.losuj == self.podaj):
                self.label2 = Label(text="wygrales")
                self.label2.grid(row=5, column=0)
        else:
            self.label2 = Label(text="cos nie tak")
            self.label2.grid(row=5, column=0)
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

gra = Tk()
losowanko = Gierka(gra)
gra.mainloop()