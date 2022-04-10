#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:49:37 2022

@author: jackyhuang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:05:41 2022

@author: jackyhuang
"""

# PPHA 30535
# Spring 2021
# Homework 1

# Yijie Huang
# Yijie Huang

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

my_dict = {'a' : 40, 'b': 50 , 'c': 60 , 'd':70}

for key,val in my_dict.items():
    print('The value at position', key, 'is',val)


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.



#radar
def isPalindrome(s):
    return l == l[::-1]

l = 'radar'
ans = isPalindrome(l)

if(ans):
    print('Yes')
else:
    print('No')




#A man, a plan, a canal, Panama!
def is_palindrome(z):
    z= z.casefold()
    z= reversed(z)
    z= 'A man, a plan, a canal, Panama!'
    
if list(z) == list(z):
   print("Yes")
else:
   print("No")


    
    
#apple
def isPalindrome(a):
    return a == a[::-1]

a = 'apple'
ans = isPalindrome(a)

if(ans):
    print('Yes')
else:
    print('No')


#This isn't a palindrome
def isPalindrome(b):
    return b == b[::-1]

b = "This isn't a palindrome"
ans = isPalindrome(b)

if(ans):
    print('Yes')
else:
    print('No')



# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')

choice1 = ('radish')

for l in available_vegetables:
    if l == 'choice1':
        print("Yes,I got it!")
        break
    else:
        print("Please pick a vegetable I have available",available_vegetables)
        continue





# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

City = ['Chicago','Seattle','Syracuse','New York', 'Arizon','Boston']


with_s = [x for x in City if x.startswith("A")]


without_s = [x for x in City if x not in with_s]


new_city = [x.lower() for x in City if x.startswith("A") or x.startswith("B")]

print(new_city)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]

start_list.reverse()


new_list5 = [x*2 for x in start_list]


print(new_list5)


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

dict_state = dict(zip(short_names, long_names))

print(dict_state)




