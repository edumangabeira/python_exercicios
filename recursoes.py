class Recursoes:

    def __init__(self, i):
        self.i = i
        self.i = 10

    def soma_recursiva(self):
        if self.i == 10:
            return self.i
        else:
            self.i += 1
            return soma_recursiva()


soma_10 = Recursoes(0)
print(soma_10.soma_recursiva())
