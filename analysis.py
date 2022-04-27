from tkinter import N, W
from turtle import title  # Import libraries used later to open iris dataset file
import pandas as pd #Import library to allow read in data and manipulation of data
import seaborn as sns  #Used for analysis of data and graphical representations
import matplotlib.pyplot as plt #Used for graphs
import numpy as np #Used for calculations of data
import csv #file type

dataRead = pd.read_csv(r"C:\Users/Catriona Murray/Documents/pands-project/iris_dataset.csv") # Read in csv file using pandas library functions
f = open(r"C:\Users\Catriona Murray\Documents\pands-project\iris_summary.csv",W , newline='') #open the file so we can write to the file
writer = csv.writer(f) # function write to the file that is opened iris_summary.csv
df = pd.DataFrame(dataRead) # Read in all data to variable df
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'Species' ] # Label the coloumns of the csv read in so we can run calculations on data using pandas library
totalSepL=df['sepal_length'].sum() # calculate and store the sum of sepal length using pandas library functions
medianSepL=df['sepal_length'].median() #calculate and store the median of sepal length using pandas library functions
meanSepL=round(df['sepal_length'].mean(),2) #calculate and store the mean of sepal length round to two decimal places using pandas library functions
stdSepL=round(df['sepal_length'].std(),2) #calculate and store the standard deviation of sepal length round to two decimal places using pandas library functions
maxSepL=df['sepal_length'].max() #calculate and store the Max sepal length round to two decimal places using pandas library functions
minSepL=df['sepal_length'].min() # calculate and store the Min sepal length round to two decimal places using pandas library functions
totalSepW=df['sepal_width'].sum() # calculate and store the sum of sepal width using pandas library functions
medianSepW=df['sepal_width'].median() #calculate and store the median of sepal width using pandas library functions
meanSepW=round(df['sepal_width'].mean(),2) #calculate and store the mean of sepal width round to two decimal places using pandas library functions
stdSepW=round(df['sepal_width'].std(),2) #calculate and store the standard deviation of sepal width round to two decimal places using pandas library function
maxSepW=df['sepal_width'].max() #calculate and store the Max sepal width round to two decimal places using pandas library functions
minSepW=df['sepal_width'].min() #calculate and store the Min sepal width round to two decimal places using pandas library functions
totalPetL=df['petal_length'].sum() # calculate and store the sum of petal length using pandas library functions
medianPetL=df['petal_length'].median() #calculate and store the median of petal length using pandas library functions
meanPetL=round(df['petal_length'].mean(),2) #calculate and store the mean of petal length round to two decimal places using pandas library functions
stdPetL=round(df['petal_length'].std(),2)#calculate and store the standard deviation of petal length round to two decimal places using pandas library functions
maxPetL=df['petal_length'].max() #calculate and store the Max petal length round to two decimal places using pandas library functions
minPetL=df['petal_length'].min() # calculate and store the min petal length round to two decimal places using pandas library functions
totalPetW=df['petal_width'].sum() # calculate and store the sum of petal width using pandas library functions
medianPetW=df['petal_width'].median()  #calculate and store the median of petal width using pandas library functions
meanPetW=round(df['petal_width'].mean(),2) #calculate and store the mean of petal width round to two decimal places using pandas library functions
stdPetW=round(df['petal_width'].std(),2) #calculate and store the standard deviation of petal width round to two decimal places using pandas library functions
maxPetW=df['petal_width'].max() #calculate and store the Max petal width round to two decimal places using pandas library functions
minPetW=df['petal_width'].min() #calculate and store the Min Petal width round to two decimal places using pandas library functions
#des=df.describe()
q1SepalLgth = np.quantile(df.sepal_length,0.25) # Using numpy library functions to calculate the 1st quartile which is 1/4 or 25% of the range of values of Sepal Length
q3SepalLgth = np.quantile(df.sepal_length,0.75)  # Using numpy library functions to calculate the 1st quartile which is 3/4 or 75% of the range of values of Sepal Length
iqrSepalLgth = round((q3SepalLgth - q1SepalLgth),2) # 50% of sample range for sepal length- 75 -25%% = 50% 
q1SepalWdth = np.quantile(df.sepal_width,0.25)# Using numpy library functions to calculate the 1st quartile which is 1/4 or 25% of the range of values of Sepal width
q3SepalWdth = np.quantile(df.sepal_width,0.75) # Using numpy library functions to calculate the 1st quartile which is 3/4 or 75% of the range of values of Sepal Width
iqrSepalWdth = round((q3SepalWdth - q1SepalWdth),2)  # 50% of sample range  for sepal width- 75 -25%% = 50%
q1PetalLgth = np.quantile(df.petal_length,0.25)  # Using numpy library functions to calculate the 1st quartile which is 1/4 or 25% of the range of values of Petal Length
q3PetalLgth = np.quantile(df.petal_length,0.75) # Using numpy library functions to calculate the 1st quartile which is 3/4 or 75% of the range of values of Petal Length
iqrPetalLgth = round((q3PetalLgth - q1PetalLgth),2) # 50% of sample range  for petal length- 75 -25%% = 50%
q1PetalWdth = np.quantile(df.petal_width,0.25) # Using numpy library functions to calculate the 1st quartile which is 1/4 or 25% of the range of values of Petal width
q3PetalWdth = np.quantile(df.petal_width,0.75) # Using numpy library functions to calculate the 1st quartile which is 3/4 or 75% of the range of values of Petal width
iqrPetalWdth = round((q3PetalWdth - q1PetalWdth),2) # 50% of sample range  for Petal width- 75 -25%% = 50%
#writer.writerow(["Sepal Length"])
writer.writerow(["","Total","Mean","Standard Deviation","Max","Min","First Quartile","Median","Third Quartile","IQR"]) #Write headings on the first row with 10 columns andthe 1st column is empty
writer.writerow(["Sepal Length",totalSepL,meanSepL,stdSepL,maxSepL,minSepL,q1SepalLgth,medianSepL,q3SepalLgth,iqrSepalLgth]) # write to iris_summary.csv with calculations of sepal Length
writer.writerow(["Sepal Width",totalSepW,meanSepW,stdSepW,maxSepW,minSepW,q1SepalWdth,medianSepW,q3SepalWdth,iqrSepalWdth]) # write to iris_summary.csv with calculations of sepal width
writer.writerow(["Petal Length",totalPetL,meanPetL,stdPetL,maxPetL,minPetL,q1PetalLgth,medianPetL,q3PetalLgth,iqrPetalLgth])# write to iris_summary.csv with calculations of petal length
writer.writerow(["Petal Width",totalPetW,meanPetW,stdPetW,maxPetW,minPetW,q1PetalWdth,medianPetW ,q3PetalWdth,iqrPetalWdth]) # write to iris_summary.csv with calculations of petal width
# File that is beint written to iris_summary.csv must not be open at the same time as running the script as it will fail with permission errors


