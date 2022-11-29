from abc import ABC, abstractmethod
from sympy import diff, symbols, Symbol


class Method(ABC):
    E: float = 0.000001
    equations: list[str] = None


class Newton(Method):
    def __init__(self, equations: list[str], eps: float = None):
        if eps:
            self.E = eps

        self.equations = equations

    def _set_starting_vector(self):
        self.vector = [float(eval(equation[-1])) for equation in self.equations]

    def get_jacobi_matrix(self, symbol: list) -> list[list[str]]:
        jacobi = []

        for equation in self.equations:
            equation_j = []

            for variable in symbol:
                equation_j.append(diff(equation, variable))

            jacobi.append(equation_j)

        return jacobi

