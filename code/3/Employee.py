class Employee:
   def __init__(self, name, age):
      self.name = name
      self.age = age


   def __repr__(self):
      return 'Name : %s, Age:%s' %( self.name,  self.age)
      
   def __lt__(self,other):
   	  return self.age < other.age
   
   	

emp1 = Employee("Neha", 22)
emp2 = Employee("Ahmad", 24)
emp3 = Employee("Sekhar", 23)
print emp1
print emp2
print emp3

print "Sorting:"

if emp1 < emp2:
	if emp1 < emp3:
		print emp1
		if emp2<emp3:
			print emp2
			print emp3
		else:
			print emp3
			print emp2
	else:
		print emp3
		print emp1
		print emp2
else:
	if emp2 < emp3:
		print emp2
		if emp1<emp3:
			print emp1
			print emp3
		else:
			print emp3
			print emp1
	else:
		print emp3
		print emp2
		print emp1	
