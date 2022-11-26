import CheckIt


def wstawianie(t, x):
    if x <= t[0]:  # przypadek kiedy trzeba wstawić na początku listy
        t.insert(0, x)
        return t
    if x >= t[len(t) - 1]:   # przypadek kiedy trzeba wstawić na końcu listy
        t.insert(len(t), x)
        return t
    # pozostałe przypadki kiedy wstawiamy wewnątrz listy.
    for i in range(len(t) - 1):
        if x >= t[i] and x < t[i + 1]:
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


def minimum(liczba):
    v = []  # tworzę listę cyfr
    while (liczba):
        x = liczba % 10  # pobieram ostatnią cyfrę
        v.append(x)  # i wstawiam ją na końcu listy
        liczba //= 10   # usuwam ostatnią cyfrę
    sort_w(v)   # sortuję listę - na początku będzie najmniejsza wartość
    return v[0]


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
