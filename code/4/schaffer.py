import random

SCHAFFER_X_MIN = -100000
SCHAFFER_X_MAX = 100000


def function1(x):
    return x * x


def function2(x):
    return (x - 2) * (x - 2)


def schaffer(x):
    return function1(x) + function2(x)


def get_min_max(xmin, xmax):
    min_ener = float('inf')
    max_ener = float('-inf')
    for x in xrange(xmin, xmax):
        curr = schaffer(x)
        if curr < min_ener:
            min_ener = curr
        if curr > max_ener:
            max_ener = curr

    return (min_ener, max_ener)


def get_random_min_max(count):
    ind = 0
    min_ener = float('inf')
    max_ener = float('-inf')

    while ind < count:
        x = random.randint(SCHAFFER_X_MIN, SCHAFFER_X_MAX)
        curr = schaffer(x)
        if curr < min_ener:
            min_ener = curr
        if curr > max_ener:
            max_ener = curr
        ind += 1

    return (min_ener, max_ener)


def get_normalizes
def simulated_annealing()



#print get_min_max(SCHAFFER_X_MIN, SCHAFFER_X_MAX)
#print get_random_min_max(100)
