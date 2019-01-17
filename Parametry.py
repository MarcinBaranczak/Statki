# ----- parametry programu -----
class Parametry:
    __tabWielkosc = 10  # wielkość tablicy do gry - NETTO
    __ileJedno = 4  # ilość jednomasztowców
    __ileDwu = 3  # ilość dwumasztowców
    __ileTrzy = 2  # ilość trzymasztowców
    __ileCztero = 1  # ilość czteromasztowców

    def getIleCztero(self):
        return self.__ileCztero

    def getIleTrzy(self):
        return self.__ileTrzy

    def getIleDwu(self):
        return self.__ileDwu

    def getIleJedno(self):
        return self.__ileJedno

    def getTabWielkosc(self):
        return self.__tabWielkosc
# endClass
