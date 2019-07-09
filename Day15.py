#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Introduction to default value ... in function
def describe_pet(pet_name,animal_type='dog'):
    """Display infor about a pet"""
    print (f"\nI have a {animal_type}.")
    print(f"my {animal_type}'s name is {pet_name}.'")


describe_pet ('jimmy','cat')


# In[13]:


# to return the output in dictinary format..

def build_person(first_name,last_name):
    """Return a dictionary of information about a person"""
    person = {'first':first_name,'last':last_name}
    return person
musician = build_person('akash','singh')
print(musician)


# In[19]:


#passing a for loop in the function.. !!
def greet_users(names):
    """print simple greeting to each user in the list"""
    for name in names:
        msg= f"Hello,{name.title()}!"
        print(msg)
        
usernames = [ 'raju','deeraj','mukul','mukund','akash']
greet_users (usernames)


# In[20]:


#passing an arbitary no of argument .. !!
def make_pizza(*toppings):
    """print the lsit of toppings that have been requested"""
    print (toppings)
    
make_pizza('mushroom','patato','olive')


# In[ ]:




