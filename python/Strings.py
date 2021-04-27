#!/usr/bin/env python
# coding: utf-8

# In[1]:


fname="Ripa"
lname='Shah'


# In[2]:


print(fname + " "+ lname)


# In[3]:


print(lname + "123")


# In[4]:


print(lname+ str(123))


# In[5]:


s1="This is a long string"
print(len(s1))


# In[6]:


s2= "   Lots of spaces in here     "
print(s2)


# In[7]:


print(">"+s2+"<")


# In[8]:


print(">"+s2.lstrip()+"<")


# In[9]:


print(">"+s2.rstrip()+"<")


# In[10]:


print(">"+s2.strip()+"<")


# In[11]:


s3="ABCDEF"
print("Does s3 starts with 'A'?" + str(s3.startswith("A")))


# In[12]:


print("Does s3 starts with 'B'" + str(s3.startswith("B")))


# In[13]:


print("Does s3 ends with 'Z'"+ str(s3.endswith("Z")))


# In[14]:


url="http://www.python.org"
print("Does url starts with http?"+ str(url.startswith("http")))


# In[15]:


print("Does url starts with https?" + str(url.startswith("https")))


# In[16]:


s4="This is a test"
print(s4)


# In[17]:


print(s4.upper())


# In[18]:


print(s4.lower())


# In[19]:


s5="I really should capitalize first letter of a sentence"
print(s5.capitalize())
print(s5.title())


# In[23]:


just="Justify me"
print(">"+just.ljust(25)+"<")
print(">"+just.center(25)+"<")
print(">"+just.rjust(25)+"<")
print(">"+just.ljust(9)+"<")#does not trim


# In[5]:


s6="abcdefghijklmnopqrstuvwxyza"
print(s6.find("j"))


# In[3]:


index=s6.find("8")
print(index)


# In[4]:


print(s6.rfind("j"))


# In[6]:


print(s6.rfind("a"))


# In[7]:


print(s6.rfind("a",2))


# In[8]:


print(s6.index('a'))


# In[10]:


#print(s6.index('8'))


# In[14]:


sAlpha="asphaertakk"
sNumeric="12345345234"
sMixed= sAlpha + sNumeric
print("sAlpha is alpha?" + " "+str(sAlpha.isalpha()))


# In[16]:


print("sAlpha is numeric?" +" "+ str(sAlpha.isnumeric()))


# In[17]:


print("sNumeric is alpha:"+ " "+ str(sNumeric.isalpha()))


# In[18]:


print("sNumeric is numeric:"+ " "+ str(sNumeric.isnumeric()))


# In[19]:


print("sMixed is alpha:"+" "+ str(sMixed.isalpha()))
print("sMixed is numeric:" +" "+ str(sMixed.isnumeric()))
print("sMixed is alnum:"+" "+str(sMixed.isalnum()))


# In[20]:


s7="tyres"
print(s7)
print(s7.replace("y","i"))


# In[26]:


s8="Hello World"
print(s8)
print(s8[2:])
print(s8[:2])
print(s8[2:6])
print(s8[:-2])
print(s8[:-3])
print(s8[-2:])


# In[27]:


phone="678-789-5678"
split=phone.split("-")
print(split)


# In[28]:


areaCode=split[0]


# In[29]:


print(areaCode)


# In[33]:


prefix=split[1]
lineNumber=split[2]
print(prefix)
print(lineNumber)
print("("+ areaCode+")-"+prefix+"-"+lineNumber)


# In[31]:


newPhone=".".join(split)


# In[32]:


print(newPhone)


# In[34]:


newPhone=str.join(".",split)
print(newPhone)


# In[39]:


fname = "Ripa"
lname = "Shah"
print(f"We can embed variables like '{fname}' directly in our strings!")


# In[42]:


print(f"We can also make function calls in the braces! See:{fname.upper()}")


# In[43]:


print(f"Embed multiple variables and constants {fname},{lname} age:{25}")


# In[47]:


print("What about decimal places? Sure:${25.1256:0.2f}")


# In[52]:


fname="Jamie"
lname="Williams"
salary=654321
print(f"{lname.ljust(20)} {fname} ${salary:.2f}")
print(f"{lname:<20} {fname:<15} ${salary:>12,.2f}")
fname="Ripa"
lname="Shah"
salary=85000
print(f"{lname:<20} {fname:<15} ${salary:>12,.2f}")


# In[ ]:




