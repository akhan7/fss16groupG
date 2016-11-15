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

    def __init__(self, name, id, duration=2):
        self.cname = name
        self.cid = id
        self.students = []
        self.duration = duration

    def __eq__(self, other):
        return self.cname == other.cname and self.cid == other.cid

    @staticmethod
    def register(course, student):
        if not Course.isRegistered(course, student):
            course.students.append(student)
            if not student.courses.__contains__(course):
                student.courses.append(course)

    @staticmethod
    def isRegistered(course, student):
        if not course is None and not student is None:
            if not course.students.__contains__(student):
                return False
            return True
        return False


class TimeSlot:
    """
    Time slots have a start and end time and will contain a Course
    """
    format = '%m/%d/%Y'
    push_format = '%m/%d/%Y %H:%M:%S'

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.course = None

    def assign(self, course):
        self.course = course


class ClassRoom:
    def __init__(self, id, capacity, lat, long):
        self.id = id
        self.capacity = capacity
        self.latitude = lat
        self.longitude = long