print ("\033[2;37;40m Sepal Length: \033[0;37;40m") # Output heading so that its underlined
print ("Sepal Length Standard Deviation: "+str(stdSepL)) # Print out Standard Deviation and all other calculations for each characteristics
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

plt.figure(figsize = (10, 7)) # Using mathplot lib library functions setting the size of figure  
x = df["sepal_length"] # Setting the x axis to the sepal length read in from data sets and using the columns that were labelled previously which are used to extract that specific variable data
plt.hist(x, bins = 20, color = "green") # setting the figure to be a histogram which is based on the x varialble , bins is particular histogran type with intervals, Color assigns the color for that histogram
plt.title("Sepal Length in cm")  # set the title of the graph
plt.xlabel("Sepal_Length_cm") # set the x axis label
plt.ylabel("Count") # set the axis label
plt.savefig('histSepalLength.png') # Save the graph generated as a png file  in current directory
plt.grid(True) # put in grid
plt.show() # Output the graphs to the screen

plt.figure(figsize = (10, 7))
x = df["sepal_width"]
plt.hist(x, bins = 20, color = "red")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.savefig('histSepalWidth.png')
plt.grid(True)
plt.show()


plt.figure(figsize = (10, 7))
x = df["petal_length"]
plt.hist(x, bins = 20, color = "blue")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.grid(True)
plt.savefig('histPetalLength.png')
plt.show()

