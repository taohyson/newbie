
# coding: utf-8

# ### 判断结构

# In[3]:


tang = 100
if tang > 200:
    print('OK')
print('test')


# In[5]:


tang = 50
if tang > 200:
    print(200)
elif tang < 100:
    print(100)
else:
    print('100-200')


# In[6]:


tang=[123,456,789]
if 123 in tang:
    print('OK')


# In[7]:


tang = {'tang':123,'yudi':456}
if 'tang' in tang:
    print('OK')

