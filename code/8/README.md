## Homework 8 Implemment NSGA-II

### Running Instructions 
  1. Clone the github repository fss16groupG from https://github.com/akhan7/fss16groupG.git
  2. Navigate to ./fss16groupG/code/8
  3. run testGA.py
 
###Abstract
The objective is to extend the implementation of GA done in the workshops to implement NSGA-II algorithm with the two types of fitness evaluations- Binary Domination with Cuboid Sorting and Continuous Domination. We test the algorithm by running it with each of the DTLZ 1, DTLZ 3, DTLZ 5 and DTLZ 7 models with 2, 4, 6, 8 objectives and with 10, 20, 40 decisions. Default parameters are used during the implementation and hypervolume is used as the performance measure. We repeat this experiment with 20 iterations.

###Introduction
*Genetic algorithm* is a meta-heuristic algorithm which is inspired from natural selection. It traditionally works on binary data but can be adopted for other data types as well. It uses techniques like Cross over, mutation and Elitism to evaluate fitness generate better population of candidate solutions.

*NSGA-II* is a standard genetic algorithm with state-of-the-art selection operator for multi-objectives. The algorithm for NSGA-II is given as:
  * Divide candidates into frontiers:
  * For some small number:
    * Keep the top i-frontiers until we reach that number
    * If you fill up half way through a frontier,
    * Delete some using crowd-pruning

The fitness evaluation of the population is done through two major algorithms, Binary Domination with Cuboid Sorting and Continuous Domination. 

Binary domination is a very fast and simple algorithm which is defined as follows:
  * Consider two points one and two.
  * For every objective o and t in one and two, o <= t
  * Atleast one objective o and t in one and two, o < t

However it is not the best method to evaluate fitness as it can be too simplistic to


###Implementation 


###Results



###Conclusions

###Threats to Validity 
1. We ran the code only for the given default values . We could run the code for different sets of default values and try to 
   decide which set of default paramters works the best. 
2. There is a discrepancy observed for DTLZ3 with 8 objectives and 20 and 40 decisions.
3. We use Hypervolume function to measure performance. There are multiple other tools which could be used. The given results might 
   be skewed because of the use of Hypervolume. 
4. The early termination condtion may be terminating a loop prematurely when a better candidate could be found.

###Future Work 
1. We could generate multiple instances of the default values and generate the graphs for those and then decide which 
   set of values work the best. 
2. Instead of just using hypervolume , we could also use spread or the loss and compute multiple graphs. Instead on measuring 
   performance based on just hypervolume , we could base it on all three of the parameters and then conclude results.
3. The early termination condition could be changed to a more lenient one , we could instead terminate when there are two instances
   of the chid frontier not doing any better. 
4. GA could be extended to multiple other models and the efficiency of it to optimize other models could be measured as well. 

###References:-

 1. [Pseudo-code for Genetic Algorithm](http://www.cleveralgorithms.com/nature-inspired/evolution/genetic_algorithm.html)
 2. Book : Clever Algorithms by Jason Brownlee
 3. https://github.com/txt/mase/blob/master/lessthan.md
 4. https://github.com/txt/mase/blob/master/STATS.md
 5. https://en.wikipedia.org/wiki/Genetic_algorithm


###Acknowledgements

   The study uses code found here :
 1.  This study uses code for Scott Knott given here : https://github.com/txt/mase/blob/master/src/doc/sk.py
 2.  This study used Hypervolume functions given here: 
     [Hypervolume Calculator](https://github.com/ai-se/storm/tree/master/PerformanceMetrics) 
