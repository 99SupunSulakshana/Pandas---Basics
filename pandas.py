import pandas as pd

# Series - Its mean one dimension array

data = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
data

# Using Data Frames - Its mean 2d Array

data = pd.DataFrame([1,2,3,4,5])
data

# using 2d array

lst = [[1,2,3,3,4],[1,2,3,3,4]]
df = pd.DataFrame(lst)
df

# How to create data frame using dictionary

dict = {'name':['Kamal','Saman','Nimal'],'marks':[80,70,60]}
df = pd.DataFrame(dict)
df

# Using two Data Frames
dict1 = {'Kamal':[5,4,5,6],'Nimal':[4,3,4,2]}
df1 = pd.DataFrame(dict1)
dict2 = {'Kamal':[5,4,5,6],'Nimal':[4,3,4,2]}
df2 = pd.DataFrame(dict2)
df1

# How to combine this two data frames
pd.concat([df1,df2],axis=1)

# How import data set in our project
data = pd.read_csv('D:\DataSet\data.csv')
data

# How to get external location's data set
data = pd.read_csv('D:\DataSet\data.csv')
data

# How to check data and columns
data.shape

# How to remove columns in data set
data.drop(columns= ['MaxValue'])

# how to get selected columns
data = data[['Date','MaxTemp','MinTemp']]

# Count The data
data.count()

# how to view head data set
data.head(20)

# How to fill missing values
data.MaxTemp = data.MaxTemp.fillna(data.MaxTemp.mean())

# How to filter data
data['MaxTemp']>45


condition = data['MaxTemp']>45
filter = data[condition]
filter

# How to get filter data columns in selected value
condition = data['MaxTemp']>45
filter = data[condition]
filter['Date']

# How to filter multiple conditions
condition = (data['MaxTemp']>45)&(data['MinTemp']<30)
filter = data[condition]
filter['Date']

# Data set details get

data.describe()


# how to create graph using data set
import matplotlib.pyplot as plt
x = range(119040)
y1 = data['MaxTemp']
y2 = data['MinTemp']
plt.plot(x,y1)
plt.plot(x,y2)

# How to create graph with data ranges
import matplotlib.pyplot as plt
x = range(119040)
y1 = data['MaxTemp'][:20]
y2 = data['MinTemp'][:20]
plt.plot(x,y1)
plt.plot(x,y2)





