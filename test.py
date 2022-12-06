from newton.service import Newton
from sympy import diff, symbols, Symbol


data = [
    "E**(x1*x2)+x1**2+x2-1.20+cos(x1)",
    "x1**2+x2**2+x1-0.55"
]
vector = [0.6, 0.5]
variables_str = "x1, x2"
variables = symbols(list(map(str, variables_str.split(", "))))

newton = Newton(equations=data, vector=vector, variables=variables, eps=0.0000001)
newton.calculate()
