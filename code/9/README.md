### Tuning Genetic Algorithm using Differential Evolution (Optimizing an optimizer)

### Running Instructions

1. Clone the github repository fss16groupG from https://github.com/akhan7/fss16groupG.git
2. Navigate to ./fss16groupG/code/9
3. run run.py


### Abstract

In this experiment we would be using Differential Evolution to optimize the parameters of GA which in turn tries to optimize DLTZ1,3,5,7 models over 2,4,6,8 objectives and 10,20,40 decisions. 
In other words we are trying to optimize an optimizer. We will be comparing the solutions generated by untuned GA (with default parameters) with the solution generated by tuned GA (with optimized parameters) and see if we actually achieve improvements.

### Introduction

> What is Genetic Algorithm (GA)?

Genetic Algorithms were invented to mimic some of the processes observed in natural evolution. Many people, biologists included, are astonished that life at the level of complexity that we observe could have evolved in the relatively short time suggested by the fossil record. The idea with GA is to use this power of evolution to solve optimization problems.

Genetic Algorithms (GAs) are adaptive heuristic search algorithm based on the evolutionary ideas of natural selection and genetics. As such they represent an intelligent exploitation of a random search used to solve optimization problems. Although randomised, GAs are by no means random, instead they exploit historical information to direct the search into the region of better performance within the search space.

"Survival of the fittest" is the basic principle behind GA's. [1]

> Operators of GA

After an initial population is randomly generated, the algorithm evolves the through three operators:
* **Selection** which equates to survival of the fittest;
* **Crossover** which represents mating between individuals;
* **Mutation** which introduces random modifications.

> Parameters required by GA

* Population Size
* Number of Generations
* Crossover probability
* Mutation probability 

> What is Differential Evolution (DE) ?

Differential evolution optimizes a problem by maintaining a population of candidate solutions and creating new candidate solutions by combining existing ones according to a formula which depends on
 the variation of DE being used, and then keeping whichever candidate solution has the best score or fitness on the optimization problem at hand. It makes few or no assumptions about the problem being optimized and can search very large spaces of candidate solutions.

DE replaces the currently selected candidate immediately if the new candidate formed by extrapolation is better than it. Hence it doesn't need one to one comparison with each of the existing candidates to maintain best solutions. In this way it is much better than GA.

In this experiment we do the following
* Extrapolate from some candidate X, chosen at random.
* Add in values from one other extrapolation (Y-Z)
* DE is used to try and optimize the parameters of the GA to get better results for DTLZ5 with 10 decision values and 2 objective functions

### Implementation

1. The model used is DLTZ 1, 3, 5 and 7 with 2, 4, 6 objectives and 10, 20 and 40 decisions.

2. Genetic Algorithm is developed to optimize the objectives of the above model. From the finally obtained frontier, the distance From Hell is calculated by finding the nearest neighbor in the baseline frontier and determining the distance between these points. The mean of all these distances is used as the aggregate score of the GA for comparison basis.

3. A model encompassing the GA parameters in written as follows. 

```python
  def ga(model, b_min, b_max, b_pop, num_can, num_gen, p_mut, p_cros):
    population_size = num_can
    generations = num_gen 
    p_crossover = p_cros 
    p_mutation = p_mut 
    total_decs = 10
    total_objs = 2
    base_min = b_min
    base_max = b_max
```

4. The Differential Evolution model is implemented which works on the GA candidates. It generates an initial frontier of candidates, and then iterates over the number of repeats trying to mutate the parameters of configuration so as to obtain the maximum distance from Hell (farther points result in more optimized objectives).

5. The final result is the best GA configuration, with the corresponding distance value, and the final populated frontier of configurations ranked based on the distance metric.

6. The best configuration is fed into GA optimizer for optimizing the given models to find the resulting mean distance and the solution obtained is compared with the solution obtained from untuned GA with default parameters.

### Results
Genetic Algorithm's parameters have been tuned with the help of DE. Normalized hypervolume is used as the performance measure to compare the tuned and untuned GA. We've plotted graphs depicting the normalized hypervolume values for tuned GA's for each of the models. We've also compared the tuned and untuned GA's by plotting and comparing their corresponding hypervalues. As we'll see from the graphs, the tuned GA performs significantly better as compared to the untuned GA.

#### Tuned GA (DTLZ 1)
The graph below shows the normalized hypervolume of the tuned GA tested with DTLZ 1 model. As the number of objectives decrease, the hypervolume also shows a significant increase. 

![DTLZ 1 Results](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/r1.jpeg)

Comparing the tuned vs untuned GA, we can see the significant increase of the hypervolume value for the tuned GA as compared to the untuned one.

![DTLZ 1 Comparison](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/e1.jpeg)

#### Tuned GA (DTLZ 3)
The graph below shows the normalized hypervolume of the tuned GA tested with DTLZ 3 model. What is surprising is the sharp increase of objective 4 20 decision value of hypervolume. The value of 2 Objective hypervolume is much higher than the other objectives. Testing with this model, the change in decision space doesn't seem to affect the performance of the GA.

![DTLZ 3 Results](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/r2.jpeg)

Comparing the tuned vs untuned GA, we can see the significant increase of the hypervolume value for the tuned GA as compared to the untuned one.

![DTLZ 3 Comparison](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/e2.jpeg)

#### Tuned GA (DTLZ 5)
The graph below shows the normalized hypervolume of the tuned GA tested with DTLZ 5 model. As the number of objectives decrease, the hypervolume also shows an increase. An interesting thing to observe is that the value 2 objective 40 decisions hypervolume is much higher than the other hypervolume values. The hypervolume values in Objective 2 only show variations with decision space, the higher objectives do not have a significant variation in their hypervolume values.

![DTLZ 5 Results](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/r3.jpeg)

Comparing the tuned vs untuned GA, it is surprising to see that in case of DTLZ 5 the untuned GA has performed better than the tuned GA. This is indicative of the probabilistic nature of these algorithms as sometimes even with tuning being done to the algorithms, unexpected results may arise.

![DTLZ 5 Comparison](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/e3.jpeg)

#### Tuned GA (DTLZ 7)
The graph below shows the normalized hypervolume of the tuned GA tested with DTLZ 7 model. In the case of DTLZ 7, the hypervolume values differ according to their decision space and not their objective space where they are fairly consistent. They have slight variations with lower decision values resulting in higher hypervolume values.

![DTLZ 7 Results](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/r4.jpeg)

Comparing the tuned vs untuned GA, the hypervolume for the tuned GA is higher than the untuned GA. But in constrast to the other models, here the variation in hypervolume value is not as significant as compared to DTLZ models 1, 3 and 5.

![DTLZ 7 Comparison](https://github.com/akhan7/fss16groupG/blob/master/code/9/image/e4.jpeg)

**One of the issues we faced was the runtime of the algorithm. As the number of objectives 
increased, the number of computations also increased dramatically. This comes as no surprise because
as more and more contradicting objectives are added, the hypervolume decreases and during creating a random candidate / mutated candidate,
the algorithm won't be able to find a valid candidate in the first place and won't be able to move forward **
### Conclusion
* This experiment has enlightened us more about Genetic Algorithm and Differential Evolution as well as different topics around them. 
* Thus, from our experiments, we conclude that Differential Evolution does improve the performance of a Genetic Algorithm. 
* We also observed that generally if the objective space is less, the hypervolume is more.
* Also if the GA is tuned, the results are way better than for untuned GAs.


### Threats to validity
1. The pareto frontier in this experiment uses a lot of time, resulting in increased time complexity.
2. The BDOM, used in the experiment, might not be that effective for every kind of data.
3. If different model is used, the results might not be the same.

### Future work
1. In the future we would like to improve the performance of the algorithm by improving the time complexity of the algorithm.
2. We would also suggest including parallel running of processes to increase the efficiency. 
3. Also memory required for the algorithm can be optimized. 
4. Also we intend to improve the results by using CDOM instead of BDOM and by performing more experiments. 


### References
[1][https://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol1/hmw/article1.html](https://www.doc.ic.ac.uk/~nd/surprise_96/journal/vol1/hmw/article1.html)
