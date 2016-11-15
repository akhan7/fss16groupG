import csv
from datetime import datetime, timedelta
from ttmodel_comps import *
import random


class Data:
    def __init__(self):
        self.courses = {}
        self.students = {}
        self.dates = {}
        self.__populate_data()

    def __populate_dates(self):
        start_date = "11/11/2016"
        end_date = "12/11/2016"

        currDate = datetime.strptime(start_date, TimeSlot.format)
        while currDate < (datetime.strptime(end_date, TimeSlot.format)):
            self.dates[currDate] = []
            currDate = currDate + timedelta(days=1)

    def __populate_students(self):
        f = open("data/students.dat", 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                self.students[row[0]] = Student(row[1] + row[2], row[0])
        finally:
            f.close()

    def __populate_courses(self):
        f = open("data/courses.dat", 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                self.courses[row[0]] = Course(row[1], row[0])
        finally:
            f.close()

    def __populate_registration(self):
        f = open("data/registration.dat", 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                Course.register(self.courses[row[0]], self.students[row[1]])
        finally:
            f.close()

    def __random_reg(self):

        f = open("data/registration.dat", 'wb')

        try:
            ind = 0
            while ind < len(self.students) * 3:

                course = self.courses[random.choice(self.courses.keys())]
                student = self.students[random.choice(self.students.keys())]

                if not Course.isRegistered(course, student):
                    if len(student.courses) < 3:
                        Course.register(course, student)
                        f.write(course.cid + "," + student.id + "\n")
                        ind += 1

        finally:
            f.close()

    def __populate_data(self):
        self.__populate_courses()
        self.__populate_students()
        # self.__random_reg()
        self.__populate_registration()
        self.__populate_dates()


##test##
d = Data()

print len(d.courses), len(d.students)
