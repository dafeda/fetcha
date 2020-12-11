#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')


# In[2]:


get_ipython().run_line_magic('autoreload', '2')
import pandas as pd
import fetcha as fetcha


# In[3]:


# https://www.ssb.no/en/statbank/list/pasient


# In[4]:


ssb = fetcha.SSB("10261")


# In[6]:


fltr = [{"code": "Region", "values": ["0"]}]


# In[10]:


df = ssb.fetch(fltr=fltr)


# In[12]:


ssb.pivot(df)


# In[ ]:




