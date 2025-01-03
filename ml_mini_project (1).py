# -*- coding: utf-8 -*-
"""ML_MINI_PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M3ztSBh_yzIlnqhX5zSb0jT-Yr4xDnSO
"""

#import necessary libraries
import seaborn as sns
import pandas as pd #for python data analysis
import matplotlib.pyplot as plt#for visualization
from sklearn.model_selection import train_test_split #for dividing test data and train data
from sklearn.preprocessing import StandardScaler #for standardization
from sklearn.preprocessing import LabelEncoder #for label encoding
from sklearn.datasets import load_breast_cancer
#IMPORTING DIFFERENT ML ALGORITHMS
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

"""**Loading dataset**"""

BC_data = load_breast_cancer()
#returns a Bunch object, which is similar to a dictionary,
#values to be accessed by key, bunch["value_key"], or by an attribute, bunch.value_key.

print("Keys of the dataset:", BC_data .keys())

print("\nFeature Names:", BC_data .feature_names)# Display the feature names

print("\nTarget Names:", BC_data.target_names)# Display the target names (classes)

print("\nShape of data (features):", BC_data.data.shape)

print("\nShape of target (labels):",BC_data.target.shape)

data_df = pd.DataFrame(data = BC_data.data,columns = BC_data.feature_names)
data_df

"""**PREPROCESSING STEPS**
1. **Handling missing values:**
Missing values can affect the accuracy of machine learning models. Handling missing values helps to ensure that the models are trained on complete data
  can be handled using folllwing methods **isnull(),dropna(inplace=True),fillna()**


"""

# Check for missing values
#print(data_df.isnull().sum())  # Sum of missing values per column
if data_df.isnull().sum().sum() == 0:     #total sum of missing values
    print("No missing values detected.")

# Display basic statistics to understand feature distribution
print(data_df.describe())

data_df = pd.DataFrame(BC_data.data, columns=BC_data.feature_names)  #Converts the BC_data.data array into a Pandas DataFrame for easier manipulation.
data_df['target'] = BC_data.target                                   #Adds the target column (data.target) to the DataFrame as a new column called 'target'
x=data_df.drop('target', axis=1)                                     # x->features
y=data_df['target']                                                  #y = pd.Series(data.target)   y->target

"""
3. **Data split:**

 Splitting the dataset into training and testing sets helps to evaluate the performance of the machine learning models. This ensures that the models are generalizing well to unseen data.

        X_train, X_test, y_train, y_test = train_test_split(df.drop('target', axis=1), df['target'], test_size=0.2, random_state=42)

"""

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42) #splitting data for training and testing
# Print the shapes of the resulting datasets
print("Training Features Shape:", x_train.shape)
print("Testing Features Shape:", x_test.shape)
print("Training Target Shape:", y_train.shape)
print("Testing Target Shape:", y_test.shape)

"""2.**Data scaling: **

Scaling the features helps to prevent features with large ranges from dominating the model. This ensures that all features are treated equally by the model.

    sc = StandardScaler()
    df[['column_name']] = scaler.fit_transform(df[['column_name']])


"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)  # Fit and transform on training set
X_test_scaled = scaler.transform(x_test)       # Transform only on test set (using training scaler)

# Output shapes for verification
print("Training set shape:", X_train_scaled.shape)
print("Testing set shape:", X_test_scaled.shape)

"""4. **Data transformation**:

 Transforming categorical variables into numerical variables helps to ensure that the machine learning models can handle them correctly.
 One-hot encoding:
       Use the get_dummies function
        or
       Label encoding: Use the LabelEncoder from scikit-learn
"""

y
# Target Variable: No processing is required as it is already in numeric binary form (0 and 1). no categorical value
#le = LabelEncoder()
#data_df['target'] = le.fit_transform(data_df['target'])
#data_df['target']

"""** Machine Learning Algorithms to Implement**:

**1.Logistic Regression**

Logistic Regression is a suitable algorithm for this dataset because it's a binary classification problem, and Logistic Regression is a popular choice for binary classification tasks.

"""

# Implement Logistic Regression
lr = LogisticRegression()# Initialization
lr.fit(X_train_scaled, y_train)
y_pred_LR = lr.predict(X_test_scaled)

y_pred_LR

"""**2.Decision Tree Classifier**

Captures non-linear relationships, interpretable via tree visualization.
Decision Tree Classifier is a suitable algorithm for this dataset because it can handle high-dimensional data and is robust to outliers.
"""

# Implement Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_scaled, y_train)
y_pred_DT = dt.predict(X_test_scaled)

y_pred_DT

"""**3.Random Forest Classifier**

An ensemble of decision trees, handles overfitting better than single trees.
Random Forest Classifier is a suitable algorithm for this dataset because it can handle high-dimensional data, is robust to outliers, and can reduce overfitting.
"""

# Implement Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_scaled, y_train)
y_pred_RF = rf.predict(X_test_scaled)

y_pred_RF

"""**4.Support Vector Machine (SVM)**

