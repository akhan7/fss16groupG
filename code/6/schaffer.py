from model import Model
from decision import Decision


class Schaffer(Model):
    def __init__(self):
        objectives = [self.f1, self.f2]
        decisions = [Decision(-10 ** 5, 10 ** 5)]
        Model.__init__(self, decisions, objectives)

    def __f1(x):
        """Generates f1(x)"""
        return x * x

    def __f2(x):
        """Generates f2(x)"""
        return (x - 2) * (x - 2)
