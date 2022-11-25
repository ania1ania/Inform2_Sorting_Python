
def checkIt(a, b):
    if a == b:
        return "Pozytywny"
    else:
        return "Negatywny"

def checkList(a, b):
    isEqual = 1
    if len(a) == len(b):
        for x in range(len(a)):
            if a[x] != b[x]:
                isEqual = 0
    else:
        isEqual = 0
        
    if isEqual:
        return "Pozytywny"
    else:
        return "Negatywny"
