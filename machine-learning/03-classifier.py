#Installing scikit-learn using Anaconda
We're going to use a Python library called scikit-learn, which includes lots of well designed tools for performing common machine learning tasks. 
We're going to install scikit-learn and its dependencies using Anaconda, which is a Python-based platform focused on data science and machine learning.
environment.yml - Download this file to install scikit-learn using Anaconda

#Loading a Dataset
from sklearn.datasets import load_iris
iris = load_iris()
print(list(iris.target_names))

#Making Predictions with a Classifier
from sklearn.datasets import load_iris
iris = load_iris()
print(list(iris.target_names))
from sklearn import tree
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(iris.data, iris.target)
print(classifier.predict([[5.1,3.5,1.4,1.5]]))


#Question
Which of the following best describes the iris dataset?
The iris flower dataset is like the "hello world" program of datasets. 
It's not meant to be used in practical applications, but it's good for testing machine learning techniques.

Which of the following code samples will create a classifier?
classifier = tree.DecisionTreeClassifier()

What's the name of the file that was used to load scikit-learn into Anaconda?
environment.yml

Why might running the same classifier twice produce a different outcome?
The decision tree classifier randomly chooses a feature that it thinks will make the best comparison which results in probabilistic behavior.

Which of the following code samples will load the iris dataset?
from sklearn.datasets import load_iris
