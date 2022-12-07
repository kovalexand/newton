from newton.service import Newton


data = [
    "x+x*y**3-9",
    "x*y+x*y**2-6"
]
variables = "x, y"

newton = Newton(equations=data, variables=variables, eps=0.0000001)
print(newton.calculate())
