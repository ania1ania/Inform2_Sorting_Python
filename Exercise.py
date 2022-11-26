import CheckIt


def minimum(liczba):
    # zdefiniuj funkcję i sprawdź jej działanie
    pass


print("")
print("Wyniki testów:")
print("----------------------------+------------+-----------+-----------")
print(" Test                       | Oczekiwano | Otrzymano | Wynik")
print("----------------------------+------------+-----------+-----------")
print(" minimum(7777777777)        | 7          | ", minimum(
    7777777777), "       |", CheckIt.checkIt(7, minimum(7777777777)))
print("----------------------------+------------+-----------+-----------")
print(" minimum(9876543210)        | 0          | ", minimum(
    9876543210), "       |", CheckIt.checkIt(0, minimum(9876543210)))
print("----------------------------+------------+-----------+-----------")
print(" minimum(12345678987654321) | 1          | ", minimum(
    12345678987654321), "       |", CheckIt.checkIt(1, minimum(12345678987654321)))
print("")
