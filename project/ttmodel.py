import math
from model import Model
from datetime import datetime, timedelta
from ttmodel_comps import *
from decision import Decision


class TimeTableModel(Model):
    def __init__(self,data):
        objectives = [self.__soft_prox, self.__hard_prox]
        decisions = [Decision("courses",data.courses),Decision("days",data.days)]
        constraints = []
        Model.__init__(self, decisions, objectives, constraints)

    def __soft_prox(self, timeslots):
        """
        Args:
            timeslots:
             A list of time slots
        Returns:
            proximity cost due to soft constraints

        """

    def generate_one(self):


    def hard_prox(self, timeslots):
        """

        :return:
        """

        return 0
