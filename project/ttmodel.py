import math
from model import Model
from decision import Decision


class TimeTableModel(Model):
    def __init__(self):
        objectives = [self.__f1, self.__f2]
        decisions = []
        constraints = []
        Model.__init__(self, decisions, objectives,constraints)

    def soft_prox(self):
        return 0

    def hard_prox(self):
        return 0