plt.figure(figsize = (10, 7))
x = df["petal_width"]
plt.hist(x, bins = 20, color = "orange")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
plt.grid(True)
plt.savefig('histPetalWidth.png')
plt.show()

sns.countplot(x='Species', data=df,).set(title='Species Count') # Creates a histogram that shows the number of flowers per species 
plt.show() #Show the chart

#scatterplots   

sns.scatterplot(x='sepal_length', y='sepal_width',
                hue='Species', data=df,).set(title='Sepal Length vs Sepal Width') # Create a scatter plot showing distribution of speal length and width of each species
#Set the tile of the graph to  Sepal Length vs Sepal Width, color is set based on the species
# Placing Legend outside the Figure 
plt.legend(bbox_to_anchor=(1, 1), loc=4) # Place legend on the graph, setting where the location is
fig = plt.gcf() # get the current figure
fig.set_size_inches(10, 8) # set the size of the current figure
plt.grid(True) # add drid to the graph
plt.savefig('scatSepal.png') #save graph as Png
plt.show() # output graph on screen

sns.scatterplot(x='petal_length', y='petal_width', hue='Species', data=df,).set(title='Petal Length vs Petal Width')
# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=4)
fig = plt.gcf()
fig.set_size_inches(10, 8)
plt.grid(True)
plt.savefig('scatPetal.png') #save graph as Png
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(16,9)) #Box plots shows distribution of Petal width,length and Sepal width and length of each Iris species
#above sets size of graph and the parameters of where it is located onscreen wgich is either 0 or 1
sns.boxplot( y="petal_width", x= "Species", data=dataRead, orient='v' , ax=axes[0, 0]) # Uses seaborn library orient = Vertical ax is location of each graph on screen
sns.boxplot( y="petal_length", x= "Species", data=dataRead, orient='v' , ax=axes[0, 1])
sns.boxplot( y="sepal_length", x= "Species", data=dataRead, orient='v' , ax=axes[1, 0])
sns.boxplot( y="sepal_width", x= "Species", data=dataRead, orient='v' , ax=axes[1, 1])
plt.savefig('boxPlot.png') 
plt.show()


sns.lineplot(data=df, x='petal_length', y='petal_width', hue='Species', dashes=False, marker='o').set(title ="Petal Length vs Petal Width");
plt.show()
sns.lineplot(data=df, x='sepal_length', y='sepal_width', hue='Species', dashes=False, marker='o').set(title ="Sepal Length vs Sepal Width");
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(16,10)) #tViolin Plot shows the density of the length and width of petal and sepal in each species
sns.violinplot( y="petal_width", x= "Species", data=dataRead, orient='v' , ax=axes[0, 0],inner='quartile')
sns.violinplot( y="petal_length", x= "Species", data=dataRead, orient='v' , ax=axes[0, 1],inner='quartile')
sns.violinplot( y="sepal_length", x= "Species", data=dataRead, orient='v' , ax=axes[1, 0],inner='quartile')
sns.violinplot( y="sepal_width", x= "Species", data=dataRead, orient='v' , ax=axes[1, 1],inner='quartile')
plt.savefig('violinPlot.png') 
plt.show()


plt.figure(figsize=(8,10)) # shows the corelation of Petal Width, Petal Length, Sepal Width and sepal length
sns.heatmap(dataRead.corr(),annot=True)
plt.plot()
plt.show()

sns.pairplot(dataRead, hue="Species", palette="husl",height =2, markers=["o", "s", "D"])
plt.show()
f.close()



