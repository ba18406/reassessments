#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
tmp=pd.Series([10799032847,8376628448,10010403245,15469661105,13503105901],['2015','2016','2017','2018','2019'])
tmp.index=pd.to_datetime(tmp.index)


# In[2]:


tmp


# In[6]:


import numpy as np
slope = pd.Series(np.gradient(tmp.values), tmp.index, name='slope')


# In[7]:


tmp_ = tmp.resample('T').interpolate()

slope = pd.Series(np.gradient(tmp_.values), tmp_.index, name='slope')

df = pd.concat([tmp_.rename('values'), slope], axis=1)
df


# In[8]:


df.plot()


# In[10]:


tmp=pd.Series([13417149416,10842037697,13019826572,12811607298,11303594030],['2015','2016','2017','2018','2019'])
tmp.index=pd.to_datetime(tmp.index)
slope = pd.Series(np.gradient(tmp.values), tmp.index, name='slope')

tmp_ = tmp.resample('T').interpolate()

slope = pd.Series(np.gradient(tmp_.values), tmp_.index, name='slope')

df = pd.concat([tmp_.rename('values'), slope], axis=1)
df


# In[11]:


df.plot()


# In[12]:


tmp=pd.Series([10799032847,8376628448,10010403245,15469661105,13503105901],['2015','2016','2017','2018','2019'])
tmp.index=pd.to_datetime(tmp.index)
slope = pd.Series(np.gradient(tmp.values), tmp.index, name='slope')

tmp_ = tmp.resample('T').interpolate()

slope = pd.Series(np.gradient(tmp_.values), tmp_.index, name='slope')

df = pd.concat([tmp_.rename('values'), slope], axis=1)
df


# In[13]:


df.plot()


# In[14]:


tmp=pd.Series([26534200000,25386900000,27181000000,30522800000,30521645000],['2015','2016','2017','2018','2019'])
tmp.index=pd.to_datetime(tmp.index)
slope = pd.Series(np.gradient(tmp.values), tmp.index, name='slope')

tmp_ = tmp.resample('T').interpolate()

slope = pd.Series(np.gradient(tmp_.values), tmp_.index, name='slope')

df = pd.concat([tmp_.rename('values'), slope], axis=1)
df


# In[15]:


df.plot()


# In[ ]:




