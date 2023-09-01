#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TOPIC: Python Basics Variable


# In[ ]:


"""1. Declare two variables, `x` and `y`, and assign them integer values. Swap the
values of these variables without using any temporary variable."""


# In[14]:


x=10
y=12
x,y=y,x
print("x=",x)
print("y=",y)


# In[ ]:


"""2. Create a program that calculates the area of a rectangle. Take the length and
width as inputs from the user and store them in variables. Calculate and
display the area."""


# In[9]:


x=int(input("Enter the lenght of reactangle:"))
y=int(input("Enter the width of rectangle:"))
z=print("The area of rectangle is:",x*y,"cm")


# In[ ]:





# In[ ]:


"""Write a Python program that converts temperatures from Celsius to
Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
convert it to Fahrenheit, and display the result."""


# In[11]:


x=int(input("What was the temperature today?:"))
y=((x*9/5)+32)
print("Today Temperature was",y,"Fahrenheit")


# In[ ]:





# In[15]:


#TOPIC: String Based Questions


# In[ ]:


"""1. Write a Python program that takes a string as input and prints the length of
the string."""


# In[17]:


str=input()
size=len(str)
print("The lenght of given string is ",size,"letters.")


# In[ ]:





# In[ ]:


"""2. Create a program that takes a sentence from the user and counts the number
of vowels (a, e, i, o, u) in the string."""


# In[22]:


str1=input("Write a sentence?:").lower()
a=str1.count("a")
e=str1.count("e")
i=str1.count("i")
o=str1.count("o")
u=str1.count("u")
number_of_vovals=(a+e+i+o+u)
print("Sentence have",number_of_vovals,"number of vovals.")


# In[ ]:





# In[ ]:


"""3. Given a string, reverse the order of characters using string slicing and print
the reversed string."""


# In[26]:


str1="PW skills"
reversed_str1=str1[-1::-1]
print("The reversed string looks like this",reversed_str1,".")


# In[ ]:





# In[ ]:


"""4. Write a program that takes a string as input and checks if it is a palindrome
(reads the same forwards and backwards)."""


# In[32]:


user_input = input("Enter a string: ")
cleaned_string = user_input.replace(" ", "").lower()
result = user_input + " is a palindrome!" if cleaned_string == cleaned_string[::-1] else user_input + " is not a palindrome."
print(result)


# In[ ]:





# In[ ]:


"""Create a program that takes a string as input and removes all the spaces from
it. Print the modified string without spaces."""


# In[33]:


str1=input()
print(str1.replace(" ",""))


# In[ ]:


# i hope you like my assignment.

