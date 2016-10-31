from __future__ import division, print_function
from random import *
import random
import math


class SA:
    def __init__(self, model):
        self.model = model
        self.kmax = 1000
        self.iter = 100

    def get_random_min_max(self):
        """Function to get the min and max values from 'iter' simulations"""
        ind = 0
        min_ener = float('inf')
        max_ener = float('-inf')

        while ind < self.iter:
            x = self.model.generate_one()
            curr = self.model.is_valid(x)
            if curr < min_ener:
                min_ener = curr
            if curr > max_ener:
                max_ener = curr
            ind += 1

        return (min_ener, max_ener)

    def run(self):
        """Simulated annealing for schaffer model"""
        min_ener, max_ener = self.get_random_min_max()

        s = self.model.generate_one()

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
