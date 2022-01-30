#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[4]:


titanic = pd.read_csv('C:/Users/Shadam Gull/Desktop/CSV data/Titanic.csv')


# In[5]:


x_ti= titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)


# In[7]:


titanic.head(10)


# In[20]:


titanic.info()


# In[9]:


titanic.describe()


# In[14]:


titanic.isnull().sum()


# In[15]:


titanic.fillna(titanic.mean(), inplace= True)


# In[16]:


titanic.head(20)


# In[17]:


titanic['Age'].mean()


# In[18]:


titanic.groupby(['Sex']).mean()


# In[21]:


sum(titanic.duplicated())


# Theree is no duplicate Value in the titanic Dataset.

# In[29]:


titanic.hist(figsize= (10,6));


# In[31]:


titanic['Age'].hist();


# In[39]:


titanic['Survived'].value_counts().plot(kind='bar');


# In[96]:


titanic['Sex'].value_counts()


# In[40]:


titanic['Sex'].value_counts().plot(kind='bar')


# In[43]:


titanic.dtypes


# In[45]:


titanic['Survived'].value_counts()


# In[47]:


titanic['Sex'].value_counts().plot(kind='pie');


# In[60]:


pd.plotting.scatter_matrix(titanic, figsize=(6,6));


# In[62]:


titanic.plot(x='Age', y= 'Survived', kind= 'bar');


# In[58]:


result = titanic.pivot_table(index='Sex', columns='PClass', aggfunc={'Survived':sum})
print(result)


# In[56]:


titanic.columns


# In[79]:


titanic_b= titanic[titanic['Survived']== 1]
(titanic_b.head())


# In[90]:


titanic_b.count()


# In[93]:


titanic_b['Sex'].value_counts().plot(kind='bar');


# Femae survival rate was much higher than males by the look of the Above graph
