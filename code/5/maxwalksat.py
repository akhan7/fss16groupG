from __future__ import print_function

import copy
import random


def r(a=0, b=1): return random.randint(a, b)


class Osyczka:
    """
    Utility class to solve the Osyczka2 equation
    """

    def min_max(self, tries):

        """
        Args:
            tries: number of tries / iterations

        Returns: A tuple of the minimum and absolute maximum of Osyczka2 function

        """
        i = 0
        min = float('inf')
        max = float('-inf')

        while i < tries:
            x = self.rand_list()
            if self.constraints(x):
                oval = self.osyczka(x)
                if oval < min:
                    min = oval
                if oval > max:
                    max = oval
                i += 1

        return min, max

    def get_threshold(self, g_min, g_max, tries):
        """

        Args:
            g_min: Min Value (found from min_max())
            g_max: Max Value (found from min_max())
            tries: Number of iterations

        Returns: Normalized threshold value averaged over "tries" number of iterations

        """
        i = 0
        aggregate_diff = 0
        while i < tries:
            min, max = self.min_max(1000)
            if min > g_min and max < g_max:
                aggregate_diff += self.get_normalized(min, g_min, g_max)
            i += 1

        return aggregate_diff / float(tries)

    def get_normalized(self, x, g_min, g_max):
        """

        Args:
            x: Value to be normalized
            g_min: Min value
            g_max: Max value

        Returns: Normalized value of x

        """
        return ((x) - g_min) / float(g_max - g_min)

    def osyczka(self, x):
        """

        Args:
            x: Independent variable

        Returns:
            value of Osyczka function at x

        """
        return self.__f1(x) + self.__f2(x)

    def constraints(self, x):
        """

        Args:
            x: List of 6 elements representing

        Returns: True if the contraints pass, False otherwise.

        """
        return self.__g1(x) >= 0 and self.__g2(x) >= 0 and self.__g3(x) >= 0 and self.__g4(x) >= 0 \
               and self.__g5(x) >= 0 and self.__g6(x) >= 0

    def rand_list(self):
        """

        Returns:  A random list of 6 integers

        """
        return [r(0, 10), r(0, 10), r(1, 5), r(0, 6), r(1, 5), r(0, 10)]

    def __f1(self, x):
        return -(25 * pow(x[0] - 2, 2) + pow(x[1] - 2, 2) \
                 + pow(x[2] - 1, 2) * pow(x[3] - 4, 2) + pow(x[4] - 1, 2))

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
        return pow(x[4] - 3, 3) + x[5] - 4


class MaxWalkSat:
    @staticmethod
    def solve(max_tries):
        o = Osyczka()

        # Get min and max over thousand tries
        g_min, g_max = o.min_max(1000)
        print("The global min,max for normalization : ", g_min, g_max)

        # Get threshold over 10 tries (Internally uses min_max(1000))
        # threshold = o.get_threshold(g_min, g_max, 10)
        threshold = 0.06;
        print("Stopping condition (threshold) : ", threshold)

        solution = o.rand_list()
        while not o.constraints(solution):
            solution = o.rand_list()

        for i in xrange(max_tries):
            # print(solution)
            if o.constraints(solution) and o.get_normalized(o.osyczka(solution), g_min, g_max) < threshold:
                return ("SUCCESS", solution, o.osyczka(solution),i)

            c = r(0, 5)
            if 0.5 < random.random():
                solution[c] = o.rand_list()[c]

            else:
                # Throw away solution
                prev_solution = copy.deepcopy(solution)
                solution = o.rand_list()
                while not o.constraints(solution) and o.get_normalized(o.osyczka(solution), g_min,
                                                                       g_max) < o.get_normalized(
                    o.osyczka(prev_solution), g_min, g_max):
                    solution = o.rand_list()

        return ("FAILURE", solution, o.osyczka(solution),i)


if __name__ == '__main__':
    print(MaxWalkSat.solve(1000))
