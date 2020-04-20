class Function:
    def __init__(self, eq: list):
        self.coefs = eq
        self.__counter = len(eq) - 1

    def dec(self):
        self.__counter -= 1
        return self.__counter + 1

    def __str__(self):
        arr = [str(x) + 'x^' + str(self.dec()) for x in self.coefs if self.__counter > 0]
        a = str(self.coefs[-1])
        if len(self.coefs) > 1:
            a = ' + '.join(arr) + ' + ' + a
        return 'y = ' + a

    def __call__(self, a):
        self.__counter = len(self.coefs) - 1
        return sum([x * a ** self.dec() for x in self.coefs])
