from logic.Solver import Solver
from logic.function import Function


class TrapezoidMethodSolver(Solver):

    def solve(self, a, b, n, func: Function):
        sum = (func(a) + func(b)) / 2
        step = (b - a) / n
        for i in range(1, n):
            sum += func(a + i * step)
        return sum * step
