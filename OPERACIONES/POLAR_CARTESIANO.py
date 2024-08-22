import math

def polarCartesiano(a):

    a0 = a[0] * math.cos(a[1])
    a1 = a[0] * math.sen(a[1])

    return a0, a1


def printResultado(resultado):
    print(resultado[0], '+', resultado[1],'i')

def main():
    printResultado(polarCartesiano([2, 5]))
main()