
# coding: utf-8

# In[2]:


import pandas as pd
import sys

# In[1]:
fname = sys.argv[1]




# In[20]:


df = pd.read_csv(fname,header = None)
print df.groupby(0).count().min().iloc[0]
# print df.groupby(0).count()


# In[ ]:




