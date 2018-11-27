
# coding: utf-8

# In[1]:


get_ipython().run_cell_magic('writefile', 'tang.txt', 'tang yu di\nhello python\nhello world')


# In[8]:


txt = open("tang.txt")
print(txt.read())
txt.close()


# In[9]:


txt = open("tang_write.txt",'w')
txt.write('it is sunny today\n')
txt.write('it is cold today')
txt.close()


# In[15]:


txt = open("tang_write.txt",'a')
txt.write('it is sunny today\n')
txt.write('it is cold today')
txt.close()


# In[16]:


with open('tang_write.txt','w') as f:
    f.write('today is good')

