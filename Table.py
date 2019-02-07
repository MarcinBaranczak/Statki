import random

class Table:
    def __init__(self, maxTabSize):
        self._tabA = [[0 for row in range(maxTabSize)] for col in range(maxTabSize)]

    def _borderFill(self):                              # wypełnia ramkę tablicy wartością -100
        for i in range(len(self._tabA)):
            self._tabA[i][0] = -100                     # kolumny
            self._tabA[0][i] = -100
            self._tabA[i][len(self._tabA)-1] = -100     # wiersze
            self._tabA[len(self._tabA) - 1][i] = -100

    def _getFieldValue(self, col, row):                 # zwraca wartosc podanego pola
        return self._tabA[col][row]

    def _checkField(self, col, row, val):               # sprawdza dane pole i pola obok(te mogą mieć zadaną wartość)
        if self._getFieldValue(col, row) != 0:          # czy wybrane pole jest puste(wartość 0), jeżeli jest wartość - wychodzi
            return False

        for i in range(3):                              # czy przyległe pola są puste, lub mają zadaną wartość. Jeżeli nie - wychodzi
            for j in range(3):
                if self._getFieldValue(col-1+i, row-1+i) > 0 and self._getFieldValue(col-1+i, row-1+i) != val and self._getFieldValue(col-1+i, row-1+i) != -100:
                    return False

        return True

    def _setField(self, col, row, val):                 # ustawia daną wartość w danym polu
        self._tabA[col][row] = val

    def _placeShip(self, val):                          #buduje statek, ustawia odpowiednie wartości w pola
        shipSize = val // 10
        shipOk = [[0 for row in range(shipSize)] for col in range(2)]
        #shipTest = [[0 for row in range(0)] for col in range(0)]

        shipSize -= 1

        while shipSize >= 0:
            col = random.randint(1, 10)
            row = random.randint(1, 10)
            if self._checkField(row, col, val) == True:
                self._setField(row, col, val)
                shipOk[0][shipSize] = row
                shipOk[1][shipSize] = col
                shipSize -=1
        print(shipOk)

        # TODO - ship test (czyli tablica do losowania kolejnych strzałów)

    def doStuff(self):                                  # funkcja testowa
        self._borderFill()
        self._placeShip(42)
        for i in range(len(self._tabA)):                # wiersze
            for j in range(len(self._tabA)):            # kolumny
                if self._tabA[i][j] < 0:
                    fill = " "
                else:
                    fill = "    "
                print(fill, self._tabA[i][j], end="")
            print()

# endClass


if __name__ == "__main__":
    main()