from __future__ import print_function
from math import pi, fabs, sin, e
from model import Model
from decision import Decision
from objective import Objective


class DTLZ7(Model):
    def __init__(self, num_dec=10, num_obj=2):
        self.decisions = []
        self.cands = []
        self.objs = []
        self.decisionSpace = num_dec
        self.objectiveSpace = num_obj
        for i in xrange(self.decisionSpace):
            self.decisions.append(Decision(0, 1))

        self.objs.append(Objective(0, 1))
        self.objs.append(Objective(5, 20))
        self.generate_one()

    def copy(self, other):
        self.decisions = other.decisions[:]
        self.cands = other.cands[:]
        self.decisionSpace = other.decisionSpace
        self.objectiveSpace = other.objectiveSpace

    def score(self):
        # use sum of objectives as score
        res = self.fi()
        val = 0.0
        for i in xrange(self.objectiveSpace - 1):
            val += self.energy(res[i], self.objs[i].lo, self.objs[i].hi)
            # print(val)
        return fabs(val/self.objectiveSpace)


    def fm(self, objectives):
        g = 1 + 9 / (self.decisionSpace - self.objectiveSpace + 1) * sum(self.cands[self.objectiveSpace :])
        h = self.objectiveSpace
        for x in range(self.objectiveSpace - 1):
            h += (objectives[x] / (1 + g)) * (1 + sin(3 * pi * objectives[x]))

        objectives.append((1 + g) * h)

    def fi(self):
        objectives = []

        # for fis before the last one
        for i in xrange(self.objectiveSpace - 1):
            objectives.append(self.cands[i])

        # calculate and append the last f
        self.fm(objectives)

        # return
        return objectives

    def cdom(self, other):
        def loss(xl, yl):
            n = len(xl)
            allloss = [-1 * e**(-1 * (xi - yi) / n) for xi,yi in zip(xl,yl)]

            return sum(allloss)/n

        x_objs = self.fi()
        y_objs = other.fi()

        l1 = loss(x_objs, y_objs)
        l2 = loss(y_objs, x_objs)
        return l2 - l1

    def findMinMax(self):
        for i in xrange(self.objectiveSpace):
            self.objs.append(Objective())

        for i in xrange(1000):
            self.any()
            res = self.fi()
            # print(res)
            for j in xrange(self.objectiveSpace):
                if (self.objs[j].hi < res[j]):
                    self.objs[j].hi = res[j]
                if (self.objs[j].lo > res[j]):
                    self.objs[j].lo = res[j]

    def energy(self, eval, min, max):
        # print(min, max)
        return (eval - min) / (max - min)


if __name__ == "__main__":
    DTLZ7 = DTLZ7()
    print(DTLZ7.cands)
    print(DTLZ7.fi())
    DTLZ7.findMinMax()
    print(DTLZ7.score())
    print(DTLZ7.objs[0].lo, DTLZ7.objs[0].hi, DTLZ7.objs[1].lo, DTLZ7.objs[1].hi)
