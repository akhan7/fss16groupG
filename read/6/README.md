New Features for Duplicate Bug Detection

Nathan Klein, Department of Computer Science, Oberlin College, Oberlin, Ohio, USA, nklein@oberlin.edu

Christopher S. Corley, Nicholas A. Kraft, Department of Computer Science, The University of Alabama, Tuscaloosa, Alabama, USA, cscorley@ua.edu, nkraft@cs.ua.edu

Keywords: 
ii1. Duplicate bug reports: When many developers/testers file a bug report having same technical problems but they use different terminology or styles and write about different phenomenon to write about the same issue(s) that is classified as a duplicate bug report.
ii2. Topic model: In machine learning and natural language processing, a topic model is a type of statistical model for discovering the abstract "topics" that occur in a collection of documents.
ii3. Machine learning: Machine learning is a subfield of computer science that is closely related to (and often overlaps   with) computational statistics; a discipline which also focuses in prediction-making through the use of computers.
ii4. Deduplication: In computing deduplication is a specialized compression technique for eliminating duplicate copies of repeating data

Notes:
iii1. Data set: The writers have used the data collected by – ‘A. Alipour, A. Hindle, and E. Stroulia. A contextual approach towards more accurate duplicate bug report detection. In Proc. 10th Working Conf. on Mining Software Repositories, pages 183–192, 2013.’. It consists of reports pulled from the android database between November 2007 and September 2012

iii2. Related Work: The work related to the authors work is by C. Sun, D. Lo, S.-C. Khoo, and J. Jiang who formulated the duplicate bug detection problem as given a bug report, return a list of the top-k most similar bug reports. Also one of the other related works is by Alipour who formulated the problem as given two bug reports, predict whether they are duplicates. The authors have mentioned that their approach is similar to the latter approach.

iii3. Results : The outcome of the authors’ study is
1.	The descriptive power of the suite of attributes show that they provide an increase in accuracy, AUC, and Kappa statistics over other related works when applied to the Android repository. 
2.	The effectiveness and simplicity of the metrics proposed in this study make them good candidates for futures studies on duplicate bug reports. 
3.	The use of Bagging to aid in classification provided a small increase in accuracy.

iii4. Future work: The authors have suggested that a future study which utilizes their metrics in order to find duplicates of incoming bugs, using a top-k approach in which a fixed number of possible duplicate reports are presented for each incoming report, would further test their effectiveness.

Improvements:

iv1. The author could maintain a separate section for related work. This could ensure that the readers will get proper idea of what related work is already done in the beginning itself. So that they could relate it further in the paper wherever required.

iv2. The author could add a separate section for future work. The author has added future work in the conclusion section. This makes it confusing to understand at times. 

iv3. When the author mentions that their study performs better in terms of some parameters, they could add a few pictorial representation of few of them for better understanding of the reader. 

