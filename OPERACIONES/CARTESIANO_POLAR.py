
import math

def Cartesianas_a_polares(a):

    p = (a[0]**2 + a[1]**2)**0.5
    alpha = math.atan2(a[1],a[0])
    return p, alpha