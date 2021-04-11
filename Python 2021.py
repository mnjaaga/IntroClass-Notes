#!/usr/bin/env python
# coding: utf-8

# # Variables

# In[1]:


#how to get keywords in python - Key words should never be used as variable names

import keyword
s = keyword.kwlist
print(s)


# In[3]:


greetings = "Habari gani"
print(greetings)


# In[2]:


#assign a single value to several variables simultaneously

a = b = c = f = 19
print(a)
print(b)
print(c)
print(f)


# In[1]:


# number values allowed in python

x = 5
y = 2
z = 2+3j
b = 4.99


# In[4]:


print(x)


# In[5]:


print(y)


# In[6]:


# how to check the data type of a variable

print(type(z))


# # Arithmetic operators

# In[4]:


# Arithmetic operators are used with numeric values to perform common mathematical operations


# Arithmetic operators 

print(x % y)


# ![image.png](attachment:image.png)

# In[5]:


# Arithmetic operators (floor division)

print(x // y)


# ![image.png](attachment:image.png)

# In[14]:


# Assignment operators are used to assign values to variables

x = 5

x -= 3

print(x)


# #Note:   int + int/ str + str
# 
#          Input() & print() receive values as string
# 

# # (+) for arithmetic & concat

# In[20]:


num3 = int(input("Enter num3 value: "))
num 
#num1 = int(input("Enter the value for num1: "))
#num2 = int(input("Enter the value for num2: "))

#sum = num1 + num2
#print(sum)


# # Comparison Operators

# In[2]:


# Comparison operators are used to compare two values (==, !=, >, <, >=, <=)
# Comparison operators


x < y


# In[ ]:


# =, ==

x = 7
print(x)
x == 5


# ## Logical Operators

# In[ ]:


# logical operators (and)

# Returns True if both statements are true

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10


# In[ ]:


# logical operators (or)
#Returns True if one of the statements is true

x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


# In[ ]:


# logical operators (not)
# Reverse the result, returns False if the result is true

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


# # Identify Operators

# In[ ]:


# identify operators(is)

# Returns True if both variables are the same object

x = ["ugali", "nyamchom"]
y = ["ugali", "nyamchom"]
z = x


print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# In[ ]:


# identify operators(is not)

# Returns True if both variables are not the same object

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


# # Membership Operators

# In[ ]:


# Membership operators(in)
# Returns True if a sequence with the specified value is present in the object

students = ["Lucy", "Nique", "Emster"]

print("Nique" in students)

# returns True because a sequence with the value "Nique" is in the list


# In[ ]:


# Membership operators(not in)
# Returns True if a sequence with the specified value is present in the object

students = ["Lucy", "Nique", "Emster"]

print("Jose" in students)

# returns True because a sequence with the value "Jose" is not in the list


# # practice code, see if you can fix the errors

# In[ ]:


num1 = int(input("Enter the value for num1: "))
num2 = int(input("Enter the value for num2: "))

sum = num1 + num2
print("Sum = " + sum)


# In[ ]:


num1 = int(input("Enter the value for num1: "))
num2 = int(input("Enter the value for num2: "))

sum = num1 + num2
print("Sum = " + str(sum))


# ![image.png](attachment:image.png)

# In[ ]:




