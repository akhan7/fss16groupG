# ASE Fun project

#Time table Scheduling 

### Why?
There are certain class of problems called NP Hard and one of the ways of solving these problems
is through randomization and by the use of meta heuristics which is what 
We've been learning throughout the semester in **`CSC591 ASE`**

### Problem Statement
>Time table scheduling problem is a multi constrained , NP Hard , combinatorial 
optimization problem. One of the derivative of this problem is Examination
time tabling problem which takes in a list of courses offered by a university and schedules
the list of students enrolled in these courses and schedules the exams in
such a way that there are no overlaps for a student and the exams
are scheduled as far as possible within a specified window of dates.


### Description
* Decisions : 
    * A set of time slots (contiguous) T
    * A set of courses C
    * A set of Students S
    * A set of student enrollments E (Ideally a pair of Student Number and Course ID)

* Objectives :
    
    * The objective of the problem is to minimize the proximity cost.
    
    According to [this](#4) paper there are two sources of cost namely **"Soft constraints"** and **"Hard constraints"**
    
    In simple terms soft constraint occurs when a student has two exams in adjacent slots and hard
    constraints occur when the student has two exams in the same slot.
    
    This the proximity cost is the sum of these costs divided by the number of students
    
    ![costs](./pics/cost.PNG)


### What algorithms can we use to optimize this problem?

During the course we have come across a variety of meta heuristic algorithms like Simulated Annealing, 
Genetic algorithm , Particle Swarm optimization and so on. >>> Just for fun read about  **Ant colony Optimization** and try 
when you get time <<<<

* #### Simulated Annealing :
Simulated annealing (SA) is a probabilistic technique for approximating the global optimum of a given function. Specifically, it is a metaheuristic to approximate global optimization in a large search space. 
It is often used when the search space is discrete (e.g., all tours that visit a given set of cities). Simulated annealing interprets slow cooling as a slow decrease in the probability of accepting worse solutions as it explores the solution space. Accepting worse solutions is a fundamental property of
metaheuristics because it allows for a more extensive search for the optimal solution.<sub>Taken from wikipedia</sub>

* #### Genetic Algorithm :
In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems 
by relying on bio-inspired operators such as mutation, crossover and selection.

* #### PSO : 
Particle swarm optimization (PSO) is a computational method that optimizes a problem by 
iteratively trying to improve a candidate solution with regard to a given measure of quality. It solves a problem by having a population of candidate solutions, here dubbed particles, and moving these particles around in the search-space according to simple mathematical formulae over the particle's position and velocity. Each particle's movement is influenced by its local best known position, but is also guided toward the best known positions 
in the search-space, which are updated as better positions are found by other particles. <sub>Taken from class notes</sub>

* #### ACO :



### Papers on using evolutionary algorithms for Time table Scheduling

* J. M. Thompson and K. A. Dowsland,A Robust Simulated Annealing Based Examination Timetabling System, Computers and Operations Researchs25(7/8) (1998), 637-648. 
* M. W. Carter,A survey of practical applications of Examination Timetabling Algorithms, Operation Research34(2) (1986), 193-202. 
* A. Colorni, M. Dorigo and V. Maniezzo,Genetic Algorithms: A New Approach to the Timetabling Problem, The practic and theory of automated timetabling, Lecture Notes in Computer Science, eds. E. Burke and P. Ross. Springer1153(1996), 235-239. 
* <a name="4"></a>M. W. Carter, G. Laporte and S. Y. Lee,Examination Timetabling: Algorithmic Strategies and Applications, Journal of the Operational Research Society47(1996), 373-383.

