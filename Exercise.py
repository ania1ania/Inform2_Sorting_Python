import CheckIt

def sort_b(t):
    isSorted = 0
    while 0 == isSorted:    # sortujemy dopóki flaga isSorted nie zostanie przestawiona w pętli for
        isSorted = 1    # flaga ustawiana podczas iteracji jeżeli trzeba bylo dokonoć zamiany elementów - sortowania
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                isSorted = 0    # będzie zamiana (sortowanie) elementów t[i] i t[i +1]
                t[i], t[i + 1] = t[i + 1], t[i]
    return t

print("")
print("Wyniki testów:")
print("----------------------------------+---------------------------+---------------------------+-----------")
print(" Test                             | Oczekiwano                | Otrzymano                 | Wynik")
print("----------------------------------+---------------------------+---------------------------+-----------")
print(" sort_b([6, 3, 15, 9, 2])         | [2, 3, 6, 9, 15]          | ", sort_b([6, 3, 15, 9, 2]),"        |", CheckIt.checkList([2, 3, 6, 9, 15], (sort_b([6, 3, 15, 9, 2]))))
print("----------------------------------+---------------------------+---------------------------+-----------")
print(" sort_b([11, 16, 8, 33, 6, 8, 1]) | [1, 6, 8, 8, 11, 16, 33]  | ", sort_b([11, 16, 8, 33, 6, 8, 1]),"|", CheckIt.checkList( [1, 6, 8, 8, 11, 16, 33], sort_b([11, 16, 8, 33, 6, 8, 1])))
print("----------------------------------+---------------------------+---------------------------+-----------")
print(" sort_b([9, 5, 2, 8, 0])          | [0, 2, 5, 8, 9]           | ", sort_b([9, 5, 2, 8, 0]),"         |", CheckIt.checkList([0, 2, 5, 8, 9], sort_b([9, 5, 2, 8, 0])))
print("")

