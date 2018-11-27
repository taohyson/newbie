
# coding: utf-8

# ### 字典结构

# In[1]:


tang = {}
type(tang)


# In[2]:


tang = dict()
type(tang)


# In[5]:


tang


# ### 字典操作
# key-value

# In[7]:


tang['first']='123'
tang


# In[10]:


tang['python']=456
tang


# In[11]:


tang['python']=789
tang


# In[12]:


tang = {'tang':123,'yu':456,'di':789}
tang


# In[13]:


tang[0]


# ### 二维字典

# In[14]:


tang = {}
tang['yudi']= [1,2,3]
tang['d1'] = {'tang':1,'yudi':2}
tang['d2'] = {'tang':'hello', 'yudi':'world'}
tang


# In[15]:


tang['tang'] = 10
tang['tang'] += 1
tang


# In[16]:


tang.get('fengzi','meiyou')


# In[17]:


tang.pop('tang')


# In[18]:


tang


# In[19]:


del tang['yudi']
tang


# In[20]:


tang = {'tang':123,'yudi':456}
tang2 = {'tang':789,'python':888}
tang.update(tang2)
tang


# In[21]:


'tang' in tang


# In[22]:


'hello' in tang


# In[23]:


'world' not in tang


# In[24]:


tang.keys()


# In[25]:


tang.values()


# In[26]:


tang.items()

