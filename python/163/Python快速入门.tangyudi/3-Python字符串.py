
# coding: utf-8

# ### 字符串运算

# In[2]:


'hello' + ' world'


# In[4]:


'hello ' *3


# ### 字符串函数

# In[25]:


len('1 2 3 4 5')


# In[23]:


tang = '1 2 3 4 5'
tang.split()


# In[6]:


tang_2 = ' '
tang_2.join(tang)


# In[8]:


tang = 'hello python'
tang_3 = tang.replace('python', 'world')
tang_3


# In[11]:


tang_4 = tang_3.upper()
tang_4


# In[12]:


tang_4.lower()


# In[13]:


tang_5 = '       hello python     '
tang_5.strip()


# In[14]:


tang_5.lstrip()


# In[15]:


tang_5.rstrip()


# In[16]:


'{} {} {}'.format('tang', 'yu', 'di')


# In[17]:


'{2} {1} {0}'.format('tang', 'yu', 'di')


# In[19]:


'{tang} {yu} {di}'.format(tang=20,yu=10,di=0)


# In[21]:


tang = 'tang yu di:'
a = 123
b = 456
c = 789
result = '%s %f %d' % (tang, b ,c)
result

