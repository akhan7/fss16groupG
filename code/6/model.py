import random


class Model:
    def __init__(self, decisions, objectives, constraints=None):
        self.decisions = decisions
        self.objectives = objectives
        self.constraints = constraints
        self.min, self.max = self.get_min_max()

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

    def generate_one(self):
        while True:
            point = []
            for decision in self.decisions:
                point.append(random.randint(decision.low, decision.high))
            valid = self.is_valid(point)
            if valid:
                return point

    def get_min_max(self, retries=1000):
        scores = []
        for i in xrange(retries):
            scores.append(self.__eval(self.generate_one()))

        return min(scores), max(scores)

    def normalize(self, score):
        return (score - self.min) / float(self.max - self.min)

    def denormalize(self, normal_val):
        """Converts normalized value to actual value"""
        return normal_val * (self.max - self.min) + self.min
