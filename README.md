# pands-project
The Iris dataset was introduced by the British statistician and biologist Ronald Fishers.  He wrote about it in his 1936 paper and it is now widely used ever since.
The data records consists of 3 different types of species of Iris they are Setosa, Versicolour, and Virginica.  The iris plant is a flowering plant, researchers measured the characteristics of the iris plant .  The sample size is 150 split evenly between the species.  The data encompasses five columns which are Petal Length, Petal Width, Sepal Length, Sepal Width, and Species Type . 
The dataset was downloaded from https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
This script will read in Iris dataset which describes the characteristics of the Iris flowers, calculate the total, median, mean , standard deviation, max, min , Quartile 1 , Quartile 3 an Inter quartile range.  
The script presents the data through histograms, scatter plots, box plots , line plots, violin plots and pair plot.
What was found with histograms :
•	The highest frequency of the sepal length is between 30 and 35 which is between 5.5 and 6
•	The highest frequency of the sepal Width is around 70 which is between 3.0 and 3.5
•	The highest frequency of the petal length is around 50 which is between 1 and 2
•	The highest frequency of the petal width is between 40 and 50 which is between 0.0 and 0.5
•	The sepal lengths of both Iris Virginica and Iris versicolor are slightly left skewed
•	In the case of Sepal Length, there is a huge amount of overlapping.
•	In the case of Sepal Width also, there is a huge amount of overlapping.
•	In the case of Petal Length, there is a very little amount of overlapping.
•	In the case of Petal Width also, there is a very little amount of overlapping.

Scatterplot is used when the visualization data contains only one-dimensional data points, they are suitable to find the relationship between two variables such as sepal length vs sepal width and petal length vs petal width .  
•	Petal Length for Setosa is fully separated from the other two classes but Versicolor and Virginica are not fully separated they have some overlap of some data points
•	Species Setosa has smaller sepal lengths but larger sepal widths.
•	Versicolor Species lies in the middle of the other two species in terms of sepal length and width
•	Species Virginica has larger sepal lengths but smaller sepal widths.
•	Species Setosa has smaller petal lengths and widths.
•	Versicolor Species lies in the middle of the other two species in terms of petal length and width
•	Species Virginica has the largest of petal lengths and widths.
 Boxplot display the summary of the set of data values.  It shows minimum, first quartile, median, third quartile and maximum 
•	Species Setosa has the smallest features and less distributed with some outliers.
•	Species Versicolor has the average features.
•	Species Virginica has the highest features

The violin plot shows density of the length and width in the species.

 Pairs plot is a matrix of scatterplots that lets you understand the pairwise relationship between different variables in a dataset.
•	Species Setosa has the smallest of petals widths and lengths. It also has the smallest sepal length but larger sepal widths
•	Versicolor sepal length is slightly larger than verginica but smaller than Setosa
•	Versicolor and verginica sepal width are similar sizing 
•	 Verginica has the largest petal length and width 


References

https://stackoverflow.com/questions/67946868/how-do-i-install-pandas-into-visual-studios-code
https://stackoverflow.com/questions/54129321/installed-pandas-but-still-cant-import-it
https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
https://www.javatpoint.com/pandas-sum#:~:text=sum()%20function%20is%20used,the%20values%20in%20each%20column.4
https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82
https://www.ritchieng.com/machine-learning-iris-dataset/
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
https://thispointer.com/pandas-get-sum-of-column-values-in-a-dataframe/
https://www.geeksforgeeks.org/python-pandas-dataframe-std/?ref=lbp
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html
https://erikrood.com/Python_References/pandas_column_average_median_final.html
https://ozzmaker.com/add-colour-to-text-in-python/#:~:text=To%20make%20some%20of%20your%20text%20more%20readable%2C,statement.%201%20print%20%28%22033%20%5B1%3B32%3B40m%20Bright%20Green%20n%22%29
https://salmaneunus27.github.io/Engineer/2021/03/09/blog-1/
https://www.c-sharpcorner.com/article/a-first-machine-learning-project-in-python-with-iris-dataset/
https://www.educba.com/data-manipulation-with-python/
https://www.codecademy.com/learn/learn-statistics-with-python/modules/quartiles-quantiles-and-interquartile-range/cheatsheet
https://www.calculatorsoup.com/calculators/statistics/quartile-calculator.php
https://www.blog.pythonlibrary.org/2021/09/07/matplotlib-an-intro-to-creating-graphs-with-python/
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
https://datahub.io/machine-learning/iris#data
https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html
https://www.programiz.com/python-programming/writing-csv-files
https://stackoverflow.com/questions/41910583/errno-13-permission-denied-python
https://stackoverflow.com/questions/39282516/python-list-to-csv-throws-error-iterable-expected-not-numpy-int64
https://www.adamsmith.haus/python/answers/how-to-add-a-column-to-a-csv-file-in-python
https://docs.python.org/3/library/csv.html
https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
https://akshay-a.medium.com/descriptive-statistics-with-pandas-on-iris-data-beginner-bbc4422597ea
https://mode.com/example-gallery/python_histogram/#:~:text=To%20create%20a%20histogram%2C%20we%20will%20use%20pandas,visualizing%20data%2C%20you%20want%20to%20highlight%20specific%20variables.
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
https://medium.com/analytics-vidhya/first-step-to-statistics-with-iris-data-3d29c0820c5d
https://notepub.io/notes/programming-languages/python-for-data-science/python-for-data-science-exploratory-data-analysis-iris-dataset/
https://datacrayon.com/posts/machine-learning/ml-with-kaggle/machine-learning-with-kaggle-kernels-part-1/#:~:text=One%20way%20to%20get%20this%20information%20is%20to,Counting%20the%20number%20of%20samples%20for%20each%20classification.
https://www.statology.org/seaborn-title/
https://www.marsja.se/how-to-change-size-of-seaborn-plot/
https://stackabuse.com/matplotlib-change-scatter-plot-marker-size/
https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python#:~:text=Set%20the%20figure%20size%20and%20adjust%20the%20padding,method.%20To%20save%20the%20histogram%2C%20use%20plt.savefig%20%28%27image_name%27%29.
https://www.statology.org/matplotlib-show-grid/#:~:text=To%20add%20gridlines%20to%20the%20plot%2C%20we%20can,plt.grid%28True%29%20plt.show%28%29%20Add%20Gridlines%20to%20Only%20One%20Axis
https://medium.com/eda-iris-dataset/exploratory-data-analysis-eda-on-iris-data-set-by-python-fbaae921654a
https://towardsdatascience.com/violin-plots-explained-fb1d115e023d
https://seaborn.pydata.org/generated/seaborn.violinplot.html
https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
https://machinelearningknowledge.ai/seaborn-pairplot-tutorial-for-beginners/#:~:text=The%20hue%20parameter%20helps%20us%20to%20categorize%20data,the%20pairplot%20%28%29%20function.%20In%20%3A%20sns.pairplot%28penguins%2C%20hue%3D%22specie
https://datascienceplus.com/box-plots-identify-outliers/#:~:text=Let%20build%20the%20following%20boxplot%20with%20iris%20dataset,median%2C%20upper%20quartile%20and%20maximum%20value%20of%20Sepal.Length.
https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/
https://stackoverflow.com/questions/58350212/matplotlib-hist-smoothing-the-line-between-points-with-step-histogram
https://github.com/NM20XX/First-step-to-Statistics-with-Iris-data-/blob/master/stacked_histogram.py
