from random import randint

class losowanie:
    def __init__(self):
        self.losuj = int(0)
        self.proby = int(0)
        self.podaj = int(0)
    def losowanie_liczby(self):
        self.losuj = randint(1,100)
    def zgadywanie(self):
        while(self.losuj != self.podaj):
            try:
                self.podaj = int(input("podaj liczbe od 1 do 100\n"))
                self.proby += 1
                if(self.podaj >= 1 and self.podaj <= 100):
                    if (self.losuj > self.podaj):
                        print("za mało")
                    elif (self.losuj < self.podaj):
                        print("za dużo")
                    elif (self.losuj == self.podaj):
                        print(f"wygrałes w {self.proby} proby")
                else:
                    print("cos nie tak")
            except Exception:
                print("cos nie tak")



gierka = losowanie()
gierka.losowanie_liczby()
gierka.zgadywanie()
