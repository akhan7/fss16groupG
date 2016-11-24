import math
from model import Model
from datetime import datetime, timedelta
from ttmodel_comps import *
from decision import Decision


class TimeTableModel(Model):
    def __init__(self):
        objectives = [self.__soft_prox, self.__hard_prox]
        decisions = []
        constraints = []
        Model.__init__(self, decisions, objectives,constraints)

    def __soft_prox(self,timeslots):
        """
        Args:
            timeslots:
             A list of time slots
        Returns:
            proximity cost due to soft constraints

        """

    def generate_one(self):
        while True:
            point = []
            for decision in self.decisions:

            valid = self.is_valid(point)
            if valid:
                return point


    def hard_prox(self):

        return 0
