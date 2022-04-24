#from statistics import median
from lib2to3.pgen2.pgen import DFAState
from tkinter import N, W
from turtle import title
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
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
maxSepL=df['sepal_length'].max()
minSepL=df['sepal_length'].min()
totalSepW=df['sepal_width'].sum()
medianSepW=df['sepal_width'].median()
meanSepW=round(df['sepal_width'].mean(),2)
stdSepW=round(df['sepal_width'].std(),2)
maxSepW=df['sepal_width'].max()
minSepW=df['sepal_width'].min()
totalPetL=df['petal_length'].sum()
medianPetL=df['petal_length'].median()
meanPetL=round(df['petal_length'].mean(),2)
stdPetL=round(df['petal_length'].std(),2)
maxPetL=df['petal_length'].max()
minPetL=df['petal_length'].min()
totalPetW=df['petal_width'].sum()
medianPetW=df['petal_width'].median()
meanPetW=round(df['petal_width'].mean(),2)
stdPetW=round(df['petal_width'].std(),2)
maxPetW=df['petal_width'].max()
minPetW=df['petal_width'].min()
#des=df.describe()
q1SepalLgth = np.quantile(df.sepal_length,0.25)
q3SepalLgth = np.quantile(df.sepal_length,0.75)
iqrSepalLgth = round((q3SepalLgth - q1SepalLgth),2)
q1SepalWdth = np.quantile(df.sepal_width,0.25)
q3SepalWdth = np.quantile(df.sepal_width,0.75)
iqrSepalWdth = round((q3SepalWdth - q1SepalWdth),2)
q1PetalLgth = np.quantile(df.petal_length,0.25)
q3PetalLgth = np.quantile(df.petal_length,0.75)
iqrPetalLgth = round((q3PetalLgth - q1PetalLgth),2)
q1PetalWdth = np.quantile(df.petal_width,0.25)
q3PetalWdth = np.quantile(df.petal_width,0.75)
iqrPetalWdth = round((q3PetalWdth - q1PetalWdth),2)
#writer.writerow(["Sepal Length"])
writer.writerow(["","Total","Mean","Standard Deviation","Max","Min","First Quartile","Median","Third Quartile","IQR"])
writer.writerow(["Sepal Length",totalSepL,meanSepL,stdSepL,maxSepL,minSepL,q1SepalLgth,medianSepL,q3SepalLgth,iqrSepalLgth])
writer.writerow(["Sepal Width",totalSepW,meanSepW,stdSepW,maxSepW,minSepW,q1SepalWdth,medianSepW,q3SepalWdth,iqrSepalWdth])
writer.writerow(["Petal Length",totalPetL,meanPetL,stdPetL,maxPetL,minPetL,q1PetalLgth,medianPetL,q3PetalLgth,iqrPetalLgth])
writer.writerow(["Petal Width",totalPetW,meanPetW,stdPetW,maxPetW,minPetW,q1PetalWdth,medianPetW ,q3PetalWdth,iqrPetalWdth])


print ("\033[2;37;40m Sepal Length: \033[0;37;40m")
print ("Sepal Length Standard Deviation: "+str(stdSepL))
print ("Total Sepal Length: "+str(totalSepL))
print ("Mean Sepal Length: "+str(meanSepL))
print ("Sepal Length Standard Deviation: "+str(stdSepL))
print ("Max Sepal Length: "+str(maxSepL))
print ("Min Sepal Length: "+str(minSepL))
print ("First Quartile Sepal Length: "+str(q1SepalLgth))
print ("Median Sepal Length: "+str(medianSepL))
print ("Third Quartile Sepal Length: "+str(q3SepalLgth))
print ("IQR Sepal Length: "+str(iqrSepalLgth)+"\n")

print ("\033[2;37;40m Sepal Width:\033[0;37;40m")
print ("Sepal Width Standard Deviation: "+str(stdSepW))
print ("Total Sepal Width: "+str(totalSepW))
print ("Mean Sepal Width: "+str(meanSepW))
print ("Sepal Width Standard Deviation: "+str(stdSepW))
print ("Max Sepal Width: "+str(maxSepW))
print ("Min Sepal Length: "+str(minSepW))
print ("First Quartile Sepal Length: "+str(q1SepalWdth))
print ("Median Sepal Width: "+str(medianSepW))
print ("Third Quartile Sepal Length: "+str(q3SepalWdth))
print ("IQR Sepal Length: "+str(iqrSepalLgth)+"\n")

print ("\033[2;37;40m Petal Length: \033[0;37;40m")
print ("Petal Length Standard Deviation: "+str(stdPetL))
print ("Total Petal Length: "+str(totalPetL))
print ("Mean Petal Length: "+str(meanPetL))
print ("Petal Length Standard Deviation: "+str(stdPetL))
print ("Max Petal Length: "+str(maxPetL))
print ("Min Petal Length: "+str(minPetL))
print ("First Quartile Petal Length: "+str(q1PetalLgth))
print ("Median Petal Length: "+str(medianPetL))
print ("Third Quartile Petal Length: "+str(q3PetalLgth))
print ("IQR Petal Length: "+str(iqrPetalLgth)+"\n")

print ("\033[2;37;40m Petal Width: \033[0;37;40m")
print ("Petal Width Standard Deviation: "+str(stdPetW))
print ("Total Petal Width: "+str(totalPetW))
print ("Mean Petal Width: "+str(meanPetW))
print ("Petal Width Standard Deviation: "+str(stdPetW))
print ("Max Petal Width: "+str(maxPetW))
print ("Min Petal Width: "+str(minPetW))
print ("First Quartile Petal Width: "+str(q1PetalWdth))
print ("Median Petal Width: "+str(medianPetW))
print ("Third Quartile Petal Length: "+str(q3PetalLgth))
print ("IQR Petal Width: "+str(iqrPetalWdth)+"\n")
#shape = df.shape
#info = df.info()
#df.isnull().sum()

#data= df.drop_duplicates(subset ="Species",) 
#data

#print(data)
#print(shape)
#print(info)
#print(des)
#spec=df['Species'].nunique()
#cnt=df.count()
#specCount=df['Species'].value_counts()
#print(specCount)
#print(spec)


plt.figure(figsize = (10, 7))
x = df["sepal_length"]
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")
plt.savefig('histSepalLength.png')
plt.show()

plt.figure(figsize = (10, 7))
x = df["sepal_width"]
plt.hist(x, bins = 20, color = "red")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.savefig('histSepalWidth.png')
plt.show()


plt.figure(figsize = (10, 7))
x = df["petal_length"]
plt.hist(x, bins = 20, color = "blue")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.savefig('histPetalLength.png')
plt.show()

plt.figure(figsize = (10, 7))
x = df["petal_width"]
plt.hist(x, bins = 20, color = "orange")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
plt.savefig('histPetalWidth.png')
plt.show()

sns.countplot(x='Species', data=df,).set(title='Species')
plt.show()

#scatterplots
sns.scatterplot(x='sepal_length', y='sepal_width',
                hue='Species', data=df,).set(title='Sepal Length vs Sepal Width')
# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=4)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.grid(True)
plt.show()

sns.scatterplot(x='petal_length', y='petal_width', hue='Species', data=df, ).set(title='Petal Length vs Petal Width')
# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=4)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.grid(True)
plt.show()

new_data = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
#print(new_data.head())
plt.figure(figsize = (10, 7))
new_data.boxplot()
plt.grid(True)
plt.show()

sns.violinplot(x="Species", y="petal_length", data=df, size=8)
plt.show()
f.close()



