from __future__ import print_function
import random
import math


def r(a=0, b=1): return random.randint(a, b)


class Osyczka:
    def min_max(self, tries):
        i = 0
        min = float('inf')
        max = float('-inf')

        while i < tries:
            x = self.rand_tuple()
            if self.constraints(x):
                oval = self.osyczka(x)
                if oval < min:
                    min = oval
                if oval > max:
                    max = oval
                i += 1

        return min, max

    def get_threshold(self, g_min, g_max, tries):
        i = 0
        aggregate_diff = 0
        while i < tries:
            min, max = self.min_max(1000)
            if min > g_min and max < g_max:
                aggregate_diff += self.get_normalized(min, g_min, g_max)
                i += 1

        return aggregate_diff / float(tries)

    def get_normalized(self, x, g_min, g_max):
        return ((x) - g_min) / float(g_max - g_min)

    def osyczka(self, x):
        return self.__f1(x) + self.__f2(x)

    def constraints(self, x):
        return self.__g1(x) >= 0 and self.__g2(x) >= 0 and self.__g3(x) >= 0 and self.__g4(x) >= 0 \
               and self.__g5(x) >= 0 and self.__g6(x) >= 0

    def rand_tuple(self):
        return (r(0, 10), r(0, 10), r(1, 5), r(0, 6), r(1, 5), r(0, 10))

    def __f1(self, x):
        return -25 * pow(x[0] - 2, 2) - pow(x[1] - 2, 2) \
               - pow(x[2] - 1, 2) - pow(x[3] - 4, 2) - pow(x[4] - 1, 2)

    def __f2(self, x):
        sum = 0
        for i in xrange(len(x)):
            sum = sum + pow(x[i], 2)
        return sum

    def __g1(self, x):
        return x[0] + x[1] - 2

    def __g2(self, x):
        return 6 - x[0] - x[1]

    def __g3(self, x):
        return 2 - x[1] + x[0]

    def __g4(self, x):
        return 2 - x[0] + 3 * x[1]

    def __g5(self, x):
        return 4 - pow(x[2] - 3, 2) - x[3]

    def __g6(self, x):
        return pow(x[4] - 3, 2) + x[5] - 4


class MaxWalkSat:
    def solve(self, max_tries):
        return None


if __name__ == '__main__':
    o = Osyczka()
    min, max = o.min_max(5000)

    print(min, max)
    print(o.get_threshold(min, max, 10))
