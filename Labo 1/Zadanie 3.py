from functools import reduce

zadania = [
    # [zadanie, czas, nagroda]
    ['zad1', 3, 12],
    ['zad2', 1, 6],
    ['zad3', 8, 26],
    ['zad4', 10, 34],
    ['zad5', 1, 14]
]

def optRozmZad(zadania):
    zadSorted = sorted(zadania, key=lambda x: (x[1], -x[2]))

    czasOcz = 0
    czasSum = 0
    for zadanie in zadSorted:
        czasOcz += zadanie[1]
        czasSum += czasOcz

    kolejOpt = list(map(lambda x: x[0], zadSorted))

    return kolejOpt, czasSum

print(optRozmZad(zadania))