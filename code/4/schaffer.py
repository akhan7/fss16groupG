from __future__ import print_function
import random
import math

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


def get_random_neighbor(x):
    return random.randint(max(SCHAFFER_X_MIN, x - 1000), min(SCHAFFER_X_MAX, x + 1000))


def get_energy(min, max, val):
    return (val - min) / float(max - min)


def get_prob(e, en, t):
    return pow(math.e, ((e - en) / t))


def simulated_annealing(kmax, emax):
    random.seed(10)
    min_ener, max_ener = get_random_min_max(10000)

    print("Simulated min and max energy : ", min_ener, max_ener, end='\n')

    s_init = random.randint(SCHAFFER_X_MIN, SCHAFFER_X_MAX)
    e_init = get_energy(min_ener, max_ener, schaffer(s_init))

    print("Initial (s , e) ", s_init, e_init, end='\n')

    s_best = s_init
    e_best = e_init

    k = 1

    while k < kmax and e_init < emax:
        sn = get_random_neighbor(s_init)
        en = get_energy(min_ener, max_ener, schaffer(sn))

        if en > e_best:
            s_best = sn
            e_best = en
            print("!", end='')

        if en > e_init:
            s_init = sn
            e_init = en
            print("+", end='')

        elif get_prob(e_init, en, k / float(kmax)) < random.random():
            s_init = sn
            e_init = en
            print("?", end='')

        print(".", end='')
        k += 1

        if k % 25 == 0:
            print(s_best, end='\n')

    return s_best


# print get_min_max(SCHAFFER_X_MIN, SCHAFFER_X_MAX)
print
get_random_min_max(1000)

print
"The best attainable solution : " + str(get_min_max(SCHAFFER_X_MIN, SCHAFFER_X_MAX)[1])

simulated_annealing(1000, 1)