Effective for high-dimensional spaces, works well with clear margins of separation.
SVM is a suitable algorithm for this dataset because it can handle high-dimensional data and is robust to outliers.
"""

# Implement Support Vector Machine (SVM)
svm = SVC(kernel='linear', probability=True)
svm.fit(X_train_scaled, y_train)
y_pred_SVM = svm.predict(X_test_scaled)

y_pred_SVM

"""** 5.k-Nearest Neighbors (k-NN)**

A non-parametric approach, works well when the decision boundary is irregular
k-NN is a suitable algorithm for this dataset because it's a simple and intuitive algorithm that can handle high-dimensional data.
"""

# Implement k-Nearest Neighbors (k-NN)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_KNN = knn.predict(X_test_scaled)

y_pred_KNN

"""**Model Comparison**"""

# Compare the performance of the five classification algorithms
print("\n\n************************************************************************\n")
print("\tLogistic Regression:\n")
print("Accuracy:", accuracy_score(y_test, y_pred_LR))
print("Classification Report:")
print(classification_report(y_test, y_pred_LR))
print("\n************************************************************************\n")
print("\tDecision Tree Classifier:")
print("Accuracy:", accuracy_score(y_test, y_pred_DT))
print("Classification Report:")
print(classification_report(y_test, y_pred_DT))
print("\n************************************************************************\n")
print("\tRandom Forest Classifier:\n")
print("Accuracy:", accuracy_score(y_test, y_pred_RF))
print("Classification Report:")
print(classification_report(y_test, y_pred_RF))
print("\n************************************************************************\n")
print("\tSupport Vector Machine (SVM):\n")
print("Accuracy:", accuracy_score(y_test, y_pred_SVM))
print("Classification Report:")
print(classification_report(y_test, y_pred_SVM))
print("\n************************************************************************\n")
print("\tnk-Nearest Neighbors (k-NN):\n")
print("Accuracy:", accuracy_score(y_test, y_pred_KNN))
print("Classification Report:")
print(classification_report(y_test, y_pred_KNN))

# Define the accuracy scores
accuracy_scores = {
    'Logistic Regression': accuracy_score(y_test, y_pred_LR),
    'Decision Tree Classifier': accuracy_score(y_test, y_pred_DT),
    'Random Forest Classifier': accuracy_score(y_test, y_pred_RF),
    'Support Vector Machine (SVM)': accuracy_score(y_test, y_pred_SVM),
    'k-Nearest Neighbors (k-NN)': accuracy_score(y_test, y_pred_KNN)
}
sorted_accuracy_scores = dict(sorted(accuracy_scores.items(), key=lambda item: item[1]) )# key=lambda item: item[1] sorting is based on the values rather than the keys
# Create a bar chart
sns.barplot(x=sorted_accuracy_scores.keys(),y=sorted_accuracy_scores.values(),data=sorted_accuracy_scores,hue=accuracy_scores.keys(),palette="plasma")
plt.xlabel('Classification Algorithm')
plt.ylabel('Accuracy')
plt.title('Accuracy of Classification Algorithms')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1)) #legend loc outside top right corner

plt.xticks(rotation=90)  # Rotate the x-axis labels for better readability
plt.show()

plt.pie(x=accuracy_scores.values(),labels=accuracy_scores.keys(),colors=["yellow", "pink", "green", "orange","red"], autopct="%1.1f%%")
plt.title("Supervised Classification Algorithms")
plt.show()

"""Summary of Model Performance

**Ranking by Accuracy:**

1.**Logistic Regression: 97.37% (Best)**

2.Random Forest Classifier: 96.49%

3.Support Vector Machine (SVM): 95.61%

4.Decision Tree Classifier: 94.74%

5.**k-Nearest Neighbors (k-NN): 94.74% (Worst)**

**Best Model:**


Logistic Regression achieved the highest accuracy (97.37%) with well-balanced precision, recall, and F1-score.

**Worst Models:**

Decision Tree Classifier and k-NN had the lowest accuracy (94.74%), possibly due to overfitting (Decision Tree) and sensitivity to scaling and parameter selection (k-NN).

Comparison of Performance Metrics

| Algorithm | Accuracy | Precision | Recall | F1-score |
| --- | --- | --- | --- | --- |
| Logistic Regression | 0.9737 | 0.98 | 0.95 | 0.97 |
| Random Forest Classifier | 0.9649 | 0.98 | 0.93 | 0.96 |
| Support Vector Machine (SVM) | 0.9561 | 0.97 | 0.96 | 0.96 |
| Decision Tree Classifier | 0.9474 | 0.96 | 0.93 | 0.94 |
| k-Nearest Neighbors (k-NN) | 0.9474 | 0.96 | 0.93 | 0.94 |

Conclusion

Logistic Regression performed the best among the five algorithms, with an accuracy score of 0.9737. k-Nearest Neighbors (k-NN) and Decision Tree Classifier performed the worst, with accuracy scores of 0.9474. Random Forest Classifier and Support Vector Machine (SVM) had accuracy scores in between.

"""

