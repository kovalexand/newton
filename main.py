from newton.service import Newton, InputNewton

inp = InputNewton()
method = Newton(equations=inp.get_equations(), variables=inp.get_variables(), eps=0.001)
print(method.get_vector())
print(method.calculate())
