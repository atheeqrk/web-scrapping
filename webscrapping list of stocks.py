#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


tables = pd.read_html('https://www.etmoney.com/stocks/list-of-stocks')


# In[4]:


len(tables)


# In[5]:


tables[0]


# In[ ]:




