import pandas as pd # conda install seaborn, matplotlib, scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns


file_url = 'http://media.githubusercontent.com/media/musthave-ML10/data_source/main/insurance.csv'
data = pd.read_csv(file_url)

# print(data)
# print(data.info()) # information of columns
# print(data.describe()) # information of statistics
# print(round(data.describe(), 2))


# [Data preprocessing]
X = data[['age', 'sex', 'bmi', 'children', 'smoker']] # independent variables
y = data['charges'] # dependent variables

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
# The random state hyperparameter is used to control any such randomness
# involved in machine learning models to get consistent results. 

model = LinearRegression()
model.fit(X_train, y_train) # model.fit(independent variables, dependent variables)
pred = model.predict(X_test)


# [Evaluating with a graph]
comparison = pd.DataFrame({'actual' : y_test, 'pred' : pred})
plt.figure(figsize=(10, 10))
sns.scatterplot(x='actual', y='pred', data=comparison)
# plt.show()


# [Evaluating in a statistical way]
mse = mean_squared_error(y_test, pred) ** 0.5
rmse = mean_squared_error(y_test, pred, squared=False)
# print(rmse)
r2 = model.score(X_train, y_train)
# print(r2)


# [Understanding of Linear Regression]
coef = model.coef_
# print(coef)
pd_coef = pd.Series(model.coef_, index = X.columns)
# print(pd_coef)
intercept = model.intercept_
print(intercept)