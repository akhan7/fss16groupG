import random
from random import uniform


class Model(object):
    def generate_one(self):
        while True:
            self.cands = []
            for dec in self.decisions:
                self.cands.append(uniform(dec.lo, dec.hi))
            if self.check():
                break

    def check(self):
        for i in range(0, len(self.decisions)):
            if self.cands[i] < self.decisions[i].lo or self.cands[i] > self.decisions[i].hi:
                return False
        return True
