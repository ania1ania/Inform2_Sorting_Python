
def checkIt(a, b):
    if a == b:
        return "Pozytywny"
    else:
        return "Negatywny"

def checkList(a, b):
    isEqual = 1
    for x in range(len(a)):
        if a[x] != b[x]:
            isEqual = 0
    if isEqual:
        return "Pozytywny"
    else:
        return "Negatywny"
