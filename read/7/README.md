Paper Title-
Auto-completing Bug Reports for Android Applications

Keywords-
Bug reports:A bug report is something that stores all information needed to document, report and fix problems occurred in a software or on a website.
android:Android is a mobile operating system developed by Google, based on the Linux kernel
reproduction steps: steps to produce its kind
auto-completion: Autocomplete, or auto completion, is a feature in which an application predicts the rest of the work the user is doing. eg:typing words.

Note:
motivational statements:The modern software development landscape has seen a shift
in focus toward mobile applications as tablets and smartphones
near ubiquitous adoption. Due to this trend, the
complexity of these \apps" has been increasing, making development
and maintenance challenging. Additionally, current
bug tracking systems are not able to eectively support
construction of reports with actionable information that directly
lead to a bug's resolution. To address the need for an
improved reporting system, we introduce a novel solution,
called FUSION, that helps users auto-complete reproduction
steps in bug reports for mobile apps.

Related Work:A past survey of open source developers conducted by
Koru et al. has shown that only about 50% of developers believe
bug reports are always complete [47]. Previous studies have
also shown that the information most useful to developers
is often the most diffcult for reporters to provide and that
the lack of this information is a major reason behind nonreproducible
bug reports [35, 21]. Diffculty providing such
information, especially reproduction steps, is compounded
in the context of mobile applications due to their complex
event-driven and GUI-based nature.

Conclusion: Prior research highlights an inherent lexical gap that exists
between reporters of bugs and developers. To help overcome
this, we introduced FUSION, a novel bug reporting
approach, that takes advantage of program analysis techniques
and the event-driven nature of Android applications,
in order to help auto-complete the reproduction steps for
bugs. Results from our comprehensive evaluation show FUSION
is able to produce more reproducible bug reports than
traditional issue tracking systems.
Future Work:In order to promote transparency for this work and facilitate
researchers working on similar projects, we provide the
full dataset collected during the empirical studies conducted
to evaluate FUSION. This dataset contains all of the time,
reproduction, user experience, and user preference results
from our study. For convenience, we offer the results in either
.xlsx or .csv format. The excel workbook is broken
into sheets each with different results outlined on each sheet,
and the .csv representation is broken into separate files each
containing different results.
In future work, we aim to improve
our DFS engine through supporting more gestures, to
explore adding more specic program information in reports
for quicker/automatic fault localization, and to use FUSION
as a tool for reporting feature requests.
