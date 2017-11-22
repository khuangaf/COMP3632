
# coding: utf-8

# In[2]:


import pandas as pd
import sys

# In[1]:
fname = sys.argv[1]


file= open(fname,'rb')


# In[20]:


df = pd.read_csv('datafile3_out.txt',header = None)
print df.groupby(0).count().min().iloc[0]


# In[ ]:




