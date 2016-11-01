import sys
from sa import SA
from mws import MWS
from osyczka2 import Osyczka2
from kursawe import Kursawe
from schaffer import Schaffer

for model in [Schaffer, Osyczka2, Kursawe]:
    for optimizer in [SA, MWS]:
           optimizer(model()).run()