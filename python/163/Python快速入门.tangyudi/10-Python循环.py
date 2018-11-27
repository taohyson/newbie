
# coding: utf-8

# ### 循环结构

# In[1]:


tang = 0
while tang < 10:
    print(tang)
    tang += 1


# In[2]:


tang = {'tang','yu','di'}
while tang:
    print(tang.pop())


# In[4]:


tang = {'tang','yu','di'}
for name in tang:
    print(name)


# In[6]:


tang = 100
for i in range(10):
    print(i)


# In[7]:


tang = [123,456,1234,24321432,15325325,1432352]
for i in range(3):
    print(tang[i])


# In[8]:


for i in range(len(tang)):
    print(tang[i])


# In[9]:


tang = {10,11,12,13,14,15}
for i in tang:
    if i%2 ==0:
        print(i)
    else:
        continue;
    print(i)


# In[10]:


for i in tang:
    if i%2==0:
        print(i);
    else:
        break;
    print(i);

