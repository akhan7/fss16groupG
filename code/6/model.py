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

    def get_min_max(self, retries=100):
        points = []
        for i in xrange(retries):
            points.append(self.__eval(self.generate_one()))

        return min(points), max(points)

    def normalize(self, score):
        return (score - self.min) / float(self.max - self.min)
