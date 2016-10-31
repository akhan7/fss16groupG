from __future__ import division, print_function
from random import *
import random
import math
from schaffer import Schaffer


class SA:
    def __init__(self, model):
        self.model = model
        self.kmax = 5000

    def get_prob(self, e, en, t):
        """Computes acceptance function"""
        return math.exp((e - en) / t)

    def run(self):
        """Simulated annealing for schaffer model"""

        s = self.model.generate_one()
        e = self.model.evaluate(s)

        print("Initial (s , e) ", s, e, end='\n')

        sb = s
        eb = e

        k = 1

        while k < self.kmax and eb > 0:
            sn = self.model.generate_one()
            en = self.model.evaluate(sn)

            if k == 1 or k % 25 == 0: print("\n,%d, %.2f, " % (k, eb), end="")

            if en < eb:
                sb = sn
                eb = en
                print("!", end='')

            if en < e:
                s = sn
                e = en
                print("+", end='')

            elif self.get_prob(e, en, k / float(self.kmax)) < random.random():
                s = sn
                e = en
                print("?", end='')

            print(".", end='')
            k += 1

        print("\n\nkmax = ", self.kmax, end="\n")
        print("The best attainable solution : ", self.model.min , self.model.min_point)
        print("The attained solution by simuated annealing : ", self.model.denormalize(eb), " at ", sb)

        return sb, eb, self.model.min, self.model.max  # print get_min_max(SCHAFFER_X_MIN, SCHAFFER_X_MAX)


SA(Schaffer()).run()
