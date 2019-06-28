#!/usr/bin/env python
# coding: utf-8

# In[3]:


#mutable - which can be changed
#imutable - which canot be changed
#a String & b. Tuple

#Modifying value of a disc
Board ={'color': 'red'}

print (f"the color of the board is {Board['color']}.")
        
Board['color'] = 'blue'
        
print (f"the color of the board is {Board['color']}.")


# In[4]:


#deleteing the valur in dictionary
value = {'color':'red', 'points':10}
print (value)
del value ['points']
print (value)


# In[5]:


#declaring simlar kind of objects
#best practice to follow  while declaring the dictionaries
language = {'raj': 'groovy','ritesh':'java','jain':'swift','akash':'yaml',
           }
lang = language['akash'].title()

print(f"akash lanugaue is {lang}.")


# In[6]:


#key errors
language = {'raj': 'groovy','ritesh':'java','jain':'swift','akash':'yaml',
           }
lang = language['raju'].title()

print(f"akash lanugaue is {lang}.")


# In[7]:


#how to avoid key errors by using get() function in dictionary
# we can call the key and also declare a masg to be printed if that is missing in given key
#dictionary
value = {'color':'red', 'speed':'slow'}
print (value['points'])





# In[10]:


value = {'color':'red', 'speed':'slow'}
print(value['points'])
solution =value.get('points','points are not declared')
print(solution)


# In[ ]:




