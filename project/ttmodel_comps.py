# time table scheduler components
class Student:
    """
        Wrapper class for a Student and has a reference to the courses taken by this student
    """
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = []

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id


class Course:
    """
        Wrapper class for a course and has a reference to the students who attend this course
    """

    def __init__(self, name, id):
        self.cname = name
        self.cid = id
        self.students = []

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    @staticmethod
    def register(course, student):
        if not course is None and not student is None:
            if not course.students.__contains__(student):
                course.students.append(student)
                if not student.courses.__contains__(course):
                    student.courses.append(course)



class TimeSlots:
    """
    Time slots have a start and end time and will contain a Course
    """
    def __init__(self, date, start_time, end_time):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.course = None

    @staticmethod
    def assign(timeslot, course):
        if timeslot.course is not None:
            timeslot.course = course
