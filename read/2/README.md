# Paper Title:
*A Discriminative Model Approach for Accurate Duplicate Bug Report Retrieval* 
(ICSE '10 Proceedings of the 32nd ACM/IEEE International Conference on Software Engineering - Volume 1)


# Keywords:
* **ii1. Tokenization**: Tokenization is the process of parsing a character stream into a sequence of word tokens by splitting the stream by the de-limiters. Tokenization is one of the important pre processing tasks in Information retrieval process.

* **ii2. Support Vector Machine (SVM)**: It is an approach to build-ing a discriminative model or classifier based on a set of labeled vectors. Given a set of vectors, some belonging to a positive class and others belonging to a negative class, SVM tries to build a hyperplane that separates vectors belonging to the positive class from those of the negative class with the largest margin.

* **ii3. Recall rate**: Recall rate is defined as the ratio of number of duplicate reports whose masters are successfully detected to the total number of duplicate reports for testing the retrieval process. In other words it gives the percentage of duplicates whose masters are successfully retreived in the list.

* **ii4. Feature Engineering**: Feature engineering is a process of using domain knowledge of the data to create, extract features that makes machine learning algorithm work.

# Notes:
* **iii1. Motivational Statements**:
Previous approaches that are used to find duplicate bugs were based on similarity score of vector space representation.
There is still much room for improvement in terms of accuracy of duplicate detection process. In this paper discriminative models for information retrieval are built to detect duplicate bug reports more accurately which the authors claim would improve duplicate bug detection accuracy by 43%

* **iii2. Data**:
Data (bug reports) have been taken from three popular open source projects - Eclipse (IDE), Firefox (Web browser) and OpenOffice (Office Suite). These sources were chosen because they were large software projects with big bug repositories and they were all written in different languages so that a generalised result can be found.


  | Dataset | Time Frame | Training Reports (Duplicate/All) | sting Reports(Duplicate/All)| 
  ----------|------------|----------------------------------|-----------------------------|
  |OpenOffice |Jan/02/2008–Dec/30/2008|100/3160|529/9572 |
  |Firefox|Apr/04/2002–Jul/07/2007|100/962|3207/46359 |
  |Eclipse |Jan/02/2008–Dec/30/2008|100/4265|1913/40387 |

* **iii3. Related Work**:
  1. One of the pioneer studies on duplicate bug report detec-tion is by Runeson et al. Their approach first cleaned the textual bug reports via natural language processing tech-niques – tokenization, stemming and stop word removal. 
    *P. Runeson, M. Alexandersson, and O. Nyholm. Detection of Duplicate Defect Reports Using Natural Language Processing. Inproceedings of the International Conference on Software Engineering, 2007.*
    
  2. Wang et al. extended the work by Runeson et al. in two dimensions.
    *X. Wang, L. Zhang, T. Xie, J. Anvik, and J. Sun. An Approach to Detecting Duplicate Bug Reports using Natural Language and Execution Information. In proceedings of the International Conference on Software Engineering, 2008.*

  3. Besides the effort on duplicate bug report detection, there has also been effort on bug report mining. Anvik et al and Cubranic and Murphy and Lucca all proposed semi-automatic techniques to categorize bug reports.

* **iii4. Baseline results**: The following figure shows the results of this discriminative model based approach on the three datasets over seven runs compared to earlier methods.

![Open office](pics/openoffice.png) ![Firefox](pics/firefox.png) ![Eclipse](pics/eclipse.png)|

# Improvements:
* **iv1.** 
* **iv2.**  

* **iv3.** 

* **iv4.** The author could have added a section of future work so that further work based on their work could be figured out.
