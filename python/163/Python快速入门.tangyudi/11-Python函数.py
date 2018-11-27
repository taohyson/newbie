
# coding: utf-8

# ### 函数

# In[1]:


def add(a,b):
    return a+b;

add(10,20)


# In[2]:


add(3,4,5)


# In[3]:


add(3)


# In[4]:


def add(a=1,b=2):
    return a+b;
add()


# In[5]:


add(3)


# In[6]:


add(b=3)


# In[7]:


add(3,b=3)


# In[8]:


def add(a,*args):
    for i in args:
        a+=i;
    return a

add(1,2,3,4)


# In[9]:


def add(a,**kwargs):
    for arg,value in kwargs.items():
        print (arg,value)
add(1,x=2,y=3)


# In[10]:


def add(a,*args):
    b = 0;
    for i in args:
        a+=i;
        b+=a;
    return a,b

add(1,2,3,4,5)


# In[11]:


a,b=(15,43)
print(a)
print(b)

