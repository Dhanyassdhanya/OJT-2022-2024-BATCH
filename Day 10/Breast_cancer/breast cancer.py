#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("data.csv")
df.head()


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df.select_dtypes(include='object').columns


# In[6]:


len(df.select_dtypes(include='object').columns)


# In[7]:


df.select_dtypes(include=['float64','int64']).columns


# In[8]:


df.describe()


# In[9]:


df.isnull().values.any()


# In[10]:


df.isnull().values.sum()


# In[11]:


df.columns[df.isnull().any()]


# In[12]:


len(df.columns[df.isnull().any()])


# In[14]:


df['Unnamed: 32'].count()


# In[15]:


df = df.drop(columns='Unnamed: 32')


# In[16]:


df.shape


# In[17]:


df.isnull().values.any()


# In[18]:


df.select_dtypes(include='object').columns


# In[19]:


df['diagnosis'].unique()


# In[20]:


df['diagnosis'].nunique()


# In[21]:


df=pd.get_dummies(data=df, drop_first=True)


# In[22]:


df.head()


# In[32]:


df.tail()


# In[35]:


sns.countplot(df['diagnosis_M'], label='Count')
plt.show()


# In[36]:


(df.diagnosis_M==0).sum()


# In[37]:


(df.diagnosis_M==1).sum()


# In[39]:


df2=df.drop(columns='diagnosis_M')


# In[40]:


df2.head()


# In[41]:


df2.corrwith(df['diagnosis_M']).plot.bar(figsize=(20,10),title='Correlated with diagnosis_M' , 
                                         rot=45,grid=True)


# In[42]:


corr=df.corr()
corr


# In[43]:


plt.figure(figsize=(20,10))
sns.heatmap(corr, annot=True)


# In[ ]:




