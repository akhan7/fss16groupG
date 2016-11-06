import math
from model import Model
from decision import Decision


class TimeTableSched(Model):
    def __init__(self):
        objectives = [self.__f1, self.__f2]
        decisions = [Decision("x1", -5, 5), Decision("x2", -5, 5), Decision("x3", -5, 5)]
        constraints = []
        Model.__init__(self, decisions, objectives,constraints)

    def soft_prox(self):
        return 0

    def hard_prox(self):
        return 0
