class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = []

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id


students = []
students.append(Student("sekhar", 1))
students.append(Student("sekhar2", 2))
students.append(Student("sekhar3", 3))

if students.__contains__(Student("sekhar",1)):
    print "present"
else:
    print "not present"