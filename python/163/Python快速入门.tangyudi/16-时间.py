
# coding: utf-8

# In[1]:


import time


# In[3]:


time.time()


# In[4]:


time.localtime()


# In[5]:


time.asctime(time.localtime())


# In[6]:


time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())


# In[8]:


import calendar
print(calendar.month(2018,11))

