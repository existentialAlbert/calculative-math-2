from logic.Solver import Solver
from logic.function import Function


class RectangleMethodSolver(Solver):

    @staticmethod
    def solve(a, b, n, func: Function, how='center'):
        sum = 0
        step = (b - a) / n
        if how == 'center':
            a += step / 2
        elif how == 'left':
            a += 0
        elif how == 'right':
            a += step
        else:
            raise TypeError
        for i in range(0, n):
            sum += step * func(a + i * step)
            # print("y", func(a + i * step), "x", a + i * step)
        return sum
