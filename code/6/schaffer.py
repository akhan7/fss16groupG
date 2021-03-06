from model import Model
from decision import Decision


class Schaffer(Model):
    def __init__(self):
        objectives = [self.__f1, self.__f2]
        decisions = [Decision("x",-10 ** 5, 10 ** 5)]
        Model.__init__(self, decisions, objectives)

    def __f1(self,x):
        """Generates f1(x)"""
        return x[0] * x[0]

    def __f2(self,x):
        """Generates f2(x)"""
        return (x[0] - 2) * (x[0] - 2)
