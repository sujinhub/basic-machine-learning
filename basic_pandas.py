import pandas as pd # conda install pandas


file_url = 'http://media.githubusercontent.com/media/musthave-ML10/data_source/main/iris.csv'
iris = pd.read_csv(file_url)

# print(iris.groupby('class').mean())
# print(iris['class'].unique())
# print(iris['class'].nunique())
# print(iris['class'].value_counts())