
# coding: utf-8

# In[8]:


get_ipython().run_cell_magic('writefile', 'tang.py', '\ntang_v = 10\n\ndef add(lst):\n    res = 0;\n    for i in range(len(lst)):\n        res += lst[i]\n    return res;\nprint(add([1,2,3,4,5]))')


# In[2]:


get_ipython().run_line_magic('run', 'tang.py')


# In[9]:


import tang


# In[10]:


import tang


# In[11]:


tang


# In[12]:


tang.tang_v


# In[13]:


tang.tang_v = 100
tang.tang_v


# In[14]:


tang.add([9,23,5465,123])


# In[15]:


import tang as tg
tg.tang_v


# In[16]:


tg.add([234,4534,123])


# In[17]:


from tang import tang_v, add
tang_v


# In[18]:


add([32,54,23])


# In[19]:


from tang import *
tang_v


# In[20]:


add([1,5,6,7])

