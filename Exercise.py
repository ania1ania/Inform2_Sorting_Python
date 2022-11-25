
import CheckIt
from random import randint

def losuj(rozmiar, od, do):
    list = []
    for x in range(rozmiar):
        list += [randint(od, do)]
    return list

print ("Lista 12 elementów od 3 do 8", losuj(12, 3, 8))
print ("Lista 16 elementów od 1 do 10", losuj(16, 1, 10))
print ("Lista 20 elementów od 0 do 10", losuj(20, 0, 10))
