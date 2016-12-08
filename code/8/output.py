from NSGA2 import *
from DTLZ import *
from performance import *
from hypervolume import *
from stats import rdivDemo as sk
models = [DTLZ1,DTLZ3,DTLZ5,DTLZ7]
for model in models:
    for num_obj in [2, 4, 6, 8]:

        hyperVolume = []
        run_stats = []
        for num_dec in [10, 20, 40]:
            for dom in [bdom,cdom]:
                avg_vol = 0
                avg_runs = 0
                repeats = 1
                info_hv = [model.__name__ + " " + str(num_obj) + " " + str(num_dec) + " " + dom.__name__]
                info_runs = [model.__name__ + " " + str(num_obj) + " " + str(num_dec) + " " + dom.__name__]
                for x in range(repeats):
                    problem = model(num_obj, num_dec)
                    hypervolume = nsga2(problem,dom_func=dom)

                    info_hv.append(hypervolume)
                hyperVolume.append(info_hv)
  
        sk(hyperVolume)
        print str(num_obj) +" Objectives done for model " + model.__name__
