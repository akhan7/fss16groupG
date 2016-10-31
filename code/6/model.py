import random


class Model:
    def __init__(self, decisions, objectives, constraints=None):
        self.decisions = decisions
        self.objectives = objectives
        self.constraints = constraints

    def evaluate(self, point):
        sum = 0
        for objective in self.objectives:
            sum += objective(point)

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
