import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


file_url = 'http://media.githubusercontent.com/media/musthave-ML10/data_source/main/titanic.csv'
data = pd.read_csv(file_url)


# [Making a heatmap with correlations]
sns.heatmap(data.corr(), cmap='coolwarm', vmin=-1, vmax=1, annot=True)
# plt.show()


# [Data preprocessing]
data = data.drop(['Name', 'Ticket'], axis=1) # Because Name and Ticket are not important
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True) # Feature Enginerring


# [Modeling and Estimation]
X = data.drop('Survived', axis=1) # X has only dependent variables
y = data['Survived'] # y has only independents variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

model = LogisticRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
# print(accuracy_score(y_test, pred))
coef = model.coef_ # double list..
# print(pd.Series(model.coef_[0], index=X.columns))


# [Multicolinearity]
data['family'] = data['SibSp'] + data['Parch']
data.drop(['SibSp', 'Parch'], axis=1, inplace=True)

X = data.drop('Survived', axis=1) # X has only dependent variables
y = data['Survived'] # y has only independents variables
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

model = LogisticRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(accuracy_score(y_test, pred))