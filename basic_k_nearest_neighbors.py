import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


file_url = 'http://media.githubusercontent.com/media/musthave-ML10/data_source/main/wine.csv'
data = pd.read_csv(file_url)

# print(data['class'].unique(), data['class'].nunique())
# print(data['class'].value_counts())

sns.barplot(x=data['class'].value_counts().index, y=data['class'].value_counts())
plt.show()