import CheckIt


def wstawianie(t, x):
    if x < t[0]:  # przypadek kiedy trzeba wstawić na początku listy
        t.insert(0, x)
        return t
    if x > t[len(t) - 1]:   # przypadek kiedy trzeba wstawić na końcu listy
        t.insert(len(t), x)
        return t
    # pozostałe przypadki kiedy wstawiamy wewnątrz listy.
    for i in range(len(t) - 1):
        if x > t[i] and x < t[i + 1]:
            t.insert(i+1, x)
            return t        # po wstawieniu kończymy pętlę


# sortowanie przez wstawianie
def sort_w(t):
    pom = []  # nowa lista
    pom = pom + [t[0]]
    for i in range(1, len(t)):
        # wstawia kolejne elementy w nowo tworzonej liście pom
        wstawianie(pom, t[i])
    return pom


def ile_liczb(tab):
    v = sort_w(tab)   # ta wersja sortowania przez wstawianie usuwa zdublowane elementy
    return len(v)  # zwracam dugość zmodyfikowanej listy


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
