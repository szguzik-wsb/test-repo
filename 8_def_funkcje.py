import random

array = []

def addToArray(item):
    array.append(item)
    print(array, 'Ilosc elementow w tablicy to: ', len(array))
    checkArray()


def checkArray():
    if len(array) == 50:
        print("Wpisano 50 pozycji")
    else:
        addToArray(random. randint(0,9))

checkArray()
print("Konic programu")