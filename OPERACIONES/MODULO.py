
def calcularModulo(a=[]):

    modulo = (a[0]**2 + a[1]**2)**0.5
    return modulo

def printResultado(resultado):
    print(resultado)

def main():
    printResultado(calcularModulo([3, 12]))

main()