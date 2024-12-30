# MINI_PROJECT_MACHINE_LEARNING_CLASSIFIERS
Objective:
The objective of this assessment is to evaluate your understanding and ability to apply supervised learning techniques to a real-world dataset.

Dataset:
Use the breast cancer dataset available in the sklearn library.

Key components to be fulfilled:

1. Loading and Preprocessing 
Load the breast cancer dataset from sklearn.
Preprocess the data to handle any missing values and perform necessary feature scaling.
Explain the preprocessing steps you performed and justify why they are necessary for this dataset.
2. Classification Algorithm Implementation 
Implement the following five classification algorithms:
1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Support Vector Machine (SVM)
5. k-Nearest Neighbors (k-NN)
For each algorithm, provide a brief description of how it works and why it might be suitable for this dataset.
3. Model Comparison 
Compare the performance of the five classification algorithms.
Which algorithm performed the best and which one performed the worst?
***********************************************************************************************************************************


Summary of Model Performance

Ranking by Accuracy:

1.Logistic Regression: 97.37% (Best)

2.Random Forest Classifier: 96.49%

3.Support Vector Machine (SVM): 95.61%

4.Decision Tree Classifier: 94.74%

5.k-Nearest Neighbors (k-NN): 94.74% (Worst)

Best Model:

Logistic Regression achieved the highest accuracy (97.37%) with well-balanced precision, recall, and F1-score.

Worst Models:

Decision Tree Classifier and k-NN had the lowest accuracy (94.74%), possibly due to overfitting (Decision Tree) and sensitivity to scaling and parameter selection (k-NN).

Comparison of Performance Metrics

Algorithm	Accuracy	Precision	Recall	F1-score
Logistic Regression	0.9737	0.98	0.95	0.97
Random Forest Classifier	0.9649	0.98	0.93	0.96
Support Vector Machine (SVM)	0.9561	0.97	0.96	0.96
Decision Tree Classifier	0.9474	0.96	0.93	0.94
k-Nearest Neighbors (k-NN)	0.9474	0.96	0.93	0.94
Conclusion

Logistic Regression performed the best among the five algorithms, with an accuracy score of 0.9737. k-Nearest Neighbors (k-NN) and Decision Tree Classifier performed the worst, with accuracy scores of 0.9474. Random Forest Classifier and Support Vector Machine (SVM) had accuracy scores in between.

