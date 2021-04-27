#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sys
import math


# In[1]:


someNumber=12
print(someNumber)


# In[2]:


doubledNumber=12*2
print(doubledNumber)


# In[6]:


someNumber=1353
print(someNumber)
print(type(someNumber))
print(type(doubledNumber))
print(type(1234))


# In[7]:


someNumber="ABC"
print(someNumber)
print(type(someNumber))


# In[8]:


long= 23452345678967890987
print(long)


# In[9]:


reallylong=long * long
print(reallylong)


# In[10]:


print(type(reallylong))


# In[12]:


hexadecimal =0xFFFF #0-9 A-F
print(hexadecimal)
print(hex(hexadecimal))


# In[17]:


#octal=0o012345678
octal=0o1234567
print(octal)
print(oct(octal))


# In[19]:


binary=0b0110110
print(binary)
print(bin(binary))


# In[21]:


float1=123.456
print(float1)
print(type(float1))


# In[22]:


float2=1234234534567896.3456
print(float2)


# In[23]:


print(type(float2))


# In[24]:


float3=12345678901234567.12345
print(float3)


# In[30]:


biggestFloat=sys.float_info.max
print(biggestFloat)
print(biggestFloat * 2)
if biggestFloat*2 == math.inf:
    print("infinity!")


# In[32]:


smallestFloat= sys.float_info.min
print(smallestFloat)


# In[34]:


expFloat=1.23e12
print(expFloat)


# In[35]:


i=12345
print(type(i))
print(i)


# In[36]:


f=1234.123
print(f)
print(type(f))


# In[37]:


whatIsIt=i*f
print(whatIsIt)
print(type(whatIsIt))


# In[38]:


someFloat=123456.789
print(someFloat)


# In[39]:


someInt=int(someFloat)
print(someInt)


# In[40]:


someInt=(int)(someFloat)
print(someInt)


# In[ ]:




