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
    min_x = float('inf')
    max_x = float('-inf')
    for x in xrange(xmin, xmax):
        curr = schaffer(x)
        if curr < min_ener:
            min_ener = curr
            min_x = curr
        if curr > max_ener:
            max_ener = curr
            max_x = curr

    return (min_ener, max_ener, min_x, max_x)


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
    return random.randint(SCHAFFER_X_MIN, SCHAFFER_X_MAX)


def get_energy(min, max, val):
    return (val - min) / float(max - min)


def get_energy_back(min, max, val):
    return val * (max - min) + min


def get_prob(e, en, t):
    # print(e - en,t,end="\n")
    return pow(math.e, ((e - en) / 1 - t))


def simulated_annealing(kmax, emin):
    """"""
    min_ener, max_ener = get_random_min_max(100000)
    s = random.randint(SCHAFFER_X_MIN, SCHAFFER_X_MAX)
    e = get_energy(min_ener, max_ener, schaffer(s))

    print("Initial (s , e) ", s, e, end='\n')

    sb = s
    eb = e

    k = 1

    while k < kmax and eb > emin:
        sn = get_random_neighbor(s)
        en = get_energy(min_ener, max_ener, schaffer(sn))

        if k == 1 or k % 25 == 0: print("\n,%d, %.2f, " % (k, eb), end="")

        if en < eb:
            sb = sn
            eb = en
            print("!", end='')

        if en < e:
            s = sn
            e = en
            print("+", end='')

        elif get_prob(e, en, k / float(kmax)) < random.random() - k / float(kmax):
            s = sn
            e = en
            print("?", end='')

        print(".", end='')
        k += 1

    return sb, eb, min_ener, max_ener  # print get_min_max(SCHAFFER_X_MIN, SCHAFFER_X_MAX)


kmax = 5000
act_min, act_max, min_x, max_x = get_min_max(SCHAFFER_X_MIN, SCHAFFER_X_MAX)

x, e, sim_min, sim_max = simulated_annealing(kmax, 0)

print("\n\nkmax = ", kmax, end="\n")
print("The best attainable solution : ", act_min, " at ", min_x)
print("Simulated min and max energy : ", sim_min, " , ", sim_max, end='\n')
print("The attained solution by simuated annealing : ", get_energy_back(sim_min, sim_max, e), " at ", x)
