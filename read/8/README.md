Paper Title:
Automatically Learning Semantic Features for Defect Prediction

Keywords:
defect: A kind of imperfection
DBN:In machine learning, a deep belief network (DBN) is a generative graphical model, or alternatively a type of deep neural network, composed of multiple layers of latent variables ("hidden units"), with connections between the layers but not between units within each layer
AST:In computer science, an abstract syntax tree (AST), is a tree representation of the abstract syntactic structure of source code written in a programming language.
WPDP: A defect prediction process which is conducted within the  single  software  project,  is  called  within-project  defect
prediction (WPDP).

Notes:
Related Work: Work related to the authors' work has been described as-  Software Defect Prediction based on WPDP and CDPD wherein for existing approaches to defect prediction are based on manually encoded traditional features which are not sensitive to programs' semantic
information, while authors approach automatically learns semantic features using DBN and uses these features to perform defect prediction tasks. Also the approach followed by the author requires only the source code of the training and test projects, it is suitable for both within-project defect prediction and cross-project defect prediction. The other related work is-Deep Learning and Semantic Feature Generation in Software Engineering wherein they used DBN to generate features from 14 traditional change level features,ie features generated from their approach are relations among existing features, whereas the authors have used DBN to learn semantic features directly from source code.

Dataset: To facilitate the replication and verification of their experiments, the authors have used PROMISE dataset which is publicly available. They have selected all Java open source projects from PROMISE whose version numbers are provided.

Result : The evaluation of the authors' work on ten open source projects shows that the automatically learned semantic features could significantly improve both within-project and cross-project defect prediction compared to traditional features. Their semantic
features improve the within-project defect prediction on average by 14.7% in precision, 11.5% in recall, and 14.2% in F1 comparing with traditional features. 

Future Work: The authors would like to extend their automatically semantic feature generation approach to C/C++ projects for defect prediction. Also they intend to extend their approach to automatically generate features for predicting defects at other levels, such as change level, module level, and package level.

Improvement:
The authors should have mentioned related work in the beginning of the paper. This would have made it easier to follow their approach.
The authors have added future work with the conclusion. Making it a different section would have been simpler for the reader to understand

