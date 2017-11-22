
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys

# In[2]:


K=4
MAX_NUMBER_SET = 5


# In[3]:


def ktest(df):

    return df.groupby(0).count().min().iloc[0]


# In[25]:


def cost(df):
    medium = round(np.median(df))
    return sum(abs(df-medium))


# In[46]:


df = pd.read_csv(sys.argv[1],header=None)
if ktest(df) >= K:
    exit(0)
MAX_NUMBER_SET = len(df) / K
unsorted = df[0]
sortIndex = np.argsort(df[0])
sortedList = np.array([df[0][i] for i in np.argsort(df[0])])
costTable = np.zeros([len(df),MAX_NUMBER_SET+1 ])
splitTable= np.zeros([len(df),MAX_NUMBER_SET+1 ])
prevDict = {}
for j in range(1,MAX_NUMBER_SET,1):
    
    for i in range(K-1, len(df),1):
        if j == 1:
            costTable[i][j] = cost(sortedList[: i + 1])
            splitTable[i][j] = i
#             print costTable
            continue

#             print i
        # when new set is not added in
        minCost = costTable[i][j -1]
        splitTable[i][j] = splitTable[i][j-1]
        splitIndex = 0
#         print splitTable[i][j-1] + 4, i-3
        for split in range(int(min(splitTable[K-1:,j-1])+4), i+1, 1):
        
            splitCost = costTable[split-4][j-1] + cost(sortedList[split-3: i+1])
                
            if splitCost < minCost:
                minCost = splitCost
                
                splitIndex = split
                splitTable[i][j] = split
                prevDict[(i,j)] = (split-4, j-1)
                
        costTable[i][j] = minCost
#         if splitIndex != 0: 
            
#             print splitIndex, i,j
            



# In[48]:


def getSplitList(dictionary):
    currentSplit = max(dictionary, key=lambda x: x[0] * 10000000 + x[1])
    splitList = [currentSplit[0]]
    while(currentSplit in dictionary):
        currentSplit = dictionary[currentSplit]
        splitList.append(currentSplit[0])
    return sorted(splitList)


# In[49]:


def transformAnon(ls, dictionary):
    splitList = getSplitList(dictionary)
    lastSplit = -1
    output = []
    for split in splitList:
        median = int(round(np.median(ls[lastSplit +1: split+1])))
        output += [median] * (split - lastSplit)
        lastSplit = split
    return output


# In[50]:


transformedList = transformAnon(sortedList, prevDict)


# In[51]:


reverseSortIndex = np.argsort( sortIndex)


# In[52]:


outputList = [ transformedList[rIndex] for rIndex in reverseSortIndex]



df[0] = outputList
df.to_csv(sys.argv[1],header=None, index=None)


# In[ ]:




