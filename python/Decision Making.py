#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=5
if x==5:
    print("x is 5")
    print("See me!!")
    


# In[6]:


if x>=5:
    print("x >= 5")
if x != 4:
    print("x != 4")


# In[9]:


y=9
if x>0 and y > 0:
    print("x and y are positive")


# In[10]:


if x>0 or y>0:
    print(" x or y is positive")


# In[11]:


if x>0 or y<0:
    print(" x or y is positive")


# In[14]:


x=-10
if x<0:
    print("x is negative")
elif x>0:
    print("x is positive")
else:
    print("x is zero")


# In[20]:


x=-1
y=-2
if x==0 and y==0:
    print("Point at origin")
elif x ==0 and y != 0:
    print("Point are at y axis")
elif x !=0 and y==0:
    print("Point are at x axis")
else:
    if x>0 and y>0:
        print("Point in quadrant 1")
    elif x>0 and y<0:
        print("Point in quadrant 4")
    elif x<0 and y>0:
        print("Point in quadrant 2")
    elif x<0 and y<0:
        print("Point in quadrant 3")


# In[23]:


x=10
if x%2==0:
    pass
else :
    print("Odd")


# In[ ]:




