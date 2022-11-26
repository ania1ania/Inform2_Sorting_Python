import CheckIt


def w(t, x):
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


print("")
print("Wyniki testów:")
print("-------------------------+----------------------+----------------------+-----------")
print(" Test                    | Oczekiwano           | Otrzymano            | Wynik")
print("-------------------------+----------------------+----------------------+-----------")
print(" w([0, 1, 2, 3, 4], 5)   | [0, 1, 2, 3, 4, 5]   |", w([0, 1, 2, 3, 4], 5),
      "  |", CheckIt.checkList([0, 1, 2, 3, 4, 5], (w([0, 1, 2, 3, 4], 5))))
print("-------------------------+----------------------+----------------------+-----------")
print(" w([2, 4, 6, 8, 10], 7)  | [2, 4, 6, 7, 8, 10]  |", w([2, 4, 6, 8, 10],
      7), " |", CheckIt.checkList([2, 4, 6, 7, 8, 10], w([2, 4, 6, 8, 10], 7)))
print("-------------------------+----------------------+----------------------+-----------")
print(" w([11, 13, 26, 78], 5)  | [5, 11, 13, 26, 78]  |", w([11, 13, 26, 78],
      5), " |", CheckIt.checkList([5, 11, 13, 26, 78], w([11, 13, 26, 78], 5)))
print("")
