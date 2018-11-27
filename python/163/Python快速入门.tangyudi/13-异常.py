
# coding: utf-8

# In[3]:


import math

for i in range(10):
    input_number = input("write a number:")
    if (input_number) == 'q':
        break;
    result = math.log(float(input_number))
    print(result)


# In[5]:


import math

for i in range(10):
    try:
        inn = input("a number: ")
        if (inn == 'q'):
            break;
        print(math.log(float(inn)))
    except ValueError:
        print('must > 0')
    except Exception:
        print('exception')


# In[ ]:


class TangError(ValueError):
    pass
class Tang2Error(ValueError):
    pass

cur_list = ['tang','yu','di']
while True:
    cur_input = input()
    try:
        if cur_input not in cur_list:
            raise TangError("invalid input")
        elif cur_list.index(cur_input) == 0:
            raise Tang2Error("first")
        else:
            raise Exception("other")
    except TangError:
        print("invalid")
    except Tang2Error:
        print("forbidden")
    except Exception:
        print("OK")

