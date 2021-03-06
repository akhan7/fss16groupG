# Paper Title:
*Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen, David Lo, Chengnian Sun. 2012. Duplicate Bug Report Detection with a Combination of Information Retrieval and Topic Modeling.* 
(Proceedings of the 27th IEEE/ACM International Conference on Automated Software Engineering)

# Keywords:
* **ii1. Duplicate bug report**: When many developers/testers file a bug report having same technical problems but they use different terminology or styles and write about different phenomenon to write about the same issue(s) that is classified as a duplicate bug report.
 
* **ii2. Information retrieval (IR)** is the activity of obtaining information resources relevant to an information need from a collection of information resources.

* **ii3. Term frequency- Inverse documents frequency (Tf-Idf)**-In information retrieval term frequency–inverse document frequency is a numerical statistic that is intended to reflect how important a word is to a document in a collection.

* **ii4. Topic Model** - In machine learning and natural language processing, a topic model is a type of statistical model for discovering the abstract topics that occur in a collection of documents. Topic modeling is a frequently used text-mining tool for discovery of hidden semantic structures in a text body.

# Notes:
* **iii1. Motivational Statements:**
Among several automated detection approaches, text-based information retrieval (IR) approaches have been shown to outperform others in term of both accuracy and time efficiency. However, those IR-based approaches do not detect well the duplicate reports on the same technical issues written in different descriptive terms.

* **iii2. Data:**
The data set has been taken from the references - *C. Sun, D. Lo, S.-C. Khoo, and J. Jiang. Towards more accurate retrieval of duplicate bug reports. In ASE’11, pages 253–262. IEEE CS, 2011.*

* **iii3. Related Work:**
Similar work has been seen in paper such as - *L. Hiew. Assisted detection of duplicate bug reports.Master’s thesis, University of British Columbia, 2006.* and *A. T. Nguyen, T. T. Nguyen, J. Al-Kofahi, H. V. Nguyen, and T. N. Nguyen. A Topic-based Approach for Narrowing the Search Space of Buggy Files from a Bug Report. In ASE’11, pp. 263-272. IEEE CS, 2011.*

* **iii4. Script:** Gibbs sampling and training algorithm, Prediction algorithm for topic model have been applied.

# Improvements:
* **iv1.** DBTM is shown to perform well with bug reports have reasonably large number of topics `(k > 60)`. Those type of bug reports are obviously more complex and hence the chances of it being detected by developers and testers is less. On the other hand, more bug reports would be submitted for the bug that is more common and less complex and hence will have lesser number of topics. The paper has not given equal importance to reports with reasonably lesser number of features (20-40).

* **iv2.**  Experiments were run on open source projects like `OpenOffice, Eclipse and Mozilla`. These projects are well maintained and used by power users and developers which might not always be the case with other software which are meant for the masses (especially those that have public beta testing programs that allow common users to send bug reposts)

* **iv3.** Many open source projects are contributed by people all around the world who might use different languages. The `effect of NLP and translation` before applying the algorithms could have been discussed a bit more. 

* **iv4.** The author could have added a section of future work so that further work based on their work could be figured out.
