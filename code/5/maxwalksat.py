from __future__ import print_function
import random
import math


class Osyczka:
    def f1(self, x):
        return -25 * pow(x[0] - 2, 2) - pow(x[1] - 2, 2) \
               - pow(x[2] - 1, 2) - pow(x[3] - 4, 2) - pow(x[4] - 1, 2)

    def f2(self, x):
        sum = 0
        for i in xrange(len(x)):
            sum = sum + pow(x[i], 2)
        return sum

    def constraints(self, x):
        return self.__g1(x) >= 0 and self.__g2(x) >= 0 and self.__g3(x) >= 0 and self.__g4(x) >= 0 \
        and self.__g5(x) >= 0 and self.__g6(x) >= 0
    

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


if __name__ == '__main__':
    o = Osyczka()
    print(o.f1((1, 2, 3, 4, 5, 6)))
    print(o.f2((1, 2, 3, 4, 5, 6)))
    print(o.constraints((0, 1, 3, 4, 5, 6)))
