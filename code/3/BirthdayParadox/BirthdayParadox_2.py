import random
from collections import Counter


def has_duplicate(lst):
    collectlst = Counter(lst)
    for i in collectlst:
        if collectlst[i] > 1:
            # print 'Duplicate items found'
            return True
    return False

def assign_bday():
    birthday = []
    for i in xrange(23):
        bday = random.randint(1, 365)
        birthday.append(bday)
    return birthday


count, sample = 0, 1000
for i in range(sample):
    birthday = assign_bday()
    if has_duplicate(birthday) == True:
        count += 1

print 'After %d simulations:' % sample
print '%d simulations with at least one match' % count
