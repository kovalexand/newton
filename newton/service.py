from typing import Any

from sympy import diff, Symbol, sympify, Matrix


class Newton:
    def __init__(self, equations: list[str], vector: list[float], variables: list[Symbol], eps: float):
        self.eps: float = eps
        self.vector: list[float] = vector
        self.variables: list[Symbol] = variables
        self.equations: list[str] = equations

    def _get_jacobi_matrix(self) -> list[list[str]]:
        jacobi = []

        for equation in self.equations:
            equation_j = []

            for variable in self.variables:
                equation_j.append(str(diff(equation, variable)))

            jacobi.append(equation_j)

        return jacobi

    def _calculate_matrix(self, matrix: Any) -> list[list[float]]:
        local_vars = dict()
        for i in range(len(self.variables)):
            local_vars[self.variables[i].name] = self.vector[i]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = sympify(matrix[i][j], locals=local_vars)

        return matrix

    def _get_negative_vector(self) -> Any:
        result = list()
        for i in self.vector:
            result.append(-i)

        return result

    def calculate(self):
        jacobi = self._get_jacobi_matrix()
        inverse_matrix = Matrix(self._calculate_matrix(jacobi)).inv()
        f_matrix = Matrix(self._get_negative_vector())
        y_matrix = inverse_matrix*f_matrix
        x_matrix = Matrix(self.vector)
        print(y_matrix+x_matrix)
