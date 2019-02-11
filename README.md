# Statki
Gra w statki dla jednej osoby

Zmienne:
*_tabA[][] - tablica na której będą tworzone statki "NPC'a". 
    ramka przyjmuje wartość -100
    puste pole przyjmuje wartość 0
    pole ze statkiem przyjmuje wartość danego statku 


Funkcje:
*def _borderFill(self):
    Wypełnia "ramkę" tablicy _tabA[][] wartością -100
    
*def _getFieldValue(self, col, row):
    Zwraca wartość pola tablicy o współrzędnych _tabA[col][row]
    
*def _checkField(self, col, row, val):
    Sprawdza wartość w polu tablicy _tabA[col][row]. 
    Jeżeli pole != 0 zwraca fałsz.
    Jeżeli pole == 0 sprawdza pobliskie pola.
        Jeżeli sprawdzane pola != od -100 oraz od zmiennej val zwraca fałsz
        W przeciwnym wypadku zwraca prawdę 
        
*def _setField(self, col, row, val):
    ustawia wartość pola tablicy _tabA[col][row]
    
*def _shipTestSet(self, col, row, val):
    Tworzy tablicę pól które będą mogły być wykorzystane do dołożenia kolejnego "masztu" do statku