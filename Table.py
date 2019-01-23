import random


class Table:
    def __init__(self, size):
        self._size = size
        self._create_empty()

    def _create_empty(self):
        self._tab = [[0 for y in range(self._size)] for x in range(self._size)]

    def doStuff(self):
        for i in range(self._size):
            for j in range (self._size):
                self._tab[i][j] = random.randint(0, 90) + 10
                print(self._tab[i][j])
# endClass


#t = Table(10)
#t.doStuff()