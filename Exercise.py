
import CheckIt

def trzy(a, b, c):
    if a > b:
        pom = a
    else:
        pom = b
    if pom > c:
        return pom
    else:
        return c

print("")
print("Wyniki testów:")
print("-----------------------+------------+-----------+-----------")
print(" Test                  | Oczekiwano | Otrzymano | Wynik")
print("-----------------------+------------+-----------+-----------")
print(" trzy(10, 10, 10)      | 10         | ", trzy(10, 10, 10),"      |", CheckIt.checkIt(10, trzy(10, 10, 10)))
print("-----------------------+------------+-----------+-----------")
print(" trzy(112, 99, 112)    | 112        | ", trzy(112, 99, 112),"     |", CheckIt.checkIt(112, trzy(112, 99, 112)))
print("-----------------------+------------+-----------+-----------")
print(" trzy(456, 456, 455)   | 456        | ", trzy(456, 456, 455),"     |", CheckIt.checkIt(456, trzy(456, 456, 455)))
print("")
