# -*- coding: utf-8 -*-
"""Exploratory Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tqzmrEu8xirpkXdf7Vj3M1YIrllZBcbL
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# %matplotlib inline
# %config InlineBackend.figure_format='retina'

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/gdrive/MyDrive/NUS_GAIP_GRP9/HPE Project/Datasets/Merged_food.csv')
df = data

df.head()

df.shape

sns.lineplot(x=df.week, y="num_orders", data=df);

df['month']=((df['week']-1)/4).astype('int64')
df['month'] = df['month'].map({0:'Jan',1:'Feb',2:'Mar',3:'Apr',4:'May',5:'June',6:'July',7:'Aug',8:'Sep',9:'Oct',
                            10:'Nov',11:'Dec',12:'Jan',13:'Feb',14:'Mar',15:'Apr',16:'May',17:'June',18:'July',
                            19:'Aug',20:'Sep',21:'Oct',22:'Nov',23:'Dec',24:'Jan',25:'Feb',26:'Mar',27:'Apr',28:'May',
                            29:'June',30:'July',31:'Aug',32:'Sep',33:'Oct',34:'Nov',35:'Dec',36:'Jan'})

plt.figure(figsize=(8,5))
sns.lineplot(x=df.month, y="num_orders", data=df);

df['quarter']=(df['week']/13).astype('int64')
df['quarter'] = df['quarter'].map({0:'Q1', 1:'Q2', 2:'Q3', 3:'Q4', 4:'Q1', 5:'Q2', 6:'Q3', 7:'Q4', 8:'Q1', 9:'Q2', 10:'Q3',11:'Q4'})

sns.lineplot(x=df.quarter, y="num_orders", data=df);

fig,(ax1, ax2, ax3)= plt.subplots(nrows=3)
fig.set_size_inches(18, 28)

sns.pointplot(data=df, x='month', y='num_orders', ax=ax1)
sns.pointplot(data=df, x='month', y='num_orders', hue='emailer_for_promotion', ax=ax2)
sns.pointplot(data=df, x='month', y='num_orders', hue='homepage_featured', ax=ax3)

#Determining the category most preferred by the customers
fig=plt.figure(figsize=(11,6))
sns.set_style("white")

plt.xticks(rotation=90,fontsize=12)
plt.title('Number of Orders per Category',fontdict={'fontsize':14})
sns.barplot(y='num_orders', x='category', data=df.groupby('category').num_orders.sum().sort_values(ascending=False).reset_index(),palette='viridis');
plt.ylabel('No. of Orders',fontdict={'fontsize':12})
plt.xlabel('Category',fontdict={'fontsize':12})

#Determining the category per cuisine most preferred by customers
fig=plt.figure(figsize=(15,6))
sns.set_style("white")
plt.xticks(rotation=90,fontsize=12)
plt.title('Total Number of Orders for Each Cuisine-Category',fontdict={'fontsize':14})

sns.barplot(x='category',y='num_orders',data=df.groupby(['cuisine','category']).sum().sort_values(by='num_orders', ascending=False).reset_index(),hue='cuisine',palette='cubehelix')

plt.ylabel('No. of Orders',fontdict={'fontsize':12})
plt.xlabel('Cuisine-Category',fontdict={'fontsize':12})
sns.despine(bottom = False, left = False);

#Plotting the total nmber of orders received by each center type across all regions
fig=plt.figure(figsize=(4,7))
plt.title('Total No. of Orders for Each Center type',fontdict={'fontsize':13})
sns.barplot(y='num_orders', x='center_type', data=df.groupby('center_type').sum()['num_orders'].reset_index(),palette='autumn');
plt.ylabel('No. of Orders',fontdict={'fontsize':12})
plt.xlabel('Center Type',fontdict={'fontsize':12})
sns.despine(bottom = True, left = True);

ax = sns.heatmap(train.corr(), annot=True)

def outliers(col):
    q3=round(df[col].quantile(0.75),6)
    q1=round(df[col].quantile(0.25),6)
    iqr=q3-q1
    lw = q1 - (3*iqr)
    hw = q3 + (3*iqr)  
    uo=df[df[col]>hw].shape[0]
    lo=df[df[col]<lw].shape[0]
    print('Number of Upper Outliers :',uo)
    print('Number of Lower Outliers :',lo)
    print('Percentage of Outliers :',((uo+lo)/df.shape[0])*100)
    return hw
    
hw = outliers('num_orders')

train.describe()

#checking skewness of checkout price column in the train set
plt.figure(figsize=(10,5))
sns.distplot(train['checkout_price'])
plt.show()

#checking skewness of checkout price column in the train set
plt.figure(figsize=(10,5))
sns.distplot(train['base_price'])
plt.show()

#https://towardsdatascience.com/demand-prediction-with-lstms-using-tensorflow-2-and-keras-in-python-1d1076fc89a0
#https://towardsdatascience.com/time-series-forecasting-with-lstms-using-tensorflow-2-and-keras-in-python-6ceee9c6c651
#https://colab.research.google.com/drive/1k3PLdczAJOIrIprfhjZ-IRXzNhFJ_OTN#scrollTo=FLGKCn9h_Fzg