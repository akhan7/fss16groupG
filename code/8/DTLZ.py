import sys
from Problem import *

def generate_decision(num_dec):
    dec = []
    for i in range(num_dec):
        dec.append(Decision(str(i),0,1))
    return dec

def generate_objective(num_obj):
    obj  = []
    for i in range(num_obj):
        obj.append(Objective(str(i)))
    return obj


class DTLZ1(Problem):
    def __init__(self,num_obj=2,num_dec=10):
        name = "DTLZ({0},{1})".format(num_obj,num_dec)
        self.num_obj = num_obj
        self.num_dec = num_dec
        self.points = []
        decisions = generate_decision(self.num_dec)
        objectives = generate_objective(self.num_obj)
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(self, point):
        def minimize(i):
            return -1 if self.objectives[i].do_minimize else 1

        x = point.decisions[:]
        objs = []
        for i in xrange(self.num_obj):
            f1 = float(0.5*(1+self.g(self,x)))


            for j in xrange(0, self.num_obj-(i+1)):
                f1 *= float(x[j])
            f1*= float(1-float(x[self.num_obj-(i+1)]))
            objs.append(f1)

        point.objectives = objs[:]

        #print point.objectives
        #point.energy = int(f1 * minimize(0) + f2 * minimize(1))
        #for i in xrange(self.num_obj):
        #    point.energy += (point.objectives[i]*minimize(i))

        return point.objectives

    @staticmethod
    def g(self,x):
        total = 0
        for i in xrange(len(x)):
            total +=((x[i]-0.5)**2 - math.cos(20*math.pi * (x[i]-0.5)))
        return 100*(self.num_dec + total)

    @staticmethod
    def is_valid(self, point):
        return True

    def any(self, retries=500):
        for _ in xrange(retries):
            point = Point([random.uniform(0, 1) for d in self.decisions])
            if self.is_valid(self, point):
                self.evaluate(self, point)
                self.points.append(point)
                #print point.energy
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % retries)



class DTLZ3(Problem):
    def __init__(self,num_obj=2,num_dec=10):
        name = "DTLZ({0},{1})".format(num_obj,num_dec)
        self.num_obj = num_obj
        self.num_dec = num_dec
        self.points = []
        decisions = generate_decision(self.num_dec)
        objectives = generate_objective(self.num_obj)
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(self, point):
        def minimize(i):
            return -1 if self.objectives[i].do_minimize else 1
        x = point.decisions[:]
        objs=[]
        for i in xrange(self.num_obj):
            f1 = 1+self.g(self,x)
            for j in xrange(0, self.num_obj-(i+1)):
                f1 *= math.cos(x[j]*math.pi / 2)
            if i==0 :
                f1 *= math.cos(x[j]*math.pi / 2)
            else:
                f1 *= math.sin(x[j]*math.pi / 2)
            objs.append(f1)
        point.objectives = objs[:]

        #print point.objectives
        #point.energy = int(f1 * minimize(0) + f2 * minimize(1))
        # for i in xrange(self.num_obj):
        #     point.energy += (point.objectives[i]*minimize(i))

        return point.objectives

    @staticmethod
    def g(self,x):
        total = 0
        for i in xrange(len(x)):
            total +=((x[i]-0.5)**2 - math.cos(20*math.pi * (x[i]-0.5)))
        return 100*(self.num_dec + total)

    @staticmethod
    def is_valid(self, point):
        return True

    def any(self, retries=500):
        for _ in xrange(retries):
            point = Point([random.uniform(0, 1) for d in self.decisions])
            if self.is_valid(self, point):
                self.evaluate(self, point)
                self.points.append(point)
                #print point.energy
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % retries)



class DTLZ5(Problem):
    def __init__(self,num_obj=2,num_dec=10):
        name = "DTLZ({0},{1})".format(num_obj,num_dec)
        self.num_obj = num_obj
        self.num_dec = num_dec
        self.points = []
        decisions = generate_decision(self.num_dec)
        objectives = generate_objective(self.num_obj)
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(self, point):
        def minimize(i):
            return -1 if self.objectives[i].do_minimize else 1
        x = point.decisions[:]

        def theta(value):
            return math.pi * (1+2*self.g(self,x) *value) / (4 * (1+self.g(self,x)))
        objs=[]
        for i in xrange(self.num_obj):
            f1 = 1+self.g(self,x)

            for j in xrange(0, self.num_obj-(i+1)):
                f1 *= math.cos(theta(x[j]) * math.pi / 2)
            if i==0 :
                f1 *= math.cos(theta(x[j]) *math.pi / 2)
            else:
                f1 *= math.sin(theta(x[j]) *math.pi / 2)
            objs.append(f1)

        point.objectives = objs[:]

        #print point.objectives
        #point.energy = int(f1 * minimize(0) + f2 * minimize(1))
        # for i in xrange(self.num_obj):
        #     point.energy += (point.objectives[i]*minimize(i))

        return point.objectives
    @staticmethod
    def g(self,x):
        total = 0
        for i in xrange(len(x)):
            total +=((x[i]-0.5)**2)
        return total

    @staticmethod
    def is_valid(self, point):
        return True

    def any(self, retries=500):
        for _ in xrange(retries):
            point = Point([random.uniform(0, 1) for d in self.decisions])
            if self.is_valid(self, point):
                self.evaluate(self, point)
                self.points.append(point)
                #print point.energy
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % retries)



class DTLZ7(Problem):
    def __init__(self,num_obj=2,num_dec=10):
        name = "DTLZ({0},{1})".format(num_obj,num_dec)
        self.num_dec = num_dec
        self.num_obj = num_obj
        self.points = []
        decisions = generate_decision(self.num_dec)
        objectives = generate_objective(self.num_obj)
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(self, point):
        def minimize(i):
            return -1 if self.objectives[i].do_minimize else 1
        x = point.decisions[:]

        objs = []
        for i in xrange(self.num_obj - 1):
            objs.append(x[i])

        objs.append((1+self.g(self,x))*self.h(self,objs[:],self.g(self,x),self.num_obj))


        point.objectives = objs[:]
        #print point.objectives
        #point.energy = int(f1 * minimize(0) + f2 * minimize(1))
        return point.objectives

    @staticmethod
    def g(self,x):
        s = sum(x)
        return 1+ ((9/len(x))*s)

    @staticmethod
    def h(self,f,g,M):
        #angle = 3*math.pi*f
        #return M - ((f/(1+g))* (1+math.sin(angle)))
        total = 0
        for i in xrange(len(f)):
            total += (f[i] / (1 + g) * (1 + math.sin(3 * math.pi * f[i])))
        return M - total

    @staticmethod
    def is_valid(self, point):
        return True


    def any(self, retries=500):
        for _ in xrange(retries):
            point = Point([random.uniform(0, 1) for d in self.decisions])
            if self.is_valid(self, point):
                self.evaluate(self, point)
                self.points.append(point)
                #print point.energy
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % retries)
