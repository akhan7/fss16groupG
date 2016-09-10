class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Name : %s, Age:%s' % (self.name, self.age)

    def __lt__(self, other):
        return self.age < other.age


emp1 = Employee("Neha", 22)
emp2 = Employee("Ahmad", 24)
emp3 = Employee("Sekhar", 23)

inp = [emp1, emp2, emp3]
print "Before Sorting: ", inp
inp.sort()
print "After Sorting: ", inp
