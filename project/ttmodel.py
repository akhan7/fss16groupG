from ttmodel_comps import *
from decision import Decision
from data import *
import random
import copy


class TimeTableModel():
    def __init__(self, data):
        self.objectives = [self.__soft_prox, self.__hard_prox]
        self.decisions = [Decision("courses", data.courses), Decision("dates", data.dates)]
        self.constraints = []

    def __soft_prox(self, timeslots):
        """
        Args:
            timeslots:
             A list of time slots
        Returns:
            proximity cost due to soft constraints

        """

    def __hard_prox(self, timeslots):
        """

        :return:
        """

        return 0

    def generate_one(self):
        dates = copy.deepcopy(self.decisions[1].possible_values)
        courses = copy.deepcopy(self.decisions[0].possible_values)
        courses_assigned = {}

        while len(courses) > 0:
            random_course = courses[random.choice(courses.keys())]

            random_date = random.choice(dates.keys())
            random_time_slot = self.get_random_time_slot(dates, random_date, random_course)
            if random_time_slot is not None:
                dates[random_date].append(random_time_slot)
                courses_assigned[random_course.cid] = random_course
                del courses[random_course.cid]

        return dates

    def get_random_time_slot(self, dates, random_date, random_course):
        tries = 0;
        while tries < 20:
            random_hour = random.randint(8, 20)
            timeslot = TimeSlot(random_hour, random_hour + random_course.duration)
            timeslot.assign(random_course)

            flag = False
            for ts in dates[random_date]:
                if timeslot.start_time > ts.start_time and timeslot.start_time < ts.end_time:
                    flag = True
                if timeslot.end_time > ts.start_time and timeslot.end_time < ts.end_time:
                    flag = True

            if not flag:
                return timeslot

            tries += 1

        if tries == 20:
            return None


d = Data()
ttm = TimeTableModel(d)
dates = ttm.generate_one()

print dates

keys = dates.keys()

print keys
keys.sort()

for key in keys:
    for ts in dates[key]:
        print key , ts.start_time, " ", ts.end_time, " ",ts.course.cid
    print "\n"
