from sympy import *
from functools import reduce


N = 50
k = 1

def f(n:int):
    E = 0
    z = Symbol("z")
    
    for d in divisors(primorial(n, nth=True)):
        for c in divisors(d):
            if c % 2 != 0:
                Xcd = Symbol(f"X_{{{c},{d}}}")
                E += (-1)**primeomega(d) * floor((z - Xcd)/d)
                
    return E


print(latex(f(2)))