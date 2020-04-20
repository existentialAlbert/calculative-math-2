from logic.TrapezoidMethodSolver import TrapezoidMethodSolver
from logic.function import Function

if __name__ == '__main__':
    while (True):
        try:
            print('Введите коэффициенты функции через пробел:')
            a = input().strip()
            f = Function([int(x) for x in a.split(' ')])
            print(f)
            print('Введите границы:')
            b = input().strip()
            print('Укажите точность:')
            n = input().strip()
            solver = TrapezoidMethodSolver()
            print('Ответ:')
            print(solver.solve(*[int(x) for x in b.split(' ')], int(n), f))
            print('Продолжить? y/n')
            q = input()
            if q == 'n':
                break
            else:
                continue
        except BaseException:
            print('Неверный формат')
            continue
