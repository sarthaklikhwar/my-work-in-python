# linear regression model
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error


Diabetes = datasets.load_diabetes()
# to know about the dataset we are using
# print(list(Diabetes.keys()))
# print(Diabetes["DESCR"])
# print(Diabetes['target'])
# print(Diabetes['data'].shape)
# print(Diabetes['frame'])
# print(Diabetes['feature_names'])

Diabetes_X = Diabetes.data[
    :, np.newaxis, 2
]  # we are considering only that feature that is at index 2.
# print(Diabetes_X)

Diabetes_X_train = Diabetes_X  # feature used for traning data
Diabetes_X_test = Diabetes_X  # feature used for testing data
# print(Diabetes_X_train,'\n',Diabetes_X_test)

Diabetes_y_train = Diabetes.target
Diabetes_y_test = Diabetes.target

# calling of linear regression
model = linear_model.LinearRegression()
model.fit(Diabetes_X_train, Diabetes_y_train)
Diabetes_y_predicted = model.predict(Diabetes_X_test)

# graph plotting(only for linear model)
plt.scatter(Diabetes_X_test, Diabetes_y_test)  # given data
plt.plot(Diabetes_X_test, Diabetes_y_predicted)  # model generated value
plt.show()

# loss compute
print(
    "mean squared error is", mean_squared_error(Diabetes_y_test, Diabetes_y_predicted)
)
print("weights", model.coef_)
print("intercept", model.intercept_)
