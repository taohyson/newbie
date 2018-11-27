
# coding: utf-8

# In[ ]:


### 列表结构
* 【】
* 元素随意


# In[1]:


tang = []
type(tang)


# In[2]:


tang = [1,2,3,4]
tang


# In[4]:


tang = ['1','2','3','4']
tang


# In[5]:


tang = [1, '2', 'tang']
tang


# In[6]:


tang = list([1,2,3])
tang


# ### list操作

# In[9]:


a = [123, 456]
b = ['tang', 'yudi']
a+b


# In[28]:


a * 2


# ### list索引

# In[11]:


a[0]


# In[12]:


a[-1]


# In[13]:


a[0:]


# In[15]:


a[:1]


# In[16]:


a[0]=789
a


# In[17]:


a[:]=['tang', 'yudi']
a


# In[19]:


a = [1,2,3,4,5,6,7]
a[4:7]


# In[20]:


del a[0]
a


# In[21]:


del a[3:]
a


# In[23]:


c = [1,2,3,4,5,6,7,8,0]
8 in c


# In[24]:


8 not in a


# In[29]:


9 in c


# ### 二维list

# In[31]:


tang = [[1,2],[3,4]]
tang[1][0]


# ### list函数

# In[26]:


len(tang)


# In[32]:


tang=['apple','banana','apple','banana','apple','banana','apple','banana']
tang.count('apple')


# In[33]:


tang.index('apple')


# In[34]:


tang.append('tang')


# In[35]:


tang.append('yudi')
tang


# In[36]:


tang.append(['tang', 'yudi'])
tang


# In[37]:


tang.insert(2,'python')
tang


# In[38]:


tang.remove(['tang','yudi'])
tang


# In[39]:


tang.remove('apple')
tang


# In[40]:


tang.pop(1)
tang


# In[41]:


tang = [1,2,3,9,6,2,3]
tang.sort()
tang


# In[42]:


tang = [1,2,3,9,6,2,3]
tang2 = sorted(tang)
print(tang)
tang2


# In[43]:


tang = ['di','yu','tang']
tang.reverse()
tang

