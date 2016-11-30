from dtlz7 import DTLZ7
from optimizers import mws,de,sa
from stats import rdivDemo

if __name__ == '__main__':
    repeats = 20
    # repeats = 1
    for model in [DTLZ7]:
        data = []
        for i,optimizer in enumerate([sa,mws,de]):
            opt_rpt = []
            opt_rpt.append(optimizer.func_name)
            for j in range(repeats):
                baseline = [model() for _ in xrange(repeats)]
                pre = model()
                pre.copy(baseline[j])
                res = optimizer(model, baseline[j])
                opt_rpt.append(res.cdom(pre))
                # print(res.candidates)
                # opt_rpt.append(res.score() * 1000)
            data.append(opt_rpt)
        rdivDemo(data)