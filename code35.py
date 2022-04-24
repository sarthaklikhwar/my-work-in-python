# Train a logistic regression classifier to predict whether a flower is iris virginica or not

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()

print(list(iris.keys()))   #prints the content of datasets
print(iris['data'].shape)  #prints number of rows and columns
print(iris['target'])      #prints the dataset values (labels)
print(iris['DESCR'])       #gives descrption about datasets

X = iris.data[:,np.newaxis,2]
y = (iris["target"] == 2).astype(np.int)
print(X,y)

# Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X,y)    #traning of model
example = clf.predict(([[2.6]]))    #testing of model
print(example)     #it either gives 0 or 1 that is it displays the probablity of iris.

# Using matplotlib to plot the visualization
X_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(X_new)
print(y_prob)
plt.plot(X_new, y_prob[:,1], "g-", label="virginica")
plt.show()






