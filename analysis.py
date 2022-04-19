#from statistics import median
from tkinter import W
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import csv
dataRead = pd.read_csv(r"C:\Users/Catriona Murray/Documents/pands-project/iris_dataset.csv")
#print(data.head())
#print(data.sample(10))
f = open(r"C:\Users\Catriona Murray\Documents\pands-project\iris_summary.csv",W , newline='')
writer = csv.writer(f)
df = pd.DataFrame(dataRead)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Species' ]
#print(data.head())
totalSepL=df['sepal_length'].sum()
medianSepL=df['sepal_length'].median()
meanSepL=round(df['sepal_length'].mean(),2)
stdSepL=round(df['sepal_length'].std(),2)
maxSepl=df['sepal_length'].max()
minSepl=df['sepal_length'].min()
des=df.describe()
writer.writerow(["Sepal Length sum","Sepal Length Median","Sepal Length Mean","Sepal Length standard deviation","Sepal Length Max","Sepal Length Min"])
writer.writerow([totalSepL,medianSepL,meanSepL,stdSepL,maxSepl,minSepl])
plt.figure(figsize = (10, 7))
x = df["sepal_length"]
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")
plt.show()
#shape = df.shape
#info = df.info()
#df.isnull().sum()

#data= df.drop_duplicates(subset ="Species",) 
#data

#print(data)
#print(shape)
#print(info)
print(des)
spec=df['Species'].nunique()
cnt=df.count()
specCount=df['Species'].value_counts()
print(specCount)
print(spec)

f.close()


