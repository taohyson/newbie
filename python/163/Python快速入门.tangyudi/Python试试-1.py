
# coding: utf-8

# ### Python试题

# （一）有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# In[6]:


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (j!=k) and k!=i:
                print(i*100+j*10+k)


# （二）企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# In[2]:


i = int(input())
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
result = 0
for idx in range(len(arr)):
    if i > arr[idx]:
        result += (i-arr[idx])*rat[idx]
        i -= arr[idx]
        pass
    pass
result


# （三）输入三个整数x,y,z，请把这三个数由小到大输出

# In[4]:


my = [];
for i in range(3):
    x = int(input())
    my.append(x)
    pass
my.sort()
my


# （四）将一个列表的数据复制到另一个列表中

# In[5]:


a = [1,2,3]
b = a[:]
b


# （五）暂停一秒输出,并格式化当前时间。使用 time 模块的 sleep() 函数。

# In[7]:


import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))


# （六）打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# In[9]:


for h in range(1,10):
    for t in range(0,10):
        for u in range(0,10):
            num = h*100+t*10+u
            if (num == pow(h,3)+pow(t,3)+pow(u,3)):
                print(num)
                pass
            pass
        pass
    pass
pass


# （七）输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# In[12]:


s = input()
letters,spaces,digits,others = 0,0,0,0
for c in s:
    if c.isalpha():
        letters += 1;
        pass
    elif c.isspace():
        spaces += 1;
        pass
    elif c.isdigit():
        digits += 1;
        pass
    else:
        others += 1;
        pass
    pass
print('%d %d %d %d' % (letters,spaces,digits,others))


# （八）一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# In[13]:


h = 100
time = 10
heights = []
for i in range(2,time+1):
    h /= 2
    heights.append(h)
    pass
print(sum(heights)*2+100)
print(min(heights)/2)

