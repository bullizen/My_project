# Funktion som heter calculate tar emot ett obestämt antal positionella argument (som ska vara antingen int eller float) och ett valfritt nyckelordsargument 'operator'.

# Om operator inte anges, ska funktionen anta att det är '+'. Funktionen kommer sedan att antingen summera eller subtrahera argumenten baserat på värdet av operator.

# # Exempel på funktionsanrop och förväntade returvärden

# print(calculate(1, 2, 3, 4))  # Förväntat returvärde: 10
# print(calculate(1, 2, 3, 4, operator='+'))  # Förväntat returvärde: 10
# print(calculate(10, 1, 2, operator='-'))  # Förväntat returvärde: 7
# print(calculate(5, 5, operator='-'))  # Förväntat returvärde: 0
# print(calculate())  # Förväntat returvärde: 0 (inga argument)

def calculate(*argument):
    operator = 