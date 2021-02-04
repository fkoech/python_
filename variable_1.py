#!/usr/bin/env python
# coding: utf-8

# In[1]:


#hello guys, once again it Felix or fkoech taking you through this youtube tutorial.
# Today were are going to learn about variables
#so what are variables?
#how can you decare and use variables? 
# We will end up our tutorial with a simple example of variable swapping.
# so we can define variable as a memory location.
# should have a meaningful name for easy reference
#It can change in value.
#example
name = "felix"
print(name)


# In[4]:


#Example demostration on how  variable change in value
name = "Koech"
#print(name)
#le me try to assign a different value to the name and call it again if it can give us name value as koech
name = "Ninja"
print(name)
# you can realise that the initial value have change from koech to Ninja, why? because we have defined the variable name with a
#different value.


# In[10]:


#So we can say that variable should contain a unique name, and  should also follow  the naming convential for variable
# now let us  finish our descusion on variable with a simple practical of swapping in the values of different variables
#Let us take for an example that we have two variable  name and registration_number, and in by bad luck we interchanged the value of this
# of this variable.So how can we interchange their values gain?
name = "1033994"
registration_number = "Felix"
#print(str(name ) + registration_number)
# you have realised that i have used two important concept here, the + sign and str().The + sign is used to concatinate two strings or string with variable but not numbers and a string that is why i have converted number  to string for it to concatinate.

#so now le us try to introduce a temporary variable temp, you can refer it with any other name.
temp = name
name =registration_number
registration_number = temp
print(name)
print(registration_number)
# you have realised that the value for name have changed from 1033994 to Felix and for registration   also.
# in this case it may look uneccessary but it can be applicable in complex situation.


# In[ ]:


Thank you very much and  please  share, subcribe and  like my video for more tutorials

