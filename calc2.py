import math
import sympy as smp
from sympy import *
import numpy as np
import scipy.integrate as spi


print('Single integral computed by SciPy fixed_quad')
print('Example 1-01 fixed_quad')
print('Integral of 2xe^-x from x=1 to x=5')

integrand =  lambda x : 2 * x * np.exp(-x)
a = 1.
b = 5.

result, none = spi.fixed_quad(integrand, a, b, n=5)
print('Result is ', result)

n= smp.symbols('n')

smp.Sum(5/3**n, (n,0,smp.oo))