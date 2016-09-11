# Paper Title:
*A Topic-based Approach for Narrowing the Search Space of Buggy Files from a Bug Report* 
(Anh Tuan Nguyen, Tung Thanh Nguyen, Jafar Al-Kofahi, Hung Viet Nguyen, Tien N. Nguyen, )


# Keywords:
* **ii1. Defect Localization :** Suppose a bug does slip through somehow and it shows up in the Integration Build. If we have made our unit tests fairly small by testing only a single behavior in each, we should be able to pinpoint the bug pretty quickly based on which test is failing. This is one of the big advantages of unit tests over customer tests. The customer tests will tell us that some behavior expected by the customer isn't working. The unit test will tell us why. This phenomena is called as Defect Localization.

* **ii2. Topic Modelling :**  a topic model is a type of statistical model for discovering the abstract "topics" that occur in a collection of documents.

* **ii3. LDA :** Latent Dirichlet Allocation (LDA)  is a generative, machine learning model, used to model the topics in a collection of textual documents.

* **ii4. Automated Bug Tracking Tool:** Automated bug tracking tools allow for an easier to use bug tracking tool. Automation helps to make the tool easier to learn to use, easier to operate and easier to teach others to use. 

# Notes:
* **iii1. Motivational Statements:**  Figures 1 and 2 display bug report #50900 and the corresponding fixed/buggy file InteropService.java (for brevity, only comments are shown in Figure 2). The report is about a software defect in which incoming synchronization tasks were not triggered properly in a server. We found that the developers fixed the bug at a single file InteropService.java by adding code into two methods processIncoming and processIncomingOneState to handle a stale data by refetching. As shown, both bug report #50900 and the buggy file InteropService.java describe the same problematic functionality of the system: the “synchronization” of “incoming data” in the interop service. This faulty techni- cal aspect (was described and) could be recognized via the relevant terms, such as sync, synchronization, incoming, interop, state, schedule, etc. Considering the bug report and the source file as textual documents, we could consider this technical aspect as one of their topics. This example suggests that the bug report and the corresponding buggy source files share the common buggy technical topic(s). Thus, detecting the common technical topic(s) between a bug report and a source file could help in bug file localization.

| Bug Report #50900 |
|-------------------|
| Summary: Error saving state returned from update of external object; incoming sync will not be triggered.
  Description: This showed up in the server log. It’s not clear which interop component this belongs to so I just picked one of them. Seems like the code run in this scheduled task should be able to properly handle a stale data by refetching/retrying. |
**Fig 1:** Bug report #50900


| InteropService.java |
|---------------------|
|// Implementation of the Interop service interface. // Fetch the latest state of the proxy |
|// Fetch the latest state of the sync rule |
|// Only return data from last synchronized state|
|// If there is a project area associated with the sync rule,|
|// Get an advisable operation for the incoming sync|
|// Schedule sync of an item with the state of an external object|
|// The result of incoming synchronization (of one item state).|
|// Use sync rule to convert an item state to new external state.|
|// Get any process area associated with a linked target item....|
|// For permissions checking, get any process area associated with the target item. If none, get the process area of the sync rule.|
|// return an instance of the process server service...|
|// Do incoming synchronization of one state of an item.|
|public IExternalProxy processIncoming (IExternalProxyHandle ...) {.......} |
**Fig 2:** Source file InteropService.java

* **iii2.  Related Work:** A related work to BugScout is from Lukins et al. They directly applied LDA analysis on bug reports and files to localize the buggy files. They perform indexing on all source files with the detected topics from LDA. Then, for a new bug report, a textual query is formed from its description and a search via Vector Space Model (VSM) is performed among such indexed source files. In contrast, BugScout correlates the topics in both source files and bug reports, and uses topics as a random variable in our model. Moreover, their approach does not work well if the code contains few common terms with a new bug report. 

* **iii3. Data sets:** Data sets from different software projects including Jazz (a development framework from IBM), Eclipse (an integrated development environment), AspectJ, and ArgoUML, have been included.

* **iii4. Baseline results:** BugScout was created which is an automated approach to localize the buggy files given a bug report. It assumes that the textual contents of a bug report and those of its corresponding source code share some technical aspects of the system. S specialized topic model was developed, that represents the technical aspects in the textual contents of bug reports and source files as topics, and correlates bug reports and buggy files via the shared topics. Empirical results showed that BugScout is accurate in localizing buggy files and outperforms existing approaches.

# Improvements:
* **iv1.** The authors have always used individual words for computing similarity scores. They could have gone a step further and used bigrams and technical phrases for analysis.

* **iv2.** The ranking system of the bug reports is derived from viewing historical data (which source files have had more defects in the past) and shared topics with the new bug report. This system fails to accomodate bug reports pertaining to new source files which might not have been so thoroughly tested and hence might not have numerous bug reports filed but still might be a buggy source file.  

* **iv3.** The authors have not made it clear how this model can be improved or optimized. They haven't mentioned any future work which can be put in this model so that it's accuracy or speed can be further increased as compared to previous models. 
