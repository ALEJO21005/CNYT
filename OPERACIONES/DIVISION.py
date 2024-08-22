
def dividirComplejos(a, b):

    real = (a[0]*b[0] + a[1]*b[1]) / (b[0]**2 + b[1]**2)
    imaginaria = (a[1]*b[0] - a[0]*b[1]) / (b[0]**2 + b[1]**2)
    return real, imaginaria

def prettyPrinting(r):
    print(r[0],'+', r[1],'i')

if __name__ == "__main__":
    prettyPrinting(dividirComplejos([-3,1],[1,3]))