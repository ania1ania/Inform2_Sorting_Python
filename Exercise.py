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
        if x >= t[i] and x < t[i + 1]:
            t.insert(i+1, x)
            return t        # po wstawieniu kończymy pętlę


def sort_w(t):
    pom = []  # nowa lista
    pom = pom + [t[0]]
    for i in range(1, len(t)):
        # wstawia kolejne elementy w nowo tworzonej liście pom
        wstawianie(pom, t[i])
    return pom


print("")
print("Wyniki testów:")
print("----------------------------+---------------------+--------------------+-----------")
print(" Test                       | Oczekiwano          | Otrzymano          | Wynik")
print("----------------------------+---------------------+--------------------+-----------")
print(" sort_w([0, 0, 1, 1, 2, 2]) | [0, 1, 2]           |", sort_w(
    [0, 0, 1, 1, 2, 2]), "         |", CheckIt.checkList([0, 1, 2], (sort_w([0, 0, 1, 1, 2, 2]))))
print("----------------------------+---------------------+--------------------+-----------")
print(" sort_w([4, 3, 2, 1, 0])    | [0, 1, 2, 3, 4]     |", sort_w(
    [4, 3, 2, 1, 0]), "   |", CheckIt.checkList([0, 1, 2, 3, 4], sort_w([4, 3, 2, 1, 0])))
print("----------------------------+---------------------+--------------------+-----------")
print(" sort_w([3, 51, 2, 17, 0])  | [0, 2, 3, 17, 51]   |", sort_w(
    [3, 51, 2, 17, 0]), " |", CheckIt.checkList([0, 2, 3, 17, 51], sort_w([3, 51, 2, 17, 0])))
print("")
