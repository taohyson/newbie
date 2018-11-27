
# coding: utf-8

# ### 集合结构
# * 数据项的组合

# In[4]:


tang = {123,123,456,456}
tang


# In[5]:


tang = set({123,123,456,789})
tang


# In[6]:


tang = {1,1,1,1,2,3,4}
tang


# ### 集合操作

# In[7]:


a = {1,2,3,4}
b = {2,3,4,5}
a.union(b)


# In[8]:


b.union(a)


# In[9]:


a|b


# In[10]:


a.intersection(b)


# In[11]:


b.intersection(a)


# In[12]:


a&b


# In[13]:


a.difference(b)


# In[14]:


b.difference(a)


# In[15]:


a - b


# In[16]:


b - a


# In[17]:


a = {1,2,3,4,5,6}
b = {2,3,4}
a.issubset(b)


# In[18]:


b.issubset(a)


# In[19]:


a > b


# In[21]:


b <= a


# In[22]:


a < a


# In[23]:


a = {1,2,3}
a.add(4)
a


# In[24]:


a.update([4,5,6])
a


# In[25]:


a.remove(1)
a


# In[26]:


a.pop()
a

