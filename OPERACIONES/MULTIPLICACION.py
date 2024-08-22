
def multiplicarComplejos(a=[], b=[]): 

    real = a[0]*b[0] + (a[1]*b[1]*-1)
    imaginaria = a[0]*b[1] + a[1]*b[0]
    return real, imaginaria

def printResultado(resultado):
    print(resultado[0], '+', resultado[1],'i')

def main():
    printResultado(multiplicarComplejos([2, 5], [5, -3]))
main()