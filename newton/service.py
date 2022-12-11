from typing import Any
import random

from sympy import diff, Symbol, sympify, Matrix, symbols


class InputNewton:
    lines: list = []

    def __init__(self, filepath: str = "input.txt"):
        self.filepath = filepath
        self._get_lines()

    def _get_lines(self):
        with open(self.filepath, "r") as file:
            for line in file:
                self.lines.append(line.replace("=0\n", ""))

    def get_equations(self):
        return self.lines[:-1]

    def get_variables(self):
        return self.lines[-1]


class Newton:
    def __init__(self, equations: list[str], variables: str, eps: float, split_str: str = ", "):
        self.eps: float = eps
        self.vector: Matrix = Matrix([random.uniform(0.1, 22.0) for i in range(len(equations))])
        self.variables: list[Symbol] = symbols(list(map(str, variables.split(split_str))))
        self.equations: list[str] = equations

    def _get_jacobi_matrix(self) -> list[list[str]]:
        jacobi = []

        for equation in self.equations:
            equation_j = []
            for variable in self.variables:
                equation_j.append(str(diff(equation, variable)))

            jacobi.append(equation_j)

        return jacobi

    def _get_local_vars(self) -> dict:
        local_vars = dict()

        for i in range(len(self.variables)):
            local_vars[self.variables[i].name] = self.vector[i]

        return local_vars

    def _calculate_matrix(self, matrix: Any) -> list[list[float]]:
        local_vars = self._get_local_vars()
        result = []

        for i in range(len(matrix)):
            result_i = []
            for j in range(len(matrix[i])):
                result_i.append(sympify(matrix[i][j], locals=local_vars))
            result.append(result_i)
        return result

    def _calculate_f_matrix(self) -> Matrix:
        local_vars = self._get_local_vars()
        result = []

        for equation in self.equations:
            result.append(sympify(equation, locals=local_vars))

        return Matrix(result)

    @staticmethod
    def _sum_magnitudes(matrix: Matrix) -> float:
        result: float = 0.0
        minus_count = 0

        for value in matrix:
            if value < 0:
                minus_count += 1
            result += abs(value)

        return result if minus_count % 2 == 0 else -result

    def get_vector(self) -> Matrix:
        return self.vector

    def calculate(self) -> dict:
        jacobi = self._get_jacobi_matrix()
        result = {}

        x_last = None
        delta: float = 1.0

        while not x_last or abs(delta) > self.eps:
            x_last = self.vector
            try:
                w = Matrix(self._calculate_matrix(jacobi))
                self.vector -= w.inv() * self._calculate_f_matrix()
            except:
                return {"detail": "Have no solutions"}
            delta = self._sum_magnitudes(self.vector - x_last)

        for i in range(len(self.vector)):
            result[self.variables[i]] = self.vector[i]

        return result
