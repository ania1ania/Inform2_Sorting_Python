import CheckIt

def w(t, x):
    v = []
    inserted = 0    # flaga informacyjna, że liczba x byla już wstawiona bo jest jeden warunek
                    # można to zrobić inaczej - przepisując z t do v sprawdzać czy
                    # t[i] < x < t[i+1]
    for i in range(len(t)):
        if x < t[i] and 0 == inserted:
            v.append(x)
            inserted = 1
        v.append(t[i])
        if i == len(t)-1 and x > t[i]:    # przypadek gdy trzeba wstawić na końcu listy
            v.append(x)
    return v

print("")
print("Wyniki testów:")
print("-------------------------+----------------------+----------------------+-----------")
print(" Test                    | Oczekiwano           | Otrzymano            | Wynik")
print("-------------------------+----------------------+----------------------+-----------")
print(" w([0, 1, 2, 3, 4], 5)   | [0, 1, 2, 3, 4, 5]   |", w([0, 1, 2, 3, 4], 5),"  |", CheckIt.checkList([0, 1, 2, 3, 4, 5], (w([0, 1, 2, 3, 4], 5))))
print("-------------------------+----------------------+----------------------+-----------")
print(" w([2, 4, 6, 8, 10], 7)  | [2, 4, 6, 7, 8, 10]  |", w([2, 4, 6, 8, 10], 7)," |", CheckIt.checkList([2, 4, 6, 7, 8, 10], w([2, 4, 6, 8, 10], 7)))
print("-------------------------+----------------------+----------------------+-----------")
print(" w([11, 13, 26, 78], 5)  | [5, 11, 13, 26, 78]  |", w([11, 13, 26, 78], 5)," |", CheckIt.checkList([5, 11, 13, 26, 78], w([11, 13, 26, 78], 5)))
print("")

