#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
fi = pd.read_csv(r'C:/Users/Prateek/Desktop/New folder (2)/archive (1)/data.csv')
fi


# In[14]:


fi.head(10)


# In[15]:


fi.tail(5)


# In[16]:


fi.info()


# In[17]:


fi.describe()


# In[21]:


fi.info()


# In[22]:


fi['Age'].mean()


# In[24]:



fi['Jersey Number'].mean()


# In[25]:


#All Rows and Coloum Mean
fi.mean()


# In[31]:


#Trimmed_Mean
from scipy.stats import trim_mean
trim_mean(fi['Age'],0.1)


# In[34]:


#Weighted Mean 
import numpy as np
np.average(fi['Age'], weights = fi['Jersey Number'])


# In[35]:


#Median
fi['Age'].median()


# In[36]:


fi.median()


# In[4]:


import numpy as np
Q1=np.percentile(fi['Age'],25)
Q1


# In[6]:


import numpy as np
Q2=np.percentile(fi['Age'],75)
Q2


# In[1]:


import matplotlib.pyplot as plt
8


# In[ ]:




