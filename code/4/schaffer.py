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


def sim_annealing()



print get_min_max(-10000, 10000)



