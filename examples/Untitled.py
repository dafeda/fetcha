#!/usr/bin/env python
# coding: utf-8

# In[57]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('load_ext', 'blackcellmagic')


# In[58]:


get_ipython().run_line_magic('autoreload', '2')
import fetcha as fetcha


# ## Norwegian API

# In[59]:


ssb_10945 = fetcha.SSB("10945")


# In[60]:


# Get all available periods
periods = ssb_10945.periods()


# In[78]:


# Total number of rows that can be fetched
ssb_10945.nrows_tot()


# In[79]:


# Number of rows in one period
ssb_10945.nrows_period()


# In[61]:


# Returns SSB-object containing data for latest period by default.
ssb_10945.fetch()


# In[62]:


# Look at the data
ssb_10945.fetch().df


# In[63]:


# Fetch list of periods
ssb_10945.fetch(["2019M12", "2020M01", "2020M02"]).df


# In[64]:


# Fetch whole year of data
ssb_10945.fetch("2020").df


# In[65]:


# Fetch multiple years
ssb_10945.fetch(["2019", "2020"]).df


# In[66]:


# Fetch and pivot
ssb_10945.fetch("2020").pivot()


# In[67]:


# Fetch and join
ssb_10948 = fetcha.SSB("10948")
ssb_10948.fetch("2020").pivot().join(ssb_10945.fetch("2020").pivot())


# In[89]:


# Fetch and add id-columns.
# You might want to pivot on id instead.
ssb_10948.fetch("2020M01", id_cols=True).pivot("statistikkvariabel_id")


# ## English API

# In[68]:


ssben_10945 = fetcha.SSB("10945", language="en")


# In[69]:


# Get all available periods
periods = ssben_10945.periods()


# In[70]:


# Returns SSB-object containing data for latest period by default.
ssben_10945.fetch()


# In[71]:


# Look at the data
ssben_10945.fetch().df


# In[72]:


# Fetch list of periods
ssben_10945.fetch(["2019M12", "2020M01", "2020M02"]).df


# In[73]:


# Fetch whole year of data
ssben_10945.fetch("2020").df


# In[74]:


# Fetch multiple years
ssben_10945.fetch(["2019", "2020"]).df


# In[75]:


# Fetch and pivot
ssben_10945.fetch("2020").pivot()


# In[76]:


# Fetch and join
ssben_10948 = fetcha.SSB("10948", language="en")
ssben_10948.fetch("2020").pivot().join(ssben_10945.fetch("2020").pivot())


# In[ ]:




