
# coding: utf-8

# In[52]:


from mondrian import mondrian
import sys, copy, random, pdb
import pandas as pd
import numpy as np
RELAX = False 
data = list(np.array(pd.read_csv(sys.argv[1],header = None)))
data = [ list(d) for d in data]
data_back = copy.deepcopy(data)

result, eval_result = mondrian(data, 4, RELAX)



# In[53]:


def sumRow(row):
    output = ''
    for i in range(len(row)):
        output+= row[i]
    return output


# In[54]:


df = pd.DataFrame(np.array(data)[:,:-1])
aggDf = pd.DataFrame(np.array(data_back)[:,:-1])
outputDf = aggDf
aggDf['steeveissmart'] = pd.DataFrame(np.array(data)[:,:-1]).apply(sumRow, axis=1)


# In[55]:


aggGroupDf = aggDf.groupby('steeveissmart').agg(np.median).applymap(lambda x: int(round(x)))


# In[56]:


outputList = [ aggGroupDf.loc[steeve] for steeve in outputDf['steeveissmart']]


# In[57]:


pd.DataFrame(np.concatenate([np.array(outputList),(np.array(data_back)[:,-1][:, None])],axis=1)).to_csv(sys.argv[1],header=None, index=None)







