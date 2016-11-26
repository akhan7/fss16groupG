from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import random, randint, seed
from math import exp
from stats import a12


def type1(x, y):
    return x.score() < y.score()


def type2(era, era_1):
    val = a12(era, era_1)
    if val > 0.56:
        return 5
    else:
        return -1


def mws(model, init_pop):
    maxTries = 20
    maxChanges = 100
    p = 0.5
    sb = model()
    sb.cands = init_pop.cands[:]
    eb = 0
    prev = []
    lives = 5
    a = randint(1, 19)
    seed(a)
    era = 1
    # retries
    for tries in xrange(0, maxTries):
        cur = []
        s = model()
        e = s.score()
        if tries == 0:
            sb.copy(s)
            eb = e

        # in each try, search for the best solution
        for changes in xrange(0, maxChanges):
            if p < random():
                s = model()
            else:
                direction = randint(0, s.decisionSpace - 1)
                s = localSearch(model, s, direction)
            currScore = s.score()
            # type 1 comparison
            if type1(s, sb):
                eb = currScore
                sb.copy(s)
            cur.append(eb)

        # early termination
        if not prev:
            prev = cur[:]
        else:
            lives += type2(prev, cur)
            prev = cur[:]
        if lives is 0:
            print("\n no changing detected, early terminating program")
            break

        print("Era: %s" % era, "Current Best solution: %s, " % sb.cands, "\nf1 and f2: %s, " % sb.fi(),
              ", at which eval the best x is found: %s" % eb)
        era = era + 1

    print("Best solution found: %s, " % sb.cands, "\nf1 and f2: %s, " % sb.fi(),
          ", at which eval the best x is found: %s" % eb)

    return sb


def localSearch(model, s, direction):
    sn = model()
    sn.copy(s)
    sLocal = model()
    sLocal.copy(sn)
    eLocal = sLocal.score()
    # print(direction)
    for val in xrange(int(s.decisions[direction].lo / 100), int(s.decisions[direction].hi / 100)):
        sn.decisions[direction] = val * 100
        if not sn.check():
            continue
        if sn.sum() > eLocal:
            sLocal.copy(sn)
            eLocal = sn.sum()
    return sLocal


def sa(model, init_pop):
    # cooling function
    def probability(en, e, T):
        p = exp((e - en) / T)
        return p

    def energy(eval, min, max):
        return (eval - min) / (max - min)

    # vars
    # print(min, max)
    s = model()
    s.cands = init_pop.cands[:]
    sb = model()
    sb.copy(s)
    e = s.score()
    eb = e
    kmax = 1000
    linewidth = 50
    print('\n %4d : %f ,' % (1, eb))
    prev = []
    cur = []
    lives = 5

    # iteration through eras
    a = randint(1, 20)
    seed(a)
    for k in xrange(1, kmax):
        T = (k / kmax)
        sn = model()
        en = sn.score()
        p = probability(en, e, T)
        q = random()
        if type1(sn, sb):
            eb = en
            sb.copy(sn)
            s.copy(sn)
        elif type1(sn, s):
            s.copy(sn)
            e = en
        elif p < q:
            # print(p, q)
            s.copy(sn)
            e = en

        cur.append(en)

        # when reached the end of an era
        if k % linewidth == 0:
            # check type 2
            if not prev:
                prev = cur[:]
            else:
                lives += type2(prev, cur)
                prev = cur[:]
            if lives == 0:
                print('\nTerminating early')
                break
            cur = []
            print('   %4d : %f ,' % (k, eb))
    print("\nBest solution: %s, " % sb.cands, "\nf1 and f2: %s, " % sb.fi(), sb.score())
    return sb


def update(mod, f, cf, frontier):
    cur = []
    for i, x in enumerate(frontier):
        s = x.score()
        new = extrapolate(frontier, x.cands, f, cf, i, mod)
        new_sc = new.score()
        if type1(new, x):
            s = new_sc
            frontier[i].copy(new)
            cur.append(new_sc)
        else:
            cur.append(s)
    return frontier, cur


def extrapolate(frontier, one, f, cf, id, mode):
    res = mode()
    res.cands = one[:]
    two, three, four = three_others(frontier, id)
    ok = False
    while not ok:
        changed = False
        for d in range(len(one)):
            ran = random()
            x, y, z = two.cands[d], three.cands[d], four.cands[d]
            if ran < cf:
                changed = True
                new = x + f * (y - z)
                res.cands[d] = trim(new, d, mode)  # keep in range
        if not changed:
            ran_index = randint(0, len(one) - 1)
            res.cands[ran_index] = two.cands[ran_index]
        ok = res.check()
    return res


def trim(val, index, mode):
    mod = mode()
    if val > mod.decisions[index].hi:
        val = val % (mod.decisions[index].hi - mod.decisions[index].lo)
    while val < mod.decisions[index].lo:
        val = mod.decisions[index].hi - mod.decisions[index].lo + val
    return val


def three_others(frontier, avoid):
    def oneOther(seen, selected):
        pick_index = randint(0, len(frontier) - 1)
        if pick_index not in seen:
            seen.append(pick_index)
            selected.append(frontier[pick_index])

    # vars
    seen = []
    seen.append(avoid)
    i = 0
    selected = []

    while len(selected) < 3:
        oneOther(seen, selected)
    return selected[0], selected[1], selected[2]


def de(mode, baseline, max_tries=20, frontier_size=25, f=0.75, cf=0.3, epsilon=0.01):
    # vars
    ib = 0
    frontier = [mode() for _ in range(frontier_size)]
    prev = []
    lives = 10
    a = randint(1, 19)
    seed(a)
    # eras
    for k in range(max_tries):
        frontier, cur = update(mode, f, cf, frontier)
        print(cur)
        if not prev:
            prev = cur[:]
        else:
            lives += type2(prev, cur)
            prev = cur[:]
        if lives is 0:
            print("\n Terminating early")
            break

    # find best candidate
    ib = 0
    score = None
    for i, x in enumerate(frontier):
        if score is None:
            score = x.score()
        else:
            curScore = x.score()
            if score > curScore:
                score = curScore
                ib = i

    f1, f2 = frontier[ib].fi()
    print(f1, f2, frontier[ib].cands, score)
    return frontier[ib]
