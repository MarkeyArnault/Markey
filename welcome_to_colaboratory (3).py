# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb

#Title of Database: Wine recognition data
	Updated Sept 21, 1998 by C.Blake : Added attribute information
  
#Sources:
   (a) Forina, M. et al, PARVUS - An Extendible Package for Data
       Exploration, Classification and Correlation. Institute of Pharmaceutical
       and Food Analysis and Technologies, Via Brigata Salerno, 
       16147 Genoa, Italy.
   
   (b) Stefan Aeberhard, email: stefan@coral.cs.jcu.edu.au
   
   (c) July 1991

   
   The data was used with many others for comparing various 
   classifiers. The classes are separable, though only RDA 
   has achieved 100% correct classification.

   Relevant Information:

   -- These data are the results of a chemical analysis of
      wines grown in the same region in Italy but derived from three
      different cultivars.
      The analysis determined the quantities of 13 constituents
      found in each of the three types of wines. 

   -- I think that the initial data set had around 30 variables, but 
      for some reason I only have the 13 dimensional version. 
      I had a list of what the 30 or so variables were, but a.) 
      I lost it, and b.), I would not know which 13 variables
      are included in the set.

#Number of Instances

      	class 1 59
	class 2 71
	class 3 48

#Number of Attributes 
	
	13

#7. For Each Attribute:

	All attributes are continuous

  
  
#Let's define Data
Data is a facts and statistics collected together for reference or analysis.

#Where can we get data? 
##We can get data almost everywhere

###Some of the place you can get data from are: UCI, kaggle, amazone and so one

#Import the data

#We going to put the columns name

#Show the begining of the data
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns

column_names = [ 'Alcohol' , 'Malic acid' , 'ash' , 'Alcalinity of ash' , 'Magnesium' , 'Total phenols' , 'Flavanoids' , 'Nonflanoids phenols' , 'Proanthocyanins' , 'color intensity' , 'Hue' , 'OD280/OD315 of diluted wines' , 'Proline' ]
 	       	      
df = pd.read_csv ("https://raw.githubusercontent.com/MarkeyArnault/Markey/main/wine.data", header=None, names = column_names)

print('The dimensions of the data are: ')

df.head()

"""#We are going to check if we have any empty data
#How Do I know if a data empty?
#You can use the attribute df. empty to check whether it's empty or not: if df. empty: print('DataFrame is empty!
"""

df.isna().sum()

"""#We are going to check how many unique values we have in each column right now"""

df.nunique()

"""#Reason Alcohol is 126 for unique value is because not everybody drunk alcohol and also it depends on how often someone drink alcohol.

#Reason why Malic acid is higher is because everyday we eat things that have malic acid without knowing.

#As it right now, everything looks clean I decided not to delete some data on the list

#SIKEEEEE!!!!!!

#We are going to delete some of the datas that aren't important and mention the name of the data and reset the data.
"""

df = df.drop(['Hue'],axis = 1)
df_original = df.copy()

column_names.remove('Hue')

df.info()

"""#I just noticed I can delete more than 1 data but decided to delete 1

#I delete ash.. Ash is something you can put in alcahol and no change after putting it.
"""

df = df.drop(['ash'],axis = 1)
df_original = df.copy()

column_names.remove('ash')

df.info()

"""#Change the data to numeric

#I will change it based off of those names

# 1- Alcohol 2- Malic acid	3- ash	4- Alcalinity of ash	5- Magnesium	6- Total phenols	7- Flavanoids	8- Nonflanoids 9- phenols	10- Proanthocyanins	11- color intensity	12- Hue	13- OD280/OD315 of diluted 14- wines	15- Proline

#Since it was a big data, I decided to convert everything but those ash, Magnesium, Hue, OD280/OD315 of diluted wines, Proline.
"""

