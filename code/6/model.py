import random


class Model:
    def __init__(self, decisions, objectives, constraints=None):
        self.decisions = decisions
        self.objectives = objectives
        self.constraints = constraints
        self.min, self.max, self.min_point, self.max_point = self.get_min_max()

    def __eval(self, point):
        sum = 0
        for objective in self.objectives:
            sum += objective(point)
        return sum

    def evaluate(self, point):
        return self.normalize(self.__eval(point))

    def is_valid(self, point):
        if self.constraints != None:
            return self.constraints(point)
        return True

    def generate_one(self, retries=20):
        while True:
            point = []
            for decision in self.decisions:
                point.append(random.randint(decision.low, decision.high))
            valid = self.is_valid(point)
            if valid:
                if len(point) == 1:
                    return point[0]
                return point

    def get_min_max(self, retries=1000):
        min_sc = min_point = float('inf')
        max_sc =  max_point = float('-inf')

        for i in xrange(retries):
            point = self.generate_one()
            curr = self.evaluate(point)
            if curr < min_ener:
                min_ener = curr
                min_point = point
            if curr > max_ener:
                max_ener = curr
                max_point = point

        return (min_ener, max_ener, min_point, max_point)

    def normalize(self, score):
        return (score - self.min) / float(self.max - self.min)

    def denormalize(self, normal_val):
        """Converts normalized value to actual value"""
        return normal_val * (self.max - self.min) + self.min
