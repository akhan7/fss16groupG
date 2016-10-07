###Paper Title – 

####Search-Based Duplicate Defect Detection: An Industrial Experience
*Mehdi Amoui, Nilam Kaushik, Abraham Al-Dabbagh, Ladan Tahvildari, Shimin Li, Weining Liu*

###Keywords - 

####ii1.Duplicate defects: 
Multiple defects whose root cause is identical (method call, memory problems, runtime errors). Fixing one defect usually leads to the other being fixed as well.
 
####ii2.Parameter tuning: 
Parameter tuning is the the process of finding and setting an optimal value of the parameters that determine a system’s characteristics. The process can be  specified by the parameters and the tuning procedure. Parameter tuning is an offline procedure in which parameter values remain fixed during the run, and should be distinguished from parameter control in which initial parameter values are changed during the run.

####ii3.Information retrieval: 
is the activity of obtaining information resources relevant to an information need from a collection of information resources.

####ii4.Search-based Software Engineering: 
SB-SE applies metaheuristic search techniques such as genetic algorithms, simulated annealing and tabu search to software engineering problems. Many activities in software engineering can be stated as optimization problems.

###Notes-  

####iii1. Checklists: 
The domain and characteristics of a software project needed to be considered for effective and high quality duplicate defect detection. In view of this, the authors needed a feedback system to assess the search quality and tune parameters for each software product. For this purpose, they developed the Duplicate Defect Detection (DDD) framework. DDD is composed of a customized search-engine and a feedback loop for evaluating and tuning the search quality for each project and its user requirements.

####iii2. Statistical tests: 
As a proof of concept and to study the performance of the authors approach within the BlackBerry domain, they performed an experimental study on one of the main and highly active defect repositories at BlackBerry. Additionally, a study on the defect repository of the Mozilla project was also performed in order to validate the reusability of their approach, which can also give an insight on the performance of their approach on a long-lived open-source project. The main focus this experimental study was designated to present the performance of the developed framework and to highlight the impact of parameter tuning on the system’s performance. Since the cost of missing duplicate defects in the search results is significantly higher than cost of false positives at BlackBerry, they use recall rate to evaluate the performance and select and tune a subset of possible parameters to maximize recall rate. 

####iii3. Baseline results: 
The experimental studies allows the authors to analyze the impact of each tuning parameter in duplicate-defect detection performance for the selected datasets. In this study, they identified a set of parameters that were usually left out in search-based software engineering approaches, while their default values were not necessarily optimal for the input dataset. They also showed that some parameters can greatly impact the search quality, but their optimal value may not be the same for all datasets and their impact is not constant. For example, among all tuning parameters, a particularly notable parameter was the Maximum Document Frequency. It’s optimal value for BlackBerry dataset is 5% while for Mozilla Firefox is 20%.


####iii4. Future work: 
The proposed approach in the paper is generic and incorporates a feedback loop for parameter tuning and customizing the search engine for individual datasets. As assessing all the possible combinations of tuning parameters can be exhaustive, the authors optimized the recall with the help of heuristics (i.e., line search algorithm). For their data set, they found a set of parameter values and algorithms that improve the results, while their values need to be tuned for each project. Their experimental results highlight the high impact of parameter tuning on the system’s performance. However, the employed one-dimensional optimization technique for finding optimal parameter values can be extended to more advanced heuristics (e.g., Genetic Algorithms) that can explore the search space more efficiently, and suggest pareto optimal values when optimizing for conflicting objectives.


###Improvements-
iv1. The parameter tuning optimization technique used in the paper is one-dimensional for finding optimal values. More advanced heuristics such as Genetic Algorithms can be employed to explore the search space more efficiently.

iv2. Fine tuning of the cutoff value was employed to obtain the most favorable number of the defects to be reported as duplicates . In this work, F-measure analysis was measured to find optimal cutoff points based on the average recall and precision for all input defects. However, this can be improved by tuning the cutoff threshold for each individual defect and its result set.

iv3. For the performance evaluation, the authors mainly calculated the trend of recall for a range of returned results and reported the average over all defects. However, in their studies they did not consider the order in which the returned defects were presented. Having the ground truth, evaluation could be improved by applying other measures that regard position in the ranked sequence of documents such as Mean reciprocal rank (MRR), Mean Average Precision (MAP), and Discounted Cumulative Gain (DCG).

iv4. Tuning DDD for various types of projects and their defect repositories can help gain more of an insight on how the project and defect characteristics impact tuning parameters. Predictive modeling techniques could be used to elicit this knowledge and help to refine it in a form of patterns.


