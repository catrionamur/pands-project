#from statistics import median
from tkinter import W
import pandas as pd
import csv
dataRead = pd.read_csv(r"C:\Users/Catriona Murray/Documents/pands-project/iris_dataset.csv")
#print(data.head())
#print(data.sample(10))
f = open(r"C:\Users\Catriona Murray\Documents\pands-project\iris_summary.csv",W , newline='')
writer = csv.writer(f)
df = pd.DataFrame(dataRead)
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'classification' ]
#print(data.head())
totalSepL = df['sepal_length'].sum()
medianSepL = df['sepal_length'].median()
meanSepL = df['sepal_length'].mean()
stdSepL = df['sepal_length'].std()
maxSepl = df ['sepal_length'].max()
minSepl = df ['sepal_length'].min()
writer.writerow(["Sepal Length sum",totalSepL])
writer.writerow(["Sepal Length Median",medianSepL])
print(totalSepL)
print(medianSepL)
print(meanSepL)
print(stdSepL)
print(maxSepl)
print(minSepl)
f.close()


