
# coding: utf-8

# （一）利用递归方法求5!

# In[4]:


def factorial(j):
    if j==0:
        return 1;
    return j*factorial(j-1);
for i in range(10):
    print(factorial(i));


# （二）利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

# In[7]:


def reverse(s,l):
    if l==0:
        return;
    print(s[l-1]);
    return reverse(s,l-1);
s = input()
reverse(s, len(s))


# （三）按逗号分隔列表

# In[9]:


L = ['tang','yu','di']
print(','.join(L))
';'.join(str(n) for n in L)


# （四）将一个数组逆序输出

# In[13]:


a = [5,6,7,8,9,1]
n = len(a)
for i in range(int(n/2)):
    a[i],a[n-1-i] = a[n-1-i],a[i]
    pass
a


# （五）两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

# In[21]:


X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
Y = [[10,2,3],
    [4,50,6],
    [7,8,90]]
Z = [[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(3):
    for j in range(3):
        Z[i][j]=X[i][j]+Y[i][j]
        pass
    pass
for z in Z:
    print(z)


# （六）匿名函数求和

# In[22]:


ret = lambda x,y:x+y
ret(3,5)


# （七）查找字符串的位置

# In[23]:


s1 = "efdfefasfefpjfas"
s2 = "efpjf"
s1.find(s2)


# （八）在字典中找到年龄最大的人，并输出

# In[27]:


people = {'wang':40,'tang':60,'zhang':30}
maxage = max(people.values())
for key in people.keys():
    if people[key] == maxage:
        print (key,people[key])


# （九）列表转换为字典

# In[30]:


item1 = ['tang','yu']
item2 = [10,20]
dict([item1,item2])


# （十）从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

# In[32]:


s = input()
f = open('test.txt','w')
f.write(s.upper())
f.close()

f = open('test.txt','r')
s2 = f.read()
f.close()
s2

