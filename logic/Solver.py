from abc import abstractmethod

from logic.function import Function


class Solver:

    @staticmethod
    @abstractmethod
    def solve(a, b, n, func: Function):
        pass

    @classmethod
    def solve_with_precision(cls, a, b, precision, func):
        n = 1
        previous_solution = 0
        actual_solution = cls.solve(a, b, n, func)
        while abs(actual_solution - previous_solution) >= 10 ** -precision:
            n *= 2
            previous_solution = actual_solution
            actual_solution = cls.solve(a, b, n, func)
        print("Искомое решение найдено при n = " + str(n))
        return actual_solution
