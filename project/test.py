from ttmodel_comps import *
from datetime import datetime, timedelta

students = []
students.append(Student("sekhar", 1))
students.append(Student("sekhar2", 2))
students.append(Student("sekhar3", 3))

if students.__contains__(Student("sekhar", 1)):
    print "present"
else:
    print "not present"

# Create a sample time slot

timeslots = []
format = '%m/%d/%Y'
push_format = '%m/%d/%Y %H:%M:%S'
start_hour = 9
end_hour = 18
timeslot_duration = 3

start_date = "11/11/2016"
end_date = "11/18/2016"

currDate = datetime.strptime(start_date, format)
print currDate

currDateTime = currDate + timedelta(hours=start_hour)
print currDateTime

while currDateTime < (datetime.strptime(end_date, format) + timedelta(hours=end_hour)):
    timeslots.append(currDateTime.strftime(push_format))
    currDateTime += timedelta(hours=timeslot_duration)
    if currDateTime >= currDate + timedelta(hours=end_hour):
        currDateTime += timedelta(days=1)
        currDateTime += timedelta(hours=start_hour)

print timeslots
