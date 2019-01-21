from Statki import Statki
from Parametry import Parametry


# ----- Program główny -----
parametry = Parametry()
statki = Statki(parametry.getTabWielkosc())

statki.ustawTab()