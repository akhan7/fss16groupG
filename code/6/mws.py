from __future__ import division, print_function
from random import *
import random
import math
from schaffer import Schaffer
from kursawe import Kursawe
from osyczka2 import Osyczka2


class MWS:
    def __init__(self, model):
        self.model = model
        self.max_tries = 100
        self.max_changes = 20
        self.threshold = 0.05
        self.prob = 0.5

    def run(self):
        """Run max walk sat on model"""

        best = self.model.generate_one()
        for i in xrange(self.max_tries):

            curr = self.model.generate_one()

            for j in xrange(self.max_changes):

                if self.model.evaluate(curr) < self.model.evaluate(best):
                    best = curr[:]
                    print("!", end='')

                if self.prob < random.random():
                    prev = curr[:]
                    curr = self.__mutate_any(curr)
                else:
                    prev = curr[:]
                    curr = self.__mutate_all(curr)

                if self.model.evaluate(curr) < self.model.evaluate(best):
                    best = curr[:]
                    print("!", end='')
                elif self.model.evaluate(curr) < self.model.evaluate(prev):
                    print("+", end='')
                else:
                    print(".", end='')
            print(", ", round(self.model.evaluate(best), 5))
        print("#iterations:", self.max_tries)
        print("best solution:", best)
        print("best score:", self.model.evaluate(best))

    def __mutate_any(self, x):
        x_backup = x[:]
        i = randint(0, len(x) - 1)
        x[i] = randint(self.model.decisions[i].low, self.model.decisions[i].low)

        local_tries = 50
        while not self.model.is_valid(x) and local_tries >= 0:
            x[i] = randint(self.model.decisions[i].low, self.model.decisions[i].low)
            local_tries -= 1

        if local_tries == -1:
            return x_backup

        return x

    def __mutate_all(self, x):
        maximized_sol = x[:]

        for i in xrange(len(x)):
            for val in xrange(self.model.decisions[i].low, self.model.decisions[i].low):
                x[i] = val
                if self.model.is_valid(x) and self.model.evaluate(x) < self.model.evaluate(maximized_sol):
                    maximized_sol = x[:]

        return maximized_sol


MWS(Schaffer()).run()
MWS(Osyczka2()).run()
MWS(Kursawe()).run()
