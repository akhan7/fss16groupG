import math
from model import Model
from decision import Decision


class Kursawe(Model):
    def __init__(self):
        objectives = [self.__f1, self.__f2]
        decisions = [Decision("x1", -5, 5), Decision("x2", -5, 5), Decision("x3", -5, 5)]
        Model.__init__(self, decisions, objectives)

    def __f1(self, x):
        total = 0
        for i in xrange(len(x) - 1):
            value = -10 * math.exp((-0.2 * ((x[i]) ** 2) + ((x[i + 1]) ** 2)))
            total += value
        return total

    def __f2(self, x):
        a = 0.8
        b = 1
        sum = 0
        for i in xrange(len(x)):
            sum += (abs(x[i]) ** a) + (5 * math.sin((x[i]) ** b))
        return sum
