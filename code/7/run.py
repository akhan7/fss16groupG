from dtlz7 import DTLZ7
from sa import sa
from mws import mws
from de import de
from stats import rdivDemo

all_eras = []

for iteration in range(20):

    for model in [DTLZ7]:

        era_size = 100

        era0 = []

        while len(era0) < era_size:
            model_instance = model()
            can = model_instance.gen_candidate()
            if can:
                era0 += [can]

        for optimizer in [de]:  # mws, de]:
            print "."

            # print "\n*****************************"
            # print optimizer.__name__ + "(" + model.__name__ + ")"
            best_can, best_score, last_era = optimizer(model_instance, threshold=-1000, max_tries=10000,
                                                       era_size=era_size, era0=era0)
            # era_scores = [model_instance.aggregate(x) for x in last_era]
            era_score = [0 for _ in range(len(last_era[0]))]
            for can_num in range(len(era_score)):
                for obj_num in range(len(last_era)):
                    era_score[can_num] += last_era[obj_num][can_num]

            era_score.insert(0, optimizer.__name__ + str(iteration))
            # print era_score
            all_eras.append(era_score)
            # print "*****************************\n"

rdivDemo(all_eras)
