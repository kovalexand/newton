from newton.service import Newton
from sympy import diff, symbols, Symbol


data = [
    "E**(x1*x2)+x1**2+x2-1.20+cos(x1)",
    "x1**2+x2**2+x1-0.55"
]

symbols = symbols(['x1', 'x2'])

test = Newton(data)
result = test.get_jacobi_matrix(symbols)
