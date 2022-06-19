#!/usr/bin/env python
# coding: utf-8

# ### Sara Magdy Mohamed

# ### Task # 3: Exploratory Data Analysis

# In[60]:


import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[61]:


superstore_df= pd.read_csv("SampleSuperstore.csv")
superstore_df.head()


# ### Data Exploration

# In[62]:


superstore_df.shape


# In[63]:


superstore_df.info()


# In[64]:


superstore_df.describe()


# In[65]:


superstore_df.isnull().sum()


# In[66]:


superstore_df.nunique()


# In[67]:


superstore_df.count()


# ### Data Preprocessing

# In[68]:


superstore_df.duplicated().sum()


# In[69]:


superstore_df.drop_duplicates(inplace=True)


# In[70]:


superstore_df.shape


# In[71]:


# relation between each pair in dataset
sns.pairplot(superstore_df)


# In[72]:


corr= superstore_df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr,annot=True)


# ### Ship Mode

# In[73]:


superstore_df['Ship Mode'].value_counts().plot(kind ='bar', figsize=(5,5))


# In[74]:


superstore_df.groupby('Ship Mode')[['Sales','Profit']].sum().round(2).plot(kind='bar',figsize=(5,5)) 
plt.title('profit & sales vs ship mode')
plt.ylabel('profit & sales')
plt.xlabel ('ship mode')
plt.show()


# ### Segment

# In[75]:


superstore_df['Segment'].value_counts().plot(kind ='bar', figsize=(5,5))


# In[76]:


superstore_df.groupby('Segment')[['Sales','Profit']].sum().round(2).plot(kind='bar',figsize=(5,5)) 
plt.title('profit & sales vs Segment')
plt.ylabel('profit & sales')
plt.xlabel ('Segment')
plt.show()


# ### State

# In[77]:


superstore_df['State'].value_counts().plot(kind ='bar', figsize=(12,10))


# In[78]:


superstore_df.groupby('State')[['Sales','Profit']].sum().round(2).plot(kind='bar',figsize=(12,10)) 
plt.title('profit & sales vs State')
plt.ylabel('profit & sales')
plt.xlabel ('State')
plt.show()


# ### Region

# In[79]:


superstore_df['Region'].value_counts().plot(kind ='bar', figsize=(10,8))


# In[80]:


superstore_df.groupby('Region')[['Sales','Profit']].sum().round(2).plot(kind='bar',figsize=(10,8)) 
plt.title('profit & sales vs Region')
plt.ylabel('profit & sales')
plt.xlabel ('Region')
plt.show()


# ### Category

# In[81]:


superstore_df['Category'].value_counts().plot(kind ='bar', figsize=(10,8))


# In[82]:


superstore_df.groupby('Category')[['Sales','Profit']].sum().round(2).plot(kind='bar',figsize=(10,8)) 
plt.title('profit & sales vs Category')
plt.ylabel('profit & sales')
plt.xlabel ('Category')
plt.show()


# ### Sub-Category

# In[83]:


superstore_df['Sub-Category'].value_counts().plot(kind ='bar', figsize=(10,8))


# In[84]:


superstore_df.groupby('Sub-Category')[['Sales','Profit']].sum().round(2).plot(kind='bar',figsize=(10,8)) 
plt.title('profit & sales vs  Sub-Category')
plt.ylabel('profit & sales')
plt.xlabel ('Sub-Category')
plt.show()


# ### The relation between Discount & Profit 

# In[85]:


superstore_df.groupby('Discount')[['Sales','Profit']].sum().plot(kind='bar',figsize=(10,8)) 
plt.title('profit & sales vs Discount')
plt.ylabel('profit & sales')
plt.xlabel ('Discount')
plt.show()


# In[86]:


sns.lineplot(superstore_df["Discount"],superstore_df["Profit"])

