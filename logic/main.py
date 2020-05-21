from logic.RectangleMethodSolver import RectangleMethodSolver
from logic.TrapezoidMethodSolver import TrapezoidMethodSolver
from logic.function import Function

if __name__ == '__main__':
    while True:
        try:
            print('Введите коэффициенты функции через пробел:')
            a = input().strip()
            f = Function([int(x) for x in a.split(' ')])
            print(f)
            print('Введите границы:')
            b = input().strip()
            # print('Укажите количество шагов:')
            #n = input().strip()
            print('Введите желаемую точность:')
            eps = input().strip()
            solver = TrapezoidMethodSolver()
            print('Ответ:')
            print(solver.solve_with_precision(*[int(x) for x in b.split(' ')], int(eps), f),)
            print('Продолжить? y/n')
            q = input()
            if q == 'n':
                break
            else:
                continue
        except BaseException:
            print('Неверный формат')
            continue
