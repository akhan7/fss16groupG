from __future__ import division
import random
from candidate import Candidate
from sk import a12

""" This contains the optimizers """


def de(model, frontier_size=10, cop=0.4, ea=0.5, max_tries=100, threshold=0.01, era_size=10, era0=None, lives=5):
    # normalizers = prerun_each_obj(model, runs=10000)
    out = []

    repeat = int(max_tries / era_size)
    print "Repeat:" + str(repeat)
    frontier_size = era_size
    energy = model.aggregate

    def type1(can1, can2):
        return energy(can1) < energy(can2)

    def type2(era1, era2):
        for index, objective in enumerate(era2):
            a12_score = a12(era1[index], objective)
            if a12_score >= 0.56:
                return True
        return False

    frontier = []
    total = 0
    n = 0

    if not era0:
        for i in range(frontier_size):
            can = model.gen_candidate()
            while can is None:
                can = model.gen_candidate()
            frontier += [can]
            total += energy(can)
            n += 1

    else:
        for can in era0:
            p = Candidate(dec_vals=can.dec_vals, scores=can.scores)
            frontier += [p]
        total = sum([energy(can) for can in frontier])
        n = len(frontier)

    curr_era = [[] for _ in model.objectives()]

    # print "model_objectives_len:" + str(len(curr_era))

    for can in frontier:
        model.eval(can)
        obj_scores = [x for x in can.scores]
        for index, score in enumerate(obj_scores):
            curr_era[index] += [score]

    # Currently treating candidates as having only one objective i.e. energy
    # which we're minimizing
    eras = [curr_era]
    curr_era = [[] for _ in model.objectives()]

    best_score = total / n
    curr_lives = lives
    early_end = False

    for j in range(repeat):

        # if j % era_size == 0:
        out += ["\n" + str(best_score) + " "]

        total, n = de_update(frontier, cop, ea, energy, out, model.decisions())
        if total / n < threshold:
            best_score = total / n
            out += ["!"]
            out += ["\nScore satisfies Threshold"]
            break

        elif total / n < best_score:
            best_score = total / n
            out += ["!"]

        for can in frontier:
            model.eval(can)
            obj_scores = [x for x in can.scores]
            # print "obj_scores_len:" + str(len(obj_scores))
            for index, score in enumerate(obj_scores):
                curr_era[index] += [score]

        eras += [curr_era]
        curr_era = [[] for _ in model.objectives()]

        if len(eras) > 1:
            if type2(eras[len(eras) - 2], eras[len(eras) - 1]):
                curr_lives += lives
            else:
                curr_lives -= 1
                if curr_lives == 0:
                    # print "No more"
                    out += ["\nNo more Lives"]
                    break

    # print ''.join(out)
    # print "\nNumber of repeats:" + str(j + 1)
    # print "Best Score:" + str(best_score)
    return _, best_score, eras[len(eras) - 1]


def de_update(frontier, cop, ea, energy_func, out, decision_objs):
    total, n = (0, 0)

    for i, can in enumerate(frontier):
        score = energy_func(can)
        new_can = de_extrapolate(frontier, i, cop, ea, decision_objs)
        new_score = energy_func(new_can)

        if new_score < score:
            frontier[i] = new_can
            score = new_score
            out += ["+"]
        else:
            out += ["."]
        total += score
        n += 1
    return total, n


def de_extrapolate(frontier, can_index, cop, ea, decision_objs):
    can = frontier[can_index]
    new_can = Candidate(dec_vals=list(can.dec_vals))
    two, three, four = get_any_other_three(frontier, can_index)

    changed = False

    for d in range(len(can.dec_vals)):
        x, y, z = two.dec_vals[d], three.dec_vals[d], four.dec_vals[d]

        if random.random() < cop:
            changed = True
            new_can.dec_vals[d] = decision_objs[d].wrap(x + ea * (y - z))

    if not changed:
        d = random.randint(0, len(can.dec_vals) - 1)
        new_can.dec_vals[d] = two.dec_vals[d]

    return new_can


def get_any_other_three(frontier, ig_index):
    lst = []

    while len(lst) < 3:
        i = random.randint(0, len(frontier) - 1)
        if i is not ig_index:
            lst += [frontier[i]]

    return tuple(lst)
