import CheckIt


def ile_liczb(tab):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass


print("")
print("Wyniki testów:")
print("----------------------------------------+------------+-----------+-----------")
print(" Test                                   | Oczekiwano | Otrzymano | Wynik")
print("----------------------------------------+------------+-----------+-----------")
print(" ile_liczb([7, 1, 4, 10, 8, 2, 4, 4, 8])| 6          |", ile_liczb(
    [7, 1, 4, 10, 8, 2, 4, 4, 8]), "        |", CheckIt.checkIt(6, (ile_liczb([7, 1, 4, 10, 8, 2, 4, 4, 8]))))
print("----------------------------------------+------------+-----------+-----------")
print(" ile_liczb([6, 6, 6, 6, 6, 6, 6, 6, 6]) | 1          |", ile_liczb(
    [6, 6, 6, 6, 6, 6, 6, 6, 6]), "        |", CheckIt.checkIt(1, ile_liczb([6, 6, 6, 6, 6, 6, 6, 6, 6])))
print("----------------------------------------+------------+-----------+-----------")
print(" ile_liczb([1, 2, 4, 5, 7, 3, 6, 9, 8]) | 9          |", ile_liczb(
    [1, 2, 4, 5, 7, 3, 6, 9, 8]), "        |", CheckIt.checkIt(9, ile_liczb([1, 2, 4, 5, 7, 3, 6, 9, 8])))
print("")
