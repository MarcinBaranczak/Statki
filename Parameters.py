# ----- parametry programu -----
class Parameters:
    __tabSize = 10  # wielkość tablicy do gry - NETTO
    __countOne = 4  # ilość jednomasztowców
    __countTwo = 3  # ilość dwumasztowców
    __countThree = 2  # ilość trzymasztowców
    __countFour = 1  # ilość czteromasztowców

    def getCountFour(self):
        return self.__countFour

    def getCountThree(self):
        return self.__countThree

    def getCountTwo(self):
        return self.__countTwo

    def getCountOne(self):
        return self.__countOne

    def getTabSize(self):
        return self.__tabSize + 2
# endClass


if __name__ == "__main__":
    main()