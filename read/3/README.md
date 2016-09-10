# Paper Title:
*A Topic-based Approach for Narrowing the Search Space of Buggy Files from a Bug Report* 
(Anh Tuan Nguyen, Tung Thanh Nguyen, Jafar Al-Kofahi, Hung Viet Nguyen, Tien N. Nguyen, )


# Keywords:
* **ii1. Defect Localization :** Suppose a bug does slip through somehow and it shows up in the Integration Build. If we have made our unit tests fairly small by testing only a single behavior in each, we should be able to pinpoint the bug pretty quickly based on which test is failing. This is one of the big advantages of unit tests over customer tests. The customer tests will tell us that some behavior expected by the customer isn't working. The unit test will tell us why. This phenomena is called as Defect Localization.

* **ii2. Topic Modelling :**  a topic model is a type of statistical model for discovering the abstract "topics" that occur in a collection of documents.

* **Ii3. LDA :** Latent Dirichlet Allocation (LDA)  is a generative, machine learning model, used to model the topics in a collection of textual documents.

* 

# Notes:
* **iii1. Motivational Statements:** 
| Bug Report #50900 |
|-------------------|
| Summary: Error saving state returned from update of external object; incoming sync will not be triggered. |
| Description: This showed up in the server log. It’s not clear which interop component this belongs to so I just picked one of them. Seems like the code run in this scheduled task should be able to properly handle a stale data by refetching/retrying. |
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

Figures 1 and 2 display bug report #50900 and the corresponding fixed/buggy file InteropService.java (for brevity, only comments are shown in Figure 2). The report is about a software defect in which incoming synchronization tasks were not triggered properly in a server. We found that the developers fixed the bug at a single file InteropService.java by adding code into two methods processIncoming and processIncomingOneState to handle a stale data by refetching. As shown, both bug report #50900 and the buggy file InteropService.java describe the same problematic functionality of the system: the “synchronization” of “incoming data” in the interop service. This faulty techni- cal aspect (was described and) could be recognized via the relevant terms, such as sync, synchronization, incoming, interop, state, schedule, etc. Considering the bug report and the source file as textual documents, we could consider this technical aspect as one of their topics. This example suggests that the bug report and the corresponding buggy source files share the common buggy technical topic(s). Thus, detecting the common technical topic(s) between a bug report and a source file could help in bug file localization.

* **iii1.  Related Work: In related work to BugScout they directly applied LDA analysis on bug reports and files to localize the buggy files.

* **iii2. Data sets : Data sets from different software projects including Jazz (a development framework from IBM), Eclipse (an integrated development environment), AspectJ, and ArgoUML, have been included.

* 

# Improvements:
* **iv1.** The authors have always used individual words for computing similarity scores. They could have gone a step further and used bigrams and technical phrases for analysis.
* **iv2.** The authors argue that since the average frequency of new report arrival is around 1 - 1.5 per hour, their system has enough time to retrain and refresh the model. But this might not always be the case especially during the time of new software release where there might be huge influx of bug reports. They could have discussed the criteria they would to update the model in such a case.  

* **iv3.** Since the model evolves continously with new incoming reports, the time for evolving the model also increases. The authors have mentioned this overhead but could have explained to optimize this case.