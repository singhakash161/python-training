#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Intro to phyton Class
#use the advantage of oops concept
# a class is the set of instruction to be perfromed
#1.Class.. 2. Object(also caled as instance)...3.Method(function)
#invoking.. something for performing an opetration
#Classs name need to define


# In[ ]:


#creating the class
class Dog:
    """A simpl attempt to model a dog"""
def __init__(self,name,age):
#this is called method
#init-invoke writing the class mandatory to define init, __before after__
#self is the parameter need to be define itself 
#self.name is the parameter below defined as a variable =name'
    """Initialization name & age atttribute"""
    self.name=name
    self.age=age

def sit(self):
    """Siulating a sitting response for the dog"""
    print(f"{self.name} is now sitting")
    
def roll_over (self):
    """simulating therollover command response to the dog"""
    print(f"{self.name} rolled over")
    
my_dog = Dog("Alex",6)
# this is the argurument for the method or the fuction

