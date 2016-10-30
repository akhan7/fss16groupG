from __future__ import print_function
import random
import math



class Model(object):
    def __init__(self,decisions,objectives,constraints):
        self.decisions = decisions
        self.objectives = objectives
        self.constraints = constraints

    @staticmethod
    def evaluate(point):
        assert False
        return point.objectives

    @staticmethod
    def is_valid(point):
        return True

    def generate_one(self, retries=20):
        for _ in xrange(retries):
            point = Point([random_value(d.low, d.high) for d in self.decisions])
            if self.is_valid(point):
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % 20)





