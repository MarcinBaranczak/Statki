from Table import Table
from Parameters import Parameters


# ----- Program główny -----
if __name__ == "__main__":
    parameters = Parameters()
    table = Table(parameters.getTabSize())

    table.doStuff()
# endIf