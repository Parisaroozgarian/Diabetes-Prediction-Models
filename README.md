# DiabetesDataset-SVM-KNN-LogisticRegres-Decisiontreeclassifiersion
The dataset used is, the dataset of information related to diabetic patients of a hospital. label is this data,
Outcome, which takes two values of 0 and 1, and indicates whether or not the patient has the disease.
It is diabetes. We divide this dataset into two parts, Train and Test.Using 4 methods, we design models based on dataset data :
- SVM
- KNN
- Logistic Regression 
- Decision Tree


To predict whether or not a patient will have diabetes with 4 methods. Then using evaluation methods module (f1_score, Precision, Recall, Accuracy) We evaluated each one and try to get the best possible result by changing the parameters 
Features of this dataset :
1. Pregnancies
2. Glucose 
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI 
7. Diabetes Pedigree Function 
8. Age

# SVM
Explanation of the SVM model:
SVM, or support vector machine, is a classifier or boundary that determines the best classification and separation between data by the criterion of placing support vectors.

Its purpose is to find the best border among the data in such a way that it has the greatest possible distance from all categories.
To use SVM in Python, we use the Python machine learning library named scikit-learn .

All kernels and mapping functions are prepared. The three functions NuSVC, LinearSVC, SVC are responsible for the main task of classification.
In the SVM code, we import the SVC class from the sklearn library and then create a new object and We store it inside the clf variable. We change the kernel parameter from its default value of 'rbf' to the value of 'linear'.Because it is more accurate. We put size_train=0.4 and size_test=0.2.

(kernel='rbf' → kernel='linear')

In this class, we help to improve the evaluation result by changing the kernel parameter

# KNN
Explanation of the KNN model:
KNN (nearest neighbor-K) is a type of machine learning algorithm
It is supervised, which is used in both classification problems and predictive regression problems.

We import the KNeighbosClassifier class from the sklearn library and then create a new object from it and store it in clf. In this class, we try to improve the data evaluation result by changing the neighbors_n parameter.We put 0.4=size_train and 0.2=size_test.

By changing the neighbors_n parameter, we get results for different values.

# LgisticRegression
Explanation of Logistic Regression model:
Logistic regression is a supervised learning classification algorithm that is used to predict the probability of a target variable.
We import the LogisticResgressionClassifier class from the sklearn library and then create a new object from it and store it in clf. We put 0.4=size_train and 0.2=size_test.
We use these numbers to be complementary.

# DecisionTree Classifier
Explanation of the DecisionTree model:
Same as SVM algorithm, the Decisiontree algorithm can handle classification, regression, and even tasks with multiple outputs. These algorithms are very powerful and can be used in complex datasets.

We import the DecisionTreeClassifier class from the sklearn library. Then we create a new object from it and store it in clf. We put 0.4 = size_train and 0.2 = size_test. We choose numbers that are complementary and use 100% of the dataset.


# Conclusion
According to the evaluation of the hobbies, it can be concluded that the SVM model has performed better than other models and has given us the best evaluation.