column_names = [ 'Alcohol' , 'Malic acid' , 'ash' , 'Alcalinity of ash' , 'Magnesium' , 'Total phenols' , 'Flavanoids' , 'Nonflanoids phenols' , 'Proanthocyanins' , 'color intensity' , 'Hue' , 'OD280/OD315 of diluted wines' , 'Proline' ]

df[['Alcohol' , 'Malic acid' , 'Alcalinity of ash' , 'Total phenols' , 'Flavanoids' , 'Nonflanoids phenols' , 'Proanthocyanins' , 'color intensity']] = \
    df[['Alcohol' , 'Malic acid' , 'Alcalinity of ash' , 'Total phenols' , 'Flavanoids' , 'Nonflanoids phenols' , 'Proanthocyanins' , 'color intensity']].apply(pd.to_numeric)

df.head()

"""#Let's check to see what the issues are.

#test what the issue is with all those name that are took out.
"""

errors = pd.DataFrame(df[pd.to_numeric(df.Magnesium, errors='coerce').isnull()])

errors.head()

"""#For some reason it appear like that. However, every seems smooth so far. Since that, I decided not to conver it to NaNs from '?', or float64. By my research the whole data was numeric

#As I said before everything is smooth and numeric So I decided to Use the .describe method to get summary stats
"""

df.describe()

"""#NOW!!! everything is Numeric which is what I want so far

#As I right now we are going to check out the Categorical Data
"""

print(df['Magnesium'].value_counts())

"""#Right we are going to do the plot of the different alcohol"""

plt.figure(figsize=(15,8))
df['Magnesium'].value_counts().plot(kind='bar', fontsize = 15)

"""#Analyze Non-Categorical Data
Here I will create some initial charts and references for the non-categorical data.

#get the numerical data by first setting up a way to refer to the numerical column names
"""

numerical_columns = column_names.remove('Magnesium')

"""##create a dataframe for now"""

df_numerical = df.drop(['Magnesium'],axis = 1)

df_numerical.hist(bins=50, figsize=(12,8))
plt.show()

"""#Correlation Matrix
We are now going to use a correlation matrix to analyze

We use something called seaborn to do this.
"""

corrMatrix = df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corrMatrix, annot=True)
plt.show()

"""#I see that Alcohol has a lot of correlated features, so let's look at it by itself, ordered"""

corrMatrix["Alcohol"].sort_values(ascending=False)

"""We see that there are a lot of variables that have very high positive and a little few of them have negative correlation to Alcohol.

#using a scatter plot to look at individual comparisons
#s - is the circle size
#c - is the color
"""

df.plot(kind="scatter", x="weight", y="Alcohol", alpha=0.4,
    s=df["Magnesium"], label="Scatter", figsize=(10,7),
    c="Alcalinity of ash", cmap=plt.get_cmap("jet"), colorbar=True,
)
plt.legend()

"""#let's now look at a few good attributes to compare
#we want to see if we are missing anything in a non-linear relationship

"""

from pandas.plotting import scatter_matrix

attributes = ['Nonflanoids phenols' , 'Alcalinity of ash' , 'Alcohol' , 'Magnesium']
scatter_matrix(df[attributes], figsize=(12, 8))

"""#We having troubles for the curves

cases like that in alcohol. we are going to choose 3 little data that appear and analyse it.

Now look at how and where these 3 data points appear in the residuals versus fits plot.

Their fitted value is less than 13 and their deviation from the residual = 0 line shares .

As we can see there's no curves for some reason so

#Dealing with Missing Data
We have three options:

1- Get rid of the missing data (the entire row)
2- Get rid of the whole attribute
3- Set the values to zero, the mean, the median, etc.

We can use DataFrame methods dropna(), drop(), and fillna() to do this:
"""

df.dropna(subset=["Magnesium"])    # option 1
df.drop("Magnesium", axis=1)       # option 2
median = df["Magnesium"].median()  # option 3
df["Magnesium"].fillna(median, inplace=True)

"""#Check for missing data"""

df.isna().sum()