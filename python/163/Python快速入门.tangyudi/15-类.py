
# coding: utf-8

# ### 类：面向对象

# In[7]:


class people:
    '帮助信息XXX'
    blood = 100;
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        pass
    
    def display(self):
        print('blood:',self.blood)
        pass
    def display2(self):
        print(self.name);
        pass
    pass

people.__doc__


# In[9]:


p1 = people('tangyudi',30)
p2 = people('python',40)
p1.name


# In[5]:


p2.name


# In[10]:


p1.display()


# In[11]:


p2.display()


# In[12]:


p2.name = 'hello'


# In[13]:


p2


# In[14]:


p2.name


# In[15]:


del p2.name


# In[16]:


p2.name


# In[17]:


hasattr(p1,'name')


# In[18]:


hasattr(p1,'sex')


# In[19]:


getattr(p1,'name')


# In[20]:


setattr(p1,'name','yudiTang')


# In[21]:


p1.name


# In[22]:


delattr(p1,'name')


# In[23]:


p1.name


# ### 基有权限
# * 公有 public
# * 保护 _protected
# * 私有 __private
# * 元有: __doc|name|module|bases|dict

# In[25]:


people.__doc__


# In[26]:


people.__name__


# In[27]:


people.__module__


# In[28]:


people.__bases__


# In[30]:


people.__dict__


# In[10]:


class Parent:
    num = 100;
    def __init__(self):
        print("parent init...")
        pass
    def parentfun(self):
        print('parent func')
        pass
    def set(self, attr):
        self.attr = attr;        
        pass
    def get(self):
        print(self.attr)
        pass
    pass

class Child(Parent):
    def __init__(self):
        print('child init')
        pass
    def childfun(self):
        print('child func')
        pass
    
c = Child()
c.childfun()
c.parentfun()
c.set('zx')
c.get()
print(Child.__bases__)
print(Parent.__dict__)
print(Child.__dict__)
c.__dict__

