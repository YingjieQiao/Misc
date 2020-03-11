import sympy as sp
from math import sin
sp.var('x')
print(sp.solve((1+1/x)*((1+x)**20-1)))

