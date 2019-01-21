import numpy as np


# ----- tablica strzałów i obsługa -----
class Statki:

    tabA = np.array[0]

    def __init__(self, wielkosc):
        np.resize(self.tabA, wielkosc)


    def ustawTab(self):
#        for i in range(10):
#            self.tabA[i] = i



        print("def ustaw tab")
        for i in self.tabA:
            print (self.tabA[i])
            print(i," ")

# endClass
